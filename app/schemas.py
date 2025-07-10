from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import datetime
from typing import Optional, Annotated

NameStr = Annotated[str, StringConstraints(min_length=3)]

# Model for validating user input when creating a new user 
class UserCreate(BaseModel):
    email: EmailStr
    full_name: NameStr
    password: str

# Model for serializing user data in responses
class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: NameStr

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
    updated_at: Optional[datetime]


    class Config:
        from_attributes = True  # for Pydantic v2

class TodoUpdate(BaseModel):
    task: Optional[str] = None
    completed: Optional[bool] = None

    class Config:
        from_attributes = True        