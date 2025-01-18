# Register-Login Application

This is a Django REST Framework-based application that allows users to sign up and log in as either a **Patient** or a **Doctor**. Upon logging in, users are redirected to their respective dashboards displaying their profile details.

## Features

- **User Types**: 
  - Patient
  - Doctor
- **Signup Form**:
  - Fields: First Name, Last Name, Profile Picture, Username, Email, Password, Confirm Password, Address (Line 1, City, State, Pincode), User Type.
  - Validates if Password and Confirm Password match.
- **Login**:
  - Validates user credentials.
  - Redirects users to their specific dashboards after successful login.
- **Dashboard**:
  - Displays the profile details entered during signup.

## Installation

### Prerequisites
- Python 3.12+
- Django 5.1+
- Virtual Environment (Recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Arpreetkhare/register-login.git
   cd USER_MANAGEMENT
2. **create virtual env**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
3. **install dependencies:**
   ```bash
   pip install -r requirements.txt


4. **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **run server:**    
    ```bash
    python manage.py runserver

6.**Access the application at:**
  ```bash
  http://127.0.0.1:8000





