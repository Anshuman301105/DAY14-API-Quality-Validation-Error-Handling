# Day 14 – API Quality, Validation & Error Handling

## Objective

Improve the Employee Management API by adding validation, error handling, pagination, search, sorting, logging, and proper HTTP status codes.

## Features

* Input validation
* Consistent error responses
* HTTP status codes
* Pagination
* Search / filtering
* Sorting
* Logging
* Exception handling

## API Examples

### Pagination

```http
GET /employees?page=1&limit=20
```

### Search

```http
GET /employees?search=John
```

### Sorting

```http
GET /employees?sort=name
```

### Combined

```http
GET /employees?page=1&limit=20&search=John&sort=name
```

## Validation

The API handles:

* Invalid email
* Missing employee name
* Invalid department
* Duplicate employee ID

## Error Response

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid employee data"
  }
}
```

## HTTP Status Codes

| Code | Meaning          |
| ---- | ---------------- |
| 200  | Success          |
| 201  | Created          |
| 400  | Bad Request      |
| 404  | Not Found        |
| 409  | Conflict         |
| 422  | Validation Error |
| 500  | Server Error     |

## Folder Structure

```text
day-14-api-quality/
│
├── main.py
├── README.md
├── requirements.txt
│
├── schemas/
│   └── employee.py
│
├── routes/
│   └── employee.py
│
├── utils/
│   └── logging_config.py
│
└── tests/
    └── test_employee.py
```

## Run Project

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

#
