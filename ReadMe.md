# NeoFi Event Management Backend

A collaborative event management backend built with FastAPI, PostgreSQL, and SQLAlchemy. Features include JWT authentication, role-based event sharing, version control with rollback, changelog and diff comparison.

Deployment

Already Deployed on Railway : https://oblibvikramneofieventmanagement-production.up.railway.app/

---

## Features

- User registration & JWT authentication
- CRUD operations for events
- Share events with users via roles (owner/editor/viewer)
- Role-based permission checks
- Event version history & rollback functionality
- Changelog and diff between event versions
- Secure password hashing
- Interactive API docs with Swagger UI

---

## Tech Stack

- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic for validation
- Uvicorn server

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/neofi-event-backend.git
cd neofi-event-backend

--- 

### 2. Create and activate virtual environment

```bash
python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

---

### 3. Install dependencies
```bash
pip install -r requirements.txt

---

### 4. Configure environment variables
```bash
Create a .env file in the project root with the following content:

DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>
SECRET_KEY=your_jwt_secret_key
ALGORITHM=HS256

Replace placeholders with your actual database credentials and JWT secret.

---

### 5. Start the server

```bash
uvicorn app.main:app --reload

Server will run at:
http://127.0.0.1:8000
API Documentation

Visit the interactive Swagger UI:
http://127.0.0.1:8000/docs

Or ReDoc:
http://127.0.0.1:8000/redoc
Usage Examples

    Register user: POST /api/auth/register

    Login user: POST /api/auth/login

    Create event: POST /api/events/

    Share event: POST /api/events/{id}/share

    View event changelog: GET /api/events/{id}/changelog

    Rollback event version: POST /api/events/{id}/rollback/{versionId}

