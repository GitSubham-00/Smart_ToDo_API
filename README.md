# Smart ToDo API – Secure Task Management Backend

Smart ToDo API is a secure RESTful backend application that allows users to manage personal tasks with **JWT-based authentication**.  
Each user can create, view, update, and delete their own tasks securely through protected APIs.

The project is built to demonstrate **backend engineering fundamentals**, clean API design, authentication, and database integration.

---

## 🚀 Live Deployment

🔗 **Base API URL**  
https://smart-todo-api-uhpu.onrender.com

🔗 **Swagger Documentation (OpenAPI)**  
https://smart-todo-api-uhpu.onrender.com/docs

---

## 🚀 Project Overview

- REST API built using **FastAPI**
- JWT-based authentication (OAuth2 Password Flow)
- User-specific task management
- MongoDB as NoSQL database
- Fully deployed on **Render**
- Fully documented using **Swagger (OpenAPI)**

---

## 📌 Features

### 👤 Authentication
- User Registration
- User Login
- Secure password hashing using **bcrypt**
- JWT token-based authentication
- Protected routes using OAuth2

### 📝 Task Management
- Create tasks
- View all tasks for the logged-in user
- Update task details and completion status
- Delete tasks
- Tasks are **user-specific** (data isolation)

### 🔐 Security


### 📖 API Documentation
- Interactive Swagger UI
- Request/response schemas
- Built-in authorization support
- JWT-based authorization
- `Authorization: Bearer <token>` header validation
- Token verification on every protected route
- Secrets managed using environment variables
- No plaintext password storage
  
---

## 🧑‍💻 Tech Stack

### Backend
- Python
- FastAPI
- MongoDB
- OAuth2 + JWT
- Pydantic (data validation)

### Security & Utilities
- bcrypt (password hashing)
- python-jose (JWT handling)
- dotenv (environment configuration)

### API Documentation
- Swagger UI (OpenAPI 3.1)

---

## 📌 API Endpoints

### 🔐 Authentication
| Method | Endpoint | Description |
|------|---------|------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive JWT token |

---

### 📝 Tasks (JWT Protected)
| Method | Endpoint | Description |
|------|---------|------------|
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | Get all tasks of logged-in user |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

---

## 🔒 Authentication Flow

1. Register a new user using `/auth/register`
2. Login using `/auth/login`
3. Receive a JWT access token
4. Use the token in request headers:
   Authorization: Bearer <your_access_token>
5. Access protected task endpoints
   
---

## 🧪 Authorization Test (curl – Verified)

### 1️⃣ Login and get JWT token
```bash
curl -X POST https://smart-todo-api-uhpu.onrender.com/auth/login \
-H "Content-Type: application/json" \
-d '{
 "email": "your_email@gmail.com",
 "password": "your_password"
}'
```
Response
```bash
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 2️⃣ Access protected route using token
```bash
curl -X GET https://smart-todo-api-uhpu.onrender.com/tasks \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
✔ Returns tasks list (or empty array)
✔ Confirms JWT authorization is working correctly

---

## 📖 Swagger Documentation

After running the server locally, access Swagger UI at:
http://127.0.0.1:8000/docs

Swagger provides:
- Interactive API testing
- JWT authorization button
- Complete request/response schemas
  
## ⚠️ Important Note

Some browsers may show limitations with OAuth2 popup authorization in Swagger UI.
This is a known Swagger behavior.

For guaranteed verification, use:

- curl
- Postman
- Manual Authorization header

---

## ⚙️ Environment Variables

Create a `.env` file in the project root (do not commit it):

```env
MONGODB_URI=your_mongodb_connection_string
DATABASE_NAME=smart_todo_api
SECRET_KEY=your_jwt_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

### ▶️ Local Installation & Setup

---

### 1️⃣ Clone the Repository
```text
git clone https://github.com/your-username/smart-todo-api.git
cd smart-todo-api
```

### 2️⃣ Create Virtual Environment
```text
python -m venv venv


Activate it:

venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```text
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```text
uvicorn app.main:app --reload


Server will run at:

http://127.0.0.1:8000
```

---

### 📂 Project Structure

```text
smart-todo-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── tasks.py
│   │
│   ├── models/
│   │   └── task.py
│   │
│   ├── schemas/
│   │   ├── user_schema.py
│   │   └── task_schema.py
│   │
│   └── utils/
│       ├── auth_dependency.py
│       ├── jwt_handler.py
│       └── password_hash.py
│
├── requirements.txt
├── .env (not committed)
└── README.md

```

### 🔌 Assignment Requirements Fulfilled

✔ REST backend using Python (FastAPI)

✔ JWT-based authentication

✔ OAuth2 password flow

✔ NoSQL database (MongoDB)

✔ Secure password handling

✔ CRUD operations

✔ Swagger documentation

✔ Cloud deployment

✔ Production-ready API


---

⭐ Final Note (For Recruiters)

- This project demonstrates:

- Clean backend architecture

- RESTful API design

- Authentication and authorization using JWT

- Secure user data handling

- Real-world task management workflow

- Production-ready documentation using Swagger

---

👨‍💻 Author

Subham Maity


🔗 GitHub: https://github.com/GitSubham-00

🔗 LinkedIn: https://linkedin.com/in/subhammaity

⭐ If you found this project useful, feel free to star the repository!
