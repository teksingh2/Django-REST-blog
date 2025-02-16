# Blog API - Django REST Framework

This is a RESTful API for a blog application built using Django REST Framework (DRF). The API allows users to create, read, update, and delete blog posts. The API has been tested using Postman.

## Features
- User authentication (JWT)
- CRUD operations for blog posts
- Pagination, filtering, and search functionality
- API testing with Postman

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite/PostgreSQL (Database)
- Postman (API testing)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd blog-drf
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

| Method | Endpoint       | Description          |
|--------|--------------|----------------------|
| GET    | /api/home/  | List all posts      |
| POST   | /api/home/  | Create a new post   |
| GET    | /api/home/{id}/ | Retrieve a post  |
| PUT    | /api/home/{id}/ | Update a post    |
| DELETE | /api/home/{id}/ | Delete a post    |

## API Testing with Postman
1. Open Postman and import the API endpoints.
2. Use authentication tokens if required.
3. Test CRUD operations.
4. Verify responses and error handling.

## License
This project is open-source and available under the MIT License.

