# FastAPI Task 0 - HNG Internship

This is a simple Project built with FastAPI with a single route that Retrieve Basic Information, including an email, the current datetime in ISO 8601 format, and a GitHub repository URL.

## Features
- Returns a JSON response with:
  - Email
  - Current datetime (UTC) in ISO 8601 format
  - GitHub repository URL

## Installation & Setup

### 1 Clone the Repository
```bash
git clone https://github.com/TYDev01/Hng12_Task_0.git
cd Hng12_Task_0


### 2 Create a Virtual Enviroment
    - python -m venv venv
    - source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3 Install Dependencies
  - pip install -r requirements.txt

### 4 Run the FastAPI App
    - uvicorn main:app --reload


### 5 Test the Endpoint
    - Once the server is running, visit:
        http://127.0.0.1:8000/home
            or use curl
    - curl http://127.0.0.1:8000/

<hr>
## Example JSON Response

{
    "email": "tonieschi@gmail.com",
    "current_datetime": "2025-01-29T14:30:45.123456Z",
    "github_url": "https://github.io/TYDev01.git/task0hng"
}



### My choosen programming language:
    - [text](https://hng.tech/hire/python-developers)
