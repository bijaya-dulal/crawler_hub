#this is used only once to create the table in db if 
# if you run twice it wont create the duplicate just deal with new tables 

from database import engine, Base
from models import User # import all  models here 



Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
