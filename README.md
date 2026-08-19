# CRM - Enterprise CRM System

A modern full-stack Enterprise CRM (Customer Relationship Management) system built with **Django**, **React**, and **TypeScript**.

This project is being developed as a portfolio project to demonstrate modern full-stack development practices, scalable architecture, REST API design, authentication, and production-ready development workflow.

---

## Features

- Authentication with JWT
- Role-Based Access Control (RBAC)
- Customer Management
- Company Management
- Contact Management
- Dashboard with business metrics
- Search, filtering, and pagination
- Responsive UI
- Form validation
- API integration
- Background task processing with Celery
- Production-ready project structure

---

# Tech Stack

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- shadcn/ui (Radix UI + Nova preset)
- React Router
- Axios
- React Hook Form
- Zod
- TanStack Query
- TanStack Table v8
- Lucide React
- Sonner
- React Context API

### Frontend Architecture

- Feature-Based Folder Structure
- Reusable UI Components
- Custom Hooks
- API Layer
- Protected Routes
- Error Boundaries

---

## Backend

- Django
- Django REST Framework (DRF)
- PostgreSQL
- JWT Authentication
- Role-Based Access Control (RBAC)
- Celery
- Redis

### Backend Architecture

- RESTful API
- Service Layer
- Modular Django Apps
- Custom Permissions
- Pagination
- Filtering
- Validation
- Background Tasks

---

## DevOps & Tooling

- Git
- npm
- ESLint
- Prettier

---

# Project Structure

```
crm/
│
├── backend/
│
└── frontend/
```

---

# Getting Started

## Clone the repository

```bash
git clone https://github.com/flat07/crm.git
cd crm
```

---

# Backend Setup

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create your environment file.

```bash
cp .env.example .env.development
```

Run migrations.

```bash
python manage.py migrate
```

Create a superuser.

```bash
python manage.py createsuperuser
```

Start the development server.

```bash
python manage.py runserver
```

---

# Frontend Setup

Navigate to the frontend directory.

```bash
cd frontend
```

Install dependencies.

```bash
npm install
```

Start the development server.

```bash
npm run dev
```

---

# Background Workers

Start Redis.

```bash
redis-server
```

Run Celery worker.

```bash
celery -A config worker -l info
```

---

# Code Quality

Run ESLint.

```bash
npm run lint
```

Format code.

```bash
npm run format
```

---

# Roadmap

- [ ] Authentication
- [ ] User Management
- [ ] Customer Management
- [ ] Company Management
- [ ] Contact Management
- [ ] Activity Timeline
- [ ] Notes
- [ ] Tasks
- [ ] Dashboard Analytics
- [ ] Email Integration
- [ ] Notifications
- [ ] File Uploads
- [ ] Audit Logs
- [ ] Docker Deployment
- [ ] CI/CD Pipeline
- [ ] Automated Testing

---

# Learning Goals

This project focuses on learning and demonstrating:

- Full-stack application architecture
- REST API development
- React best practices
- Django best practices
- Authentication & Authorization
- State management
- API integration
- Form handling
- Database design
- Background processing
- Clean project architecture
- Production-ready development workflow

---

# License

This project is for educational and portfolio purposes.
