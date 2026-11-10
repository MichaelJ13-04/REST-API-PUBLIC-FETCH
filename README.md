# REST API – Book Management System

## Project Overview

This project is a Flask-based REST API that allows users to retrieve and manage book information. It demonstrates how RESTful endpoints can be used to access and update data through HTTP requests.

The API returns book information in JSON format and includes a favorite books feature that allows users to store and view their favorite books.

## Technologies Used

- Python
- Flask
- REST API
- JSON
- Visual Studio Code

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/goodbooks` | Retrieves the available books |
| GET | `/goodbooks` | Returns book information in JSON format |

## Favorite Books Feature

The project includes a favorite books feature with the following information:

- Book ID
- Title
- Author
- Rating (1–5)

Books with a rating of 4 or higher are highlighted to make highly rated books easier to identify.

## Installation and Setup

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Install Flask:

```bash
pip install flask
```

5. Run the application:

```bash
python app.py
```

6. Open the API in your browser:

```text
http://127.0.0.1:5000/goodbooks
```

## Testing

The API can be tested using a web browser, PowerShell, or an API testing tool.

Example PowerShell request:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/goodbooks" -Method Get
```

## Project Purpose

The purpose of this assignment was to gain hands-on experience building a REST API with Flask, working with JSON data, creating API endpoints, and organizing book information. It also introduced the process of adding and displaying favorite books with ratings.
