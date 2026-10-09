# FastAPI REST API Project

A Python REST API project built with **FastAPI**, **SQLAlchemy**, and **SQLite**. This project demonstrates backend development fundamentals, API structure, database integration, and working with Python web frameworks.

## Technologies Used

* **Python** — Backend programming
* **FastAPI** — Building REST APIs
* **SQLAlchemy** — Database interaction and ORM
* **SQLite** — Database storage
* **Pydantic** — Data validation and schemas
* **Uvicorn** — ASGI server
* **Git & GitHub** — Version control

## Project Structure

```text
fastapi-project/
├── main.py          # Application entry point and routes
├── database.py      # Database connection and configuration
├── models.py        # Database models
├── schemas.py       # Data validation schemas
├── products.db      # SQLite database
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/fastapi-project.git
cd fastapi-project
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

The application should now be running locally at:

http://127.0.0.1:8000

## API Documentation

FastAPI automatically generates interactive API documentation.

Once the application is running, visit:

* **Swagger UI:** http://127.0.0.1:8000/docs
* **ReDoc:** http://127.0.0.1:8000/redoc

These interfaces allow you to explore the available endpoints and test API requests.

## What I Learned

Through this project, I practised:

* Structuring a Python backend application into separate modules.
* Building REST API endpoints with FastAPI.
* Separating database models from request and response schemas.
* Connecting a Python application to a SQLite database using SQLAlchemy.
* Running and testing an API locally.
* Using Git and GitHub to manage source code.

## Future Improvements

* Add automated tests for API endpoints.
* Improve error handling and input validation.
* Add authentication and authorization.
* Deploy the application to a cloud hosting platform.
* Add further API functionality as the project evolves.

## Author

**Muhammad Junaid**

Electronics Engineering graduate transitioning into Python development, software automation, and AI engineering.

GitHub: https://github.com/mjunaidaus-tech
