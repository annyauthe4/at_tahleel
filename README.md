# 🎓 School Portal Backend (Django)

A production-ready school portal backend built using Django and Django REST Framework.

## 📦 Features

- JWT Authentication (Students, Staff)
- Student profile management
- Course & grade tracking
- Fees & payment tracking
- Admin panel for school management
- API-ready for frontend or mobile integration

## 🚀 Technology Stack

- Python 3
- Django
- Django REST Framework
- PostgreSQL
- Gunicorn + Whitenoise (for deployment)
- Heroku/Render (for hosting)

## 🛠️ Installation

```bash
git clone https://github.com/your-username/school_portal.git
cd school_portal
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver