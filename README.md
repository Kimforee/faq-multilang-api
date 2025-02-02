# faq-multilang-api
 This project is a Django-based FAQ system with multilingual support using Google Translate and caching with Redis.

## Features
- Store and manage FAQs with automatic translations (English, Hindi, Bengali).
- WYSIWYG editor support (`django-ckeditor`).
- REST API with language selection via `?lang=` query parameter.
- Caching with Redis for optimized performance.
- Unit testing with `pytest`.
- PEP8 compliance using `flake8`.

Testing : ![image](https://github.com/user-attachments/assets/d5a3dee4-77a4-4339-be68-acf8a1960c58)
Home page : 
![image](https://github.com/user-attachments/assets/a83d7b54-74a2-423e-84d6-ae0e79093947)
Admin :
![image](https://github.com/user-attachments/assets/580034c5-bfa9-4863-8e65-99d9d73f77e2)
---

### Prerequisites
- Python 3.10+
- PostgreSQL or SQLite (default)
- Redis (for caching)

### Docker Build
```bash
docker-compose up --build
```
#### **Admin Panel**  

#### **Automated Superuser Credentials**
Automated superuser is created if docker is used, use the following credentials:  
**Username:** `123`  
**Password:** `123`  
Access Django Admin:  
```bash
http://127.0.0.1:8000/admin/
```
create a new superuser using:  
```bash
python manage.py createsuperuser
```
---

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Kimforee/faq-multilang-api.git
   cd faq-multilang-api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/scripts/activate  # On Windows: venv\Scripts\activate
   ```

3. Ensure Redis is installed and running locally:
   ```bash
   redis-server
   ```
4. Update settings.py to use local Redis:
   ```bash
   CACHES = {
       "default": {
           "BACKEND": "django_redis.cache.RedisCache",
           "LOCATION": "redis://localhost:6379/1",
           "OPTIONS": {
               "CLIENT_CLASS": "django_redis.client.DefaultClient",
           }
       }
   }
   ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Run the server:
   ```bash
   python manage.py runserver
   ```

## API Usage

### Fetch all FAQs (English)
```bash
curl http://127.0.0.1:8000/api/faqs/
```

### Fetch FAQs in Hindi
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=hi
```

### Fetch FAQs in Bengali
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=bn
```

## Running Tests (works with local setup only)
```bash
pytest
```

## Code Quality Check
```bash
flake8 faqs/
```
