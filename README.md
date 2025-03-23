# 📚 Library Management System

## 📖 Overview
This is a **Library Management System** built using **Django & Django REST Framework (DRF)**. The system allows:
- **Admins** to manage books via **CRUD operations**.
- **Students** to view the book list.
- **Token-based authentication** for security.
- **MySQL or SQL Server** as the database.

---

## 🛠 Installation & Setup
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/shubhagith/library-management.git
cd library-management
```

### 2️⃣ **Create Virtual Environment & Activate**
```sh
python -m venv venv  # Create Virtual Environment

# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Database Configuration**
Create a `.env` file in the project root (`library_management/.env`) and add:
```
DB_ENGINE=mysql  # Change to sqlserver if using SQL Server
DB_NAME=library_db
DB_USER=mysqluser
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306  # 1433 for SQL Server
```

#### **For MySQL:**
```sh
python create_db.py  # Ensures DB & user exist
python manage.py migrate  # Apply migrations

---

## 🚀 Running the Server
```sh
python manage.py runserver
```
API available at: **`http://127.0.0.1:8000/`**

---

## 🔐 Authentication
### **Create Superuser (for Django Admin Panel)**
```sh
python manage.py createsuperuser
```
Access Admin Panel: **`http://127.0.0.1:8000/admin/`**

### **Admin Signup (API)**
- **URL:** `/api/auth/signup/`
- **Method:** `POST`
- **Body:**
```json
{
  "username": "admin1",
  "email": "admin@example.com",
  "password": "adminpassword"
}
```

### **Admin Login & Token Generation**
- **URL:** `/api/auth/login/`
- **Method:** `POST`
- **Body:**
```json
{
  "email": "admin@example.com",
  "password": "adminpassword"
}
```
- **Response:**
```json
{
  "token": "your_generated_token"
}
```

---

## 📚 Book Management (Admin Only)

### **Create a Book**
- **URL:** `/api/books/`
- **Method:** `POST`
- **Headers:**
```
Authorization: Token your_generated_token
Content-Type: application/json
```
- **Body:**
```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "9780743273565",
  "published_date": "1925-04-10"
}
```

### **View All Books (Student & Admin)**
- **URL:** `/api/books/`
- **Method:** `GET`

### **Update a Book**
- **URL:** `/api/books/{book_id}/`
- **Method:** `PUT`

### **Delete a Book**
- **URL:** `/api/books/{book_id}/`
- **Method:** `DELETE`

---

## 🎨 Student View Using Django Templates
- **URL to Access:** `http://127.0.0.1:8000/api/books/list`

---

## 🧪 API Testing (Using Browser & Postman)
### **1️⃣ Test in Browser (Browsable API)**
1. Open **`http://127.0.0.1:8000/api/books/`**
2. Log in with **admin credentials**.
3. Perform **GET/POST/DELETE** operations.

### **2️⃣ Test Using Postman**
- **Set `Authorization: Token your_generated_token` in Headers**
- Use **POST, GET, PUT, DELETE** requests as needed.

### **3️⃣ Debug Using Django Shell**
```sh
python manage.py shell
>>> from books.models import Book
>>> Book.objects.all()
```

## ✅ Unit Testing Using `pytest`

### **1️⃣ Install `pytest` & Django Plugin**

```sh
pip install pytest pytest-django
```

### **2️⃣ Set Up Test Database**

Before running tests, ensure the test database is created:
```sh
python create_test_db.py
```

### **3️⃣ Run Tests Correctly**
Before running tests, ensure Django is loaded properly:
```sh
pytest --ds=library_management.settings
```

### **4️⃣ Run All Tests**
```sh
pytest
```

---
