from passlib.context import CryptContext # type: ignore
from datetime import datetime, timedelta
from jose import JWTError, jwt # type: ignore
from typing import Optional
from app.schemas import TokenData
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import User
from fastapi.security import OAuth2PasswordBearer

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login") 

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT settings
SECRET_KEY = "9f8d4e2e1b6a4a1e5a8e6f7c4d3b2a1f9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f" #generated randomly and added here
ALGORITHM = "HS256"
#expires after 30 minutes
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Hash a password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Create JWT token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Decode and verify JWT token
def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            return None
        return TokenData(email=email)
    except JWTError:
        return None
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate token")    