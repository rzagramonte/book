# 📚 Book

Book is a full-stack reading community platform that matches users into archetype-based groups, assigns curated books, and supports real-time discussion with optional AI-assisted literary analysis.

This project emphasizes production-oriented architecture, domain-layer separation, CI validation, and structured development workflows.

![landing page of Book](https://u.cubeupload.com/rzagramonte/Screenshot20250609at.png)

---

## 🚀 Core Features

- Archetype-based quiz and ranking system
- Automatic group formation (max 6 users per group)
- Multi-group membership support
- Structured book lifecycle (current vs completed)
- Real-time group chat (WebSockets)
- User-invoked AI literary analysis
- Cloud-based media storage (Cloudinary)

---

## 🏗 Architecture

### Backend
- Python
- Django
- PostgreSQL
- Django ORM
- Django Channels (WebSockets)
- Service-layer domain logic (e.g., `book_assignment.py`)

### Frontend
- React
- Tailwind CSS
- Component-based architecture

### AI Integration
- Hugging Face API

### Infrastructure
- GitHub Actions (CI)
- Branch-protected `main` workflow

---

## 🖥 Local Development

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL

---

## ⚡ Quickstart

```bash
# Clone repository
git clone https://github.com/<your-username>/book.git
cd book

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

Backend: http://127.0.0.1:8000  
Frontend: http://localhost:5173  

---

## 🔐 Configuration

Create a `.env` file in `/backend` using `.env.example`.

Required variables:

```
SECRET_KEY=
DEBUG=True

POSTGRESQL_NAME=
POSTGRESQL_USER=
POSTGRESQL_PASSWORD=
POSTGRESQL_HOST=localhost
POSTGRESQL_PORT=5432

CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=

HF_API_KEY=
```

These values are loaded in Django via environment variables. Do not commit secrets.

---

## 🧪 Development Commands

### Backend (run from `backend/`)

```bash
# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Lint
ruff check .

# Format
black .
```

### Frontend (run from `frontend/`)

```bash
# Start dev server
npm run dev

# Lint
npm run lint

# Build
npm run build
```

---

## 🔄 Development Workflow

1. Create a feature branch
2. Open a Pull Request
3. CI runs validation checks
4. Merge into protected `main` branch

All changes must pass CI before merging.

---

## 📌 Project Status

MVP in active development.
