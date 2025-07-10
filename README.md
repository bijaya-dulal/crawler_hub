# crawler_hub
#  FastAPI To-Do API

A simple, secure To-Do REST API built with **FastAPI**, **SQLAlchemy**, and **JWT authentication**.

---

## 🚀 Features

- ✅ User registration & login with hashed passwords
- 🔐 JWT-based authentication
- 🗂️ Create, Read, Update, Delete (CRUD) to-dos
- 📆 Track created & updated timestamps
- 🧑‍💼 Per-user to-do management

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/bijaya-dulal/crawler_hub
```  

### 2. Create and Activate Virtual Environment


```bash
python -m venv env
source env/bin/activate      # On Windows: .\env\Scripts\activate

```  

### 3.install requirements.txt
```bash
pip install -r requirements.txt
```
### 4.to run app
```bash
uvicorn app.main:app --reload
```


# API ENDPOINTS
## auth
post /register       register the user
post /login          login
## todos
POST 
GET	/todos  	     Retrieve paginated list of user's todos
POST	/todos	     Create a new to-do item
PUT	/todos/{id}	     Update an existing to-do (partial OK)
DELETE	/todos/{id}  Delete a specific to-do