from fastapi import FastAPI
from app.routes import user
from app.database import engine, Base



app = FastAPI()

# Register routers
app.include_router(user.router)
