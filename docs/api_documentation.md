# PandutaXP API Documentation

## Authentication Endpoints

### Login

POST /api/auth/login/
Request Body:
{
    "username": "string",
    "password": "string"
}
Response: {
    "token": "string",
    "user_id": "integer"
}


### Register

POST /api/auth/register/
Request Body:
{
    "username": "string",
    "email": "string",
    "password": "string",
    "user_type": "client|provider"
}
Response: {
    "success": true,
    "user_id": "integer"
}


## Order Management

### Create Order

POST /api/orders/create/
Request Body:
{
    "service_id": "integer",
    "pickup_time": "datetime",
    "notes": "string"
}
Response: {
    "success": true,
    "order_id": "integer"
}


### Update Order Status

POST /api/orders/update-status/
Request Body:
{
    "order_id": "integer",
    "status": "accepted|in_progress|completed"
}
Response: {
    "success": true
}


## Service Management

### List Services

GET /api/services/
Response: {
    "services": [
        {
            "id": "integer",
            "name": "string",
            "description": "string",
            "price": "decimal",
            "duration": "integer"
        }
    ]
}


### Add Service

POST /api/services/add/
Request Body:
{
    "name": "string",
    "description": "string",
    "price": "decimal",
    "duration": "integer"
}
Response: {
    "success": true,
    "service_id": "integer"
}


### Get Provider Services

GET /api/providers/services
Response: {
    "services": [
        {
            "id": "integer",
            "name": "string",
            "description": "string",
            "price": "decimal",
            "duration": "integer"
        }
    ]
}


## Error Responses

{
    "status": "error",
    "error": "error_code",
    "message": "string"
}

