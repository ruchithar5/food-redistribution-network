# 🍱 Smart Food Redistribution Network (SFRN)

[![Django Version](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

> An AI-powered web platform that reduces food waste by connecting donors, NGOs, and volunteers for efficient food redistribution to people in need.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [User Roles](#-user-roles)
- [Dashboard Features](#-dashboard-features)
- [API Endpoints](#-api-endpoints)
- [Future Enhancements](#-future-enhancements)
- [Screenshots](#-screenshots)
- [Common Errors & Fixes](#-common-errors--fixes)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Support](#-support)

---

## 🎯 Project Overview

The **Smart Food Redistribution Network (SFRN)** is a full-stack Django application that bridges the gap between food surplus and hunger. It uses **Artificial Intelligence** to match donors with NGOs, predict food expiry, optimize delivery routes, and track impact in real-time.

### Problem Statement

Every year, millions of tons of edible food go to waste while millions go hungry. SFRN solves this by creating a smart ecosystem where:

- **Donors** can post surplus food
- **NGOs** can request and receive food
- **Volunteers** can report needy people and deliver food
- **Admins** can verify reports and manage the platform

---

## 🌟 Key Features

### 🧠 AI-Powered Features

| Feature | Description | Status |
|---------|-------------|--------|
| **Smart NGO Matching** | AI algorithm matches donors with nearest NGOs | ✅ |
| **Food Expiry Prediction** | Predicts spoilage time using ML models | ✅ |
| **AI Food Quality Score** | Image-based quality verification | ✅ |
| **Route Optimization** | Smart delivery route planning | 🔄 |
| **Demand Forecasting** | Predicts food demand in areas | 📅 |

### 👥 Role-Based Dashboards

| Role | Features |
|------|----------|
| **Donor** | Post donations, track status, AI matching, blockchain tracking |
| **NGO** | View available food, accept donations, request supplies, rate donors |
| **Volunteer** | Report needy people, claim tasks, deliver food, upload proof |
| **Admin** | Verify reports, manage users, system analytics, blockchain ledger |

### 🔗 Unique Features

- 📸 **Photo/Video Evidence** - Volunteers upload proof of needy people
- ✅ **Admin Verification** - Prevents fake reports
- 🔗 **Blockchain Tracking** - Transparent donation records
- 🌿 **Carbon Footprint** - Track CO₂ savings
- ⭐ **Trust Score System** - Gamification for reliable users
- 🚨 **Emergency Alerts** - Real-time notifications for urgent cases

---

## 🏗️ Tech Stack

### Backend

| Technology | Purpose |
|------------|---------|
| Python 3.10+ | Core programming language |
| Django 5.0 | Web framework |
| SQLite | Database (upgradable to PostgreSQL) |
| Django REST Framework | API development |

### Frontend

| Technology | Purpose |
|------------|---------|
| HTML5 | Structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive UI |
| JavaScript | Interactivity |
| Chart.js | Analytics charts |
| Leaflet/Google Maps | Location tracking |

### Tools & DevOps

| Tool | Purpose |
|------|---------|
| Git & GitHub | Version control |
| Pillow | Image processing |
| Font Awesome | Icons |

---

## 📂 Project Structure

food-redistribution-network/
│
├── backend/
│ ├── core/
│ │ ├── migrations/
│ │ ├── templates/
│ │ │ └── core/
│ │ │ ├── home.html
│ │ │ ├── login.html
│ │ │ ├── register.html
│ │ │ ├── dashboard_donor.html
│ │ │ ├── dashboard_ngo.html
│ │ │ ├── dashboard_volunteer.html
│ │ │ └── dashboard_admin.html
│ │ ├── static/
│ │ ├── admin.py
│ │ ├── apps.py
│ │ ├── models.py
│ │ ├── views.py
│ │ ├── urls.py
│ │ ├── forms.py
│ │ └── helpers.py
│ │
│ ├── food_redistribution/
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ │
│ ├── db.sqlite3
│ ├── manage.py
│ └── requirements.txt
│
├── venv/
├── .gitignore
└── README.md


---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.10 or higher
- pip package manager
- Git (optional)

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/food-redistribution-network.git
cd food-redistribution-network/backend

# 🍱 Food Redistribution Network

An AI-powered food donation and redistribution platform built using the Django framework.  
This system helps reduce food wastage by connecting food donors, NGOs, volunteers, and administrators efficiently.

---

# 📂 Project Structure

```text
food-redistribution-network/
│
├── backend/
│   ├── core/
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── core/
│   │   │       ├── home.html
│   │   │       ├── login.html
│   │   │       ├── register.html
│   │   │       ├── dashboard_donor.html
│   │   │       ├── dashboard_ngo.html
│   │   │       ├── dashboard_volunteer.html
│   │   │       └── dashboard_admin.html
│   │   │
│   │   ├── static/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── helpers.py
│   │
│   ├── food_redistribution/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── db.sqlite3
│   ├── manage.py
│   └── requirements.txt
│
├── venv/
├── .gitignore
└── README.md
```

---

# ⚙️ Installation & Setup

## ✅ Prerequisites

- Python 3.10 or higher
- pip package manager
- Git (optional)

---

## 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/food-redistribution-network.git

cd food-redistribution-network/backend
```

---

## 🔹 Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 🔹 Step 3: Install Dependencies

```bash
pip install django pillow
```

---

## 🔹 Step 4: Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## 🔹 Step 5: Create Superuser (Admin Access)

```bash
python manage.py createsuperuser
```

---

## 🔹 Step 6: Run Development Server

```bash
python manage.py runserver
```

---

## 🔹 Step 7: Access the Application

- Main App:  
  `http://127.0.0.1:8000/`

- Admin Panel:  
  `http://127.0.0.1:8000/admin/`

---

# 👥 User Roles

| Role | Icon | Access Level | Key Actions |
|------|------|------|------|
| Donor | 🍽️ | Post donations | Add food, track status, view impact |
| NGO | 🤝 | Accept donations | View food, request supplies, rate donors |
| Volunteer | 🚚 | Report & Deliver | Find needy, upload proof, deliver food |
| Admin | 👑 | Full control | Verify reports, manage users, analytics |

---

# 🔄 Role-Based Redirect Flow

```text
Register → Login → Dashboard Router → Role-specific Dashboard

Donor     → /dashboard/donor/
NGO       → /dashboard/ngo/
Volunteer → /dashboard/volunteer/
Admin     → /dashboard/admin/
```

---

# 📊 Dashboard Features

## 🍽️ Donor Dashboard

| Feature | Description |
|------|------|
| Post Donation | Add food with image, quantity, expiry |
| AI Match Score | See best NGO match percentage |
| Donation History | Track status of all donations |
| Impact Metrics | Food saved, CO₂ reduced, meals served |
| Blockchain Record | View donation transaction hash |
| Live Tracking | Track volunteer delivering your food |

---

## 🤝 NGO Dashboard

| Feature | Description |
|------|------|
| Available Food | View AI-matched donations nearby |
| Accept Donations | Claim food for beneficiaries |
| Request Food | Post specific food requirements |
| Rate Donors | Provide feedback to donors |
| Volunteer Management | Assign volunteers for pickup |
| Impact Analytics | Track food received and distributed |

---

## 🚚 Volunteer Dashboard

| Feature | Description |
|------|------|
| Report Needy | Upload photos/videos of people in need |
| Claim Tasks | Take on reports from other volunteers |
| Today's Route | AI-optimized delivery path |
| Live Navigation | Real-time turn-by-turn directions |
| Delivery Proof | Upload photos after delivery |
| Earnings Tracker | Track incentives and rewards |

---

## 👑 Admin Dashboard

| Feature | Description |
|------|------|
| Verify Reports | Approve/reject volunteer reports |
| User Management | Manage donors, NGOs, volunteers |
| System Analytics | Platform-wide statistics |
| AI Health Monitor | Check matching engine status |
| Blockchain Ledger | View all transactions |
| Report Export | Generate CSV/PDF reports |

---

# 🔗 API Endpoints (Planned)

| Endpoint | Method | Description | Auth |
|------|------|------|------|
| /api/donations/ | GET | List all donations | ✅ |
| /api/donations/ | POST | Create new donation | Donor |
| /api/donations/{id}/accept/ | POST | Accept donation | NGO |
| /api/reports/ | GET/POST | Needy person reports | Volunteer |
| /api/reports/{id}/verify/ | POST | Verify report | Admin |
| /api/pickups/ | GET | List pickups | ✅ |
| /api/stats/ | GET | Platform statistics | Admin |

---

# 🔮 Future Enhancements

## 🤖 Phase 2: AI Integration

- Real ML Models using TensorFlow
- Live tracking with Google Maps
- Deep Learning NGO Matching

---

## 📱 Phase 3: Mobile & Notifications

- Flutter / React Native App
- Real-time notifications
- Email & SMS integration

---

## 🔗 Phase 4: Advanced Features

- Ethereum Blockchain
- Power BI Analytics
- Razorpay / Stripe Integration

---

# 📸 Screenshots

## 🏠 Home Page

Add screenshot here later.

---

## 🍽️ Donor Dashboard

Add screenshot here later.

---

## 🤝 NGO Dashboard

Add screenshot here later.

---

## 🚚 Volunteer Dashboard

Add screenshot here later.

---

## 👑 Admin Panel

Add screenshot here later.

---

# 🐞 Common Errors & Fixes

| Error | Solution |
|------|------|
| No module named 'django' | Run `pip install django` |
| No module named 'PIL' | Run `pip install pillow` |
| no such table | Run `python manage.py migrate` |
| TemplateDoesNotExist | Check template path in settings.py |
| CSRF verification failed | Add `{% csrf_token %}` to forms |

---

# ⚙️ Django Settings Configuration

Ensure `INSTALLED_APPS` in `settings.py` includes:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
]
```

---

# 🤝 Contributing

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/amazing-feature
```

3. Commit changes

```bash
git commit -m "Add amazing feature"
```

4. Push to branch

```bash
git push origin feature/amazing-feature
```

5. Open Pull Request

---

# 🧹 Coding Standards

- Follow PEP 8
- Use meaningful variable names
- Add comments for complex logic
- Write docstrings for functions

---

# 📜 License

This project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2026 Ruchitha Reddy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

Full license:  
https://opensource.org/licenses/MIT

---

# 👩‍💻 Author

## Ruchitha Reddy

- 🎓 Final Year Engineering Student
- 🐙 GitHub: https://github.com/your-username
- 🔗 LinkedIn: https://linkedin.com/in/your-profile

---

# 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team
- Font Awesome
- Open Source Community

---

# 💡 Project Vision

> “To build a smarter and sustainable ecosystem where no food goes to waste and everyone has access to it.”

---

# 🎯 Impact Goals

- Reduce food waste by 30%
- Connect 100+ NGOs
- Serve 1M+ meals annually
- Reduce CO₂ emissions