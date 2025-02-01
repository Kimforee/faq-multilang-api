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

---

### Check Code Quality with flake8**  
Run `flake8` to check for PEP8 compliance:  
```bash
flake8 faqs/views.py
```

### Prerequisites
- Python 3.11+
- PostgreSQL or SQLite (default)
- Redis (for caching)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/django-multilingual-faq.git
   cd django-multilingual-faq
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the server:
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

## Running Tests
```bash
pytest
```

## Code Quality Check
```bash
flake8 faqs/
```

## Git Best Practices
Use conventional commit messages:
- `feat: Add FAQ translation`
- `fix: Improve caching mechanism`
- `docs: Update API documentation`

---
