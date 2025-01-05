# PandutaXP API Documentation

## Authentication Endpoints
POST /api/auth/login/
POST /api/auth/register/

## Order Management
POST /api/orders/create/
- Request Body: {provider_id, service_type, pickup_date}
- Response: {success, order_id}

POST /api/orders/update-status/
- Request Body: {order_id, status}
- Response: {success}

## Service Management
GET /api/services/
POST /api/services/add/
