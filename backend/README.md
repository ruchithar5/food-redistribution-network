# 🍱 Smart Food Redistribution Network (SFRN)

> An AI-powered web platform designed to reduce food waste by connecting food donors with NGOs and volunteers for efficient redistribution.

[![Django Version](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [User Roles](#-user-roles)
- [Implemented Modules](#-implemented-modules)
- [API Endpoints](#-api-endpoints)
- [Future Enhancements](#-future-enhancements)
- [Common Errors & Fixes](#-common-errors--fixes)
- [Testing](#-testing)
- [Contribution Guidelines](#-contribution-guidelines)
- [License](#-license)
- [Author](#-author)
- [Project Vision](#-project-vision)
- [Support](#-support)

---

## 🎯 Project Overview

The **Smart Food Redistribution Network (SFRN)** is a full-stack Django-based application that aims to:

| Objective | Description |
|-----------|-------------|
| 🍽️ **Reduce Food Wastage** | Minimize food waste by connecting surplus food with those in need |
| 🤝 **Connect Stakeholders** | Bridge the gap between donors, NGOs, and volunteers |
| 🧠 **Smart Optimization** | Leverage AI for matching, routing, and expiry prediction |
| 📊 **Real-time Analytics** | Provide insights on impact metrics and sustainability |

### Problem Statement

Every year, millions of tons of edible food go to waste while millions go hungry. SFRN bridges this gap using **Artificial Intelligence** and **Smart Logistics**.

### Solution

A unified platform where:
- **Donors** post surplus food
- **AI** intelligently matches with nearest NGOs
- **Volunteers** optimize pickup/delivery routes
- **Impact** is tracked in real-time

---

## 🌟 Key Features

### 🧠 Core AI Features
| Feature | Description | Status |
|---------|-------------|--------|
| **AI Smart Matching** | Automatically matches donors with nearest NGOs using priority-based AI scoring | ✅ Implemented |
| **Food Expiry Prediction** | Predicts spoilage time using ML models to prioritize urgent donations | ✅ Implemented |
| **Smart Route Optimization** | AI-powered volunteer routing for efficient pickups and deliveries | ✅ Implemented |
| **Demand Forecasting** | Predicts food demand in different areas | 🔄 In Progress |

### 👥 Role-Based Dashboards
| Dashboard | Features |
|-----------|----------|
| **Donor Dashboard** | Post donations, track status, view impact metrics, AI matching score |
| **NGO Dashboard** | View available food, accept donations, request supplies, manage pickups |
| **Volunteer Dashboard** | View assigned routes, track deliveries, earn rewards, delivery history |
| **Admin Dashboard** | System overview, user management, analytics, blockchain logs |

### 🔗 Additional Features
- 🔗 **Blockchain Tracking** (Concept) - Transparent, tamper-proof donation tracking
- 🌱 **Sustainability Dashboard** - CO₂ savings, meals served, impact metrics
- ⭐ **Trust & Reputation System** - Rating system for donors, NGOs, and volunteers
- 🚨 **Emergency Food Requests** - SOS-based real-time dispatch
- 🤖 **AI Chatbot Assistant** - 24/7 support for all users

---

## 🏗️ Tech Stack

### Backend
| Technology | Purpose |
|------------|---------|
| **Python 3.10+** | Core programming language |
| **Django 5.0** | Web framework |
| **SQLite** | Database (upgradable to PostgreSQL) |
| **Django REST Framework** | API development (planned) |

### Frontend
| Technology | Purpose |
|------------|---------|
| **HTML5** | Structure |
| **CSS3** | Styling |
| **Bootstrap 5** | Responsive UI framework |
| **JavaScript** | Interactivity |
| **Font Awesome** | Icons |

### Tools & DevOps
| Tool | Purpose |
|------|---------|
| **Git & GitHub** | Version control |
| **VS Code** | IDE |
| **Pillow** | Image processing |
| **Django Debug Toolbar** | Debugging |

---

## 📂 Project Structure
food-redistribution-network/│├── backend/ # Django project root│ ├── core/ # Main application│ │ ├── migrations/ # Database migrations│ │ ├── templates/ # HTML templates│ │ │ └── core/│ │ │ ├── home.html│ │ │ ├── login.html│ │ │ ├── register.html│ │ │ ├── dashboard\_donor.html│ │ │ ├── dashboard\_ngo.html│ │ │ ├── dashboard\_volunteer.html│ │ │ └── dashboard\_admin.html│ │ ├── static/ # CSS, JS, images│ │ ├── **init**.py│ │ ├── admin.py # Admin panel config│ │ ├── apps.py # App config│ │ ├── models.py # Database models│ │ ├── views.py # View controllers│ │ ├── urls.py # URL routing│ │ ├── forms.py # Django forms│ │ └── helpers.py # Utility functions│ ││ ├── food redistribution/ # Project settings│ │ ├── **init**.py│ │ ├── settings.py # Django settings│ │ ├── urls.py # Main URL config│ │ └── wsgi.py # WSGI config│ ││ ├── db.sqlite3 # SQLite database│ ├── manage.py # Django management script│ └── requirements.txt # Python dependencies│├── venv/ # Virtual environment├── .gitignore # Git ignore rules└── README.md # Project documentation

text

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ---  ## ⚙️ Installation & Setup  ### Prerequisites  - Python 3.10 or higher  - pip (Python package manager)  - Git (optional)  ### 🔹 Step 1: Clone the Repository  ```bash  # Using HTTPS  git clone https://github.com/your-username/food-redistribution-network.git  # Or using SSH  git clone git@github.com:your-username/food-redistribution-network.git  # Navigate to project directory  cd food-redistribution-network/backend   `

### 🔹 Step 2: Create Virtual Environment

bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # Windows  python -m venv venv  venv\Scripts\activate  # macOS/Linux  python3 -m venv venv  source venv/bin/activate   `

### 🔹 Step 3: Install Dependencies

bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # If requirements.txt exists  pip install -r requirements.txt  # If requirements.txt is not available  pip install django pillow   `

### 🔹 Step 4: Run Migrations

bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python manage.py makemigrations  python manage.py migrate   `

### 🔹 Step 5: Create Superuser (Admin Access)

bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python manage.py createsuperuser  # Follow prompts to set username, email, and password   `

### 🔹 Step 6: Run Development Server

bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python manage.py runserver   `

### 🔹 Step 7: Access the Application

Open your browser and navigate to:

*   **Main App:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    
*   **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
    

👥 User Roles
-------------

RoleIconAccess LevelKey Actions**Donor**🍽️Post donationsAdd food, track status, view impact**NGO**🤝Accept donationsView available food, request supplies, manage pickups**Volunteer**🚚Deliver foodView routes, complete deliveries, earn rewards**Admin**⚙️Full system controlUser management, analytics, system health

### Role-Based Redirect Flow

text

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Register → Login → Dashboard Router → Role-specific Dashboard  Donor     → /dashboard/donor/  NGO       → /dashboard/ngo/  Volunteer → /dashboard/volunteer/  Admin     → /dashboard/admin/   `

📊 Implemented Modules
----------------------

ModuleStatusDescription✅ **User Authentication**CompleteLogin, Register, Session management✅ **Role-Based Access**CompleteDonor/NGO/Volunteer/Admin separation✅ **Donation Management**CompletePost, view, edit, delete donations✅ **NGO Dashboard**CompleteView matched donations, accept food✅ **Volunteer Dashboard**CompleteAssigned routes, delivery tracking✅ **Admin Panel**CompleteUser management, system overview✅ **Food Request System**CompleteNGOs can request specific food items✅ **AI Matching Logic**CompletePriority-based donor-NGO matching🔄 **Route Optimization**In ProgressGoogle Maps API integration🔄 **Real-time Notifications**In ProgressEmail/SMS alerts📅 **Expiry Prediction**PlannedML model integration

🔗 API Endpoints (Planned)
--------------------------

EndpointMethodDescriptionAuth Required/api/donations/GETList all donations✅/api/donations/POSTCreate new donation✅ (Donor)/api/donations/{id}/GETGet donation details✅/api/donations/{id}/accept/POSTNGO accepts donation✅ (NGO)/api/pickups/GETList pickups✅/api/pickups/{id}/complete/POSTComplete pickup✅ (Volunteer)/api/requests/GET/POSTFood requests✅ (NGO)/api/stats/GETPlatform statistics✅

🔮 Future Enhancements
----------------------

### Phase 2: AI Integration

*   🤖 **Real ML Model Integration** - TensorFlow/PyTorch for expiry prediction
    
*   📍 **Google Maps Live Tracking** - Real-time volunteer location tracking
    
*   🧠 **Advanced Matching Algorithm** - Deep learning for donor-NGO matching
    

### Phase 3: Mobile & Notifications

*   📱 **Mobile Application** - Flutter/React Native cross-platform app
    
*   🔔 **Real-time Notifications** - WebSocket + Firebase Cloud Messaging
    
*   📧 **Email/SMS Alerts** - Automated reminders and updates
    

### Phase 4: Advanced Features

*   🔗 **Blockchain Integration** - Ethereum smart contracts for transparency
    
*   📊 **Advanced Analytics** - Power BI/Django Charts dashboard
    
*   🌍 **Multi-language Support** - i18n integration
    
*   💳 **Payment Gateway** - For donation incentives (Razorpay/Stripe)
    

🧪 Testing
----------

### Run Basic Checks

bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # Check for common issues  python manage.py check  # Run Django tests (if implemented)  python manage.py test   `

### Manual Testing Checklist

Test CaseExpected ResultUser RegistrationAccount created, redirect to dashboardUser LoginSuccessful authentication, role-based redirectDonor posts foodDonation appears in NGO dashboardNGO accepts donationStatus updates, volunteer notifiedVolunteer completes deliveryImpact metrics update

🐞 Common Errors & Fixes
------------------------

ErrorSolutionModuleNotFoundError: No module named 'django'Run pip install djangoModuleNotFoundError: No module named 'PIL'Run pip install pillowdjango.db.utils.OperationalError: no such tableRun python manage.py migrateImportError: cannot import name 'xxx'Check file structure and importsTemplateDoesNotExistVerify template path in settings.pyCSRF verification failedAdd {% csrf\_token %} to forms

### Settings Configuration

Ensure INSTALLED\_APPS in settings.py includes:

python

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   INSTALLED_APPS = [      'django.contrib.admin',      'django.contrib.auth',      'django.contrib.contenttypes',      'django.contrib.sessions',      'django.contrib.messages',      'django.contrib.staticfiles',      'core',  # Your main app  ]   `

🤝 Contribution Guidelines
--------------------------

We welcome contributions! Follow these steps:

### Step 1: Fork the Repository

Click the **Fork** button on GitHub

### Step 2: Clone Your Fork

bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone https://github.com/your-username/food-redistribution-network.git  cd food-redistribution-network   `

### Step 3: Create a Feature Branch

bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git checkout -b feature/amazing-feature   `

### Step 4: Make Changes & Commit

bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git add .  git commit -m "Add: amazing feature description"   `

### Step 5: Push to GitHub

bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git push origin feature/amazing-feature   `

### Step 6: Create Pull Request

Go to GitHub and create a Pull Request from your branch

### Coding Standards

*   Follow PEP 8 for Python code
    
*   Use meaningful variable names
    
*   Add comments for complex logic
    
*   Write docstrings for functions
    

📜 License
----------

This project is licensed under the **MIT License** - see below:

text

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   MIT License  Copyright (c) 2024 Ruchitha Reddy  Permission is hereby granted, free of charge, to any person obtaining a copy  of this software and associated documentation files (the "Software"), to deal  in the Software without restriction, including without limitation the rights  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  copies of the Software, and to permit persons to whom the Software is  furnished to do so, subject to the following conditions...  Full license text: https://opensource.org/licenses/MIT   `

> **Note:** This project is developed for **educational purposes** as a Final Year Engineering Project.

👩‍💻 Author
------------

**Ruchitha Reddy**

*   🎓 Final Year Engineering Student
    
*   📧 Email: \[your-email@example.com\]
    
*   🔗 LinkedIn: \[[linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)\]
    
*   🐙 GitHub: \[[github.com/your-username](https://github.com/your-username)\]
    

### Project Supervisor

*   \[Supervisor Name\] - \[Designation\]
    
*   \[College/University Name\]
    

🙏 Acknowledgments
------------------

*   **Django Documentation** - For excellent framework documentation
    
*   **Bootstrap Team** - For responsive UI components
    
*   **Font Awesome** - For beautiful icons
    
*   **Open Source Community** - For invaluable resources
    

💡 Project Vision
-----------------

> _"To build a smarter and sustainable ecosystem where no food goes to waste and everyone has access to it."_

### Impact Goals

*   🎯 Reduce food waste by 30% in pilot areas
    
*   🎯 Connect 100+ NGOs within first year
    
*   🎯 Serve 1M+ meals annually
    
*   🎯 Reduce CO₂ emissions by 500 tons
    

📞 Contact & Support
--------------------

For questions, suggestions, or collaboration:

*   **Open an Issue** on GitHub
    
*   **Email:** \[your-email@example.com\]
    
*   **LinkedIn:** \[Your Profile\]
    

⭐ Support the Project
---------------------

If you find this project useful:

ActionHow to⭐ **Star**Click the star button on GitHub🍴 **Fork**Fork the repository for your own use📢 **Share**Share with friends and colleagues🐛 **Report Issues**Open GitHub issues for bugs💻 **Contribute**Submit pull requests

📊 Project Status
-----------------

text

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   🟢 ACTIVE - Under Active Development   `

MilestoneStatusCompletionRequirements Analysis✅100%UI/UX Design✅100%Backend Development✅90%Frontend Integration✅85%AI Features🔄60%Testing & Debugging🔄70%Documentation🔄80%Deployment⏳0%

🖼️ Screenshots
---------------

> _\[Add screenshots of your application here\]_

### Home Page

[https://screenshots/home.png](https://screenshots/home.png)

### Donor Dashboard

[https://screenshots/donor-dashboard.png](https://screenshots/donor-dashboard.png)

### NGO Dashboard

[https://screenshots/ngo-dashboard.png](https://screenshots/ngo-dashboard.png)

### Volunteer Dashboard

[https://screenshots/volunteer-dashboard.png](https://screenshots/volunteer-dashboard.png)

🔗 Useful Links
---------------

*   [Django Documentation](https://docs.djangoproject.com/)
    
*   [Bootstrap Documentation](https://getbootstrap.com/docs/)
    
*   [Python Documentation](https://docs.python.org/3/)
    
*   [GitHub Guides](https://guides.github.com/)
    

**Built with ❤️ for a Zero Hunger Future**

_© 2024 Smart Food Redistribution Network | All Rights Reserved_

\`\`\`

How to Use
----------

1.  **Copy** the entire code block above
    
2.  **Paste** into a file named README.md
    
3.  **Save** the file in your project's root directory
    
4.  **Customize** the following sections with your actual details:
    
    *   Your email address
        
    *   GitHub username
        
    *   LinkedIn profile
        
    *   College/University name
        
    *   Supervisor name
        
    *   Add actual screenshots
        

What Makes This README Professional
-----------------------------------

FeatureBenefit✅ Table of ContentsEasy navigation✅ BadgesVisual status indicators✅ Emojis & IconsVisual appeal✅ Code blocksProper formatting✅ TablesOrganized information✅ Step-by-step guidesClear instructions✅ Error handlingTroubleshooting help✅ Contribution guideOpen source ready✅ Project statusTransparency✅ Future roadmapShows vision

Want me to add **screenshots placeholders**, **API documentation**, or **deployment instructions** (Heroku/AWS/Railway)?

_This response is AI-generated, for reference only._