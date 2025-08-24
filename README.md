# 📦 Inventory Management System

A **secure, role-based, and authenticated** Django-based **Inventory Management System**.  
This project provides a user-friendly interface for managing products, customers, and orders, with strong access control and MySQL as the backend database.  

---

## 🚀 Features
- 🔐 **Authentication & Authorization**
  - Role-based access (Admin, Staff, Customer)
  - Only authorized users can perform CRUD operations
- 📦 **Product Management**
  - Add, update, delete, and view products
  - Upload and display product images
- 👤 **Customer Management**
  - Create and manage customers
  - Link customers with their orders
- 🛒 **Order Management**
  - Place, track, and manage customer orders
  - Orders reference both customers and products
- 🗄️ **Database**
  - Uses **MySQL** for reliable data storage
- 🖥️ **User Interface**
  - Clean and responsive design with Bootstrap
  - Easy navigation and management dashboard

---

## 🛠️ Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: MySQL
- **Authentication**: Django Auth with role-based access
- **Version Control**: Git + GitHub

---

## 📌 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Sethu-333/Inventory-Management-System.git
   cd Inventory-Management-System
   ```

2. Create & activate virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure **MySQL Database** in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'django_db',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. Start development server:
   ```bash
   python manage.py runserver
   ```

---

## 📷 Screenshots (Optional)
_Add screenshots here later (e.g., Dashboard, Products page, Orders page, etc.)_

---

## 📜 License
This project is licensed under the MIT License.
