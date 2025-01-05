# PandutaXP API Documentation

## Authentication Endpoints

### Register User
- **URL**: `/accounts/register/`
- **Method**: POST
- **Body**:
  
  {
    "username": "string",
    "email": "string",
    "password1": "string",
    "password2": "string",
    "user_type": "CLIENT|PROVIDER"
  }
    