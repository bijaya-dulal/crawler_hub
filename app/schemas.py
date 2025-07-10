from pydantic import BaseModel, EmailStr
from datetime import datetime

# Model for validating user input when creating a new user 
class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str

# Model for serializing user data in responses
class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str

    class Config:
        from_attributes = True

# Model representing the JWT token response after login 
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Model for holding the email extracted from the JWT token payload 
class TokenData(BaseModel):
    email: str | None = None

#create todo for user
class TodoCreate(BaseModel):
    task: str
    completed: bool = False

class TodoOut(BaseModel):
    id: int
    task: str
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True  # for Pydantic v2