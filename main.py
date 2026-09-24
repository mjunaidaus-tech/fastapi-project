import os
from fastapi import FastAPI, Depends, HTTPException, Header
from database import engine, get_db, Base
from models import Product
from schemas import ProductCreate, ProductResponse
# import io
from dotenv import load_dotenv
load_dotenv()



app = FastAPI()
Base.metadata.create_all(bind=engine)
API_KEY = os.getenv("API_KEY")
#---------------------home route ------------------------#
@app.get("/")
def home():
    return {"message": "Hello World"}
#----------------------posting products-------------------#
@app.post("/products",response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate, db=Depends(get_db)):
    new_product = Product(
        name=product.name,
        price=product.price,
        quantity=product.quantity
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
#------------------GET all products----------------------#
@app.get("/products",response_model=list[ProductResponse])
def get_products(db=Depends(get_db)):
    products = db.query(Product).all()
    return products
#----------------GET one product------------------------#
@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db=Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


#--------------------updating a product PUT----------------#
@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate, db=Depends(get_db)):
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    existing_product.name = product.name
    existing_product.price = product.price
    existing_product.quantity = product.quantity
    db.commit()
    db.refresh(existing_product)
    return existing_product


#---------------------DELETE-----------------------------#
@app.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int, db=Depends(get_db)):
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(existing_product)
    db.commit()
    db.refresh(existing_product)
    return existing_product

#------------------------ASYNC IO-------------------------------#
# @app.get("/wait")
# async def wait():
#     await asyncio.sleep(3)
#     return {"message": "waited for 3 seconds"}
#------------------API key------------------------------------------#
@app.get("/secure")
def secure_endpoint(x_api_key: str = Header(...)):

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    return {"message": "Access granted"}