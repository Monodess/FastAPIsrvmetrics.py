# FastAPI python Server Metrics Capturer
# ---------Work is still in progress---------

Project for capturing web servers metrics and storing them into DB with backend API.
App receives a link with and checks its Health and captures GooglePagespeed metrics with storing it into DB.
After metrics captured, user can get data by sending request with specified filter.

## Key features:
- Asynchronous URL health checking.

- Automated Google PageSpeed metrics collection.

- Filtering system for historical data retrieval (in progress) 
## Stack used: 
- FastAPI + Pydantic, SQLAlchemy, alembic
- MySQL 8.0+
- Pagespeed API
- PyTests

## How to run tests: pytest

