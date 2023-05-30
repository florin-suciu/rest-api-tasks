# Test Practice REST API

This project provides a simple REST API that can be used for testing practice purposes. It allows you to manage tasks through various API endpoints. This README file provides an overview of the project and instructions on how to get started.

## Features

- User authentication using JWT (JSON Web Tokens)
- Create, read, update, and delete tasks
- SQLite database storage

## Prerequisites

- Python 3.x installed on your system
- `pip` package manager

## Getting Started

1. Clone the repository:
   ```bash
   git clone git@github.com:florin-suciu/rest-api-tasks.git


2. Change into the project directory:
   ```bash
    cd rest-api-tasks

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

4. Set up the local SQLite database:
- Run the following commands in your terminal or command prompt:
    ```bash
    python
- Once in the Python interactive shell, enter the following commands:
    ```bash
    from app import db
    db.create_all()
    exit()

5. Start the server:
    ```bash
    python app.py

6. The API will be accessible at http://localhost:5000.


## API Documentation
The API provides the following endpoints:

- `POST /auth/register`: Create a new user account.
- `POST /auth/login`: Log in to an existing user account and receive an authentication token.
- `GET /tasks`: Get a list of tasks.
- `GET /tasks/<task_id>`: Get details of a specific task.
- `POST /tasks`: Create a new task.
- `PUT /tasks/<task_id>`: Update an existing task.
- `DELETE /tasks/<task_id>`: Delete a task.

Please refer to the API documentation or the code itself for further details on the request/response format for each endpoint.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.