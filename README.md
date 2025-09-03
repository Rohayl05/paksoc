# Paksoc - Django Ticket Management System

## Project Structure
```
Paksoc/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── docker-compose.yml     # PostgreSQL database setup
├── .env                   # Environment variables
├── paksoc/               # Main Django project
│   ├── settings.py       # Django configuration
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI application
├── users/                # User authentication app
│   ├── models.py         # User model with roles
│   ├── views.py          # Authentication endpoints
│   ├── serializers.py    # Data validation
│   └── urls.py           # User URLs
└── events/               # Events app (future)
    └── ...
```

## Setup Instructions

1. **Create Virtual Environment**
   ```bash
   cd "c:\Users\rohay\Desktop\Comp Sci\New folder\Paksoc"
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Database**
   ```bash
   docker-compose up -d
   ```

4. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start Server**
   ```bash
   python manage.py runserver
   ```

## Available Endpoints

- `GET /hello/` - Hello world endpoint
- `GET /about/` - About page endpoint
- `POST /auth/register/` - User registration
- `POST /auth/login/` - User login
- `GET /admin/` - Django admin panel

## Next Steps

1. Test the authentication endpoints
2. Build events management system
3. Add ticket reservation functionality
