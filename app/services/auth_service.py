# Directory: app/services/auth_service.py
# NOTE: This is a placeholder for JWT auth logic

def register_user(data):
    return {"access_token": "mock", "token_type": "bearer"}

def login_user(data):
    return {"access_token": "mock", "token_type": "bearer"}

def refresh_token():
    return {"access_token": "mock", "token_type": "bearer"}

def logout_user():
    return {"message": "Logged out"}