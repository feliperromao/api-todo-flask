# TODO API with Flask

This project has an objective to implement a REST API for study purposes

This is an REST API for CRUD(create, read, update and delete) resources in a database MongoDB

## How to install

`$ pip install -r requirements.txt`

## The TODOs

### List

**Path**: `/todo`

**Method**: `GET`

### Create

**Path**: `/todo`

**Method**: `POST`

**Body**:
```json
{
    "title": "string|required",
    "description": "string",
    "date": "date"
}
```