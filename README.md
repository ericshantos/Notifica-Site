[🇧🇷] [Lê em português](README.pt.md)

# Portfolio Tracker API

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.1.1-green.svg)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)

API for tracking portfolio visits with automated daily email reports.

## 📋 Prerequisites

- Python 3.9+
- Gmail account with "App Passwords" configured (see below)
- Dependencies listed in `requirements.txt`

## 🔐 Gmail Configuration

To send emails through Gmail, you'll need to set up an "App Password":

1. Access your [Google Account](https://myaccount.google.com/)
2. Go to "Security" → "App Passwords"
3. Select "App" as `Mail` and "Device" as `Other (Custom Name)`
4. Click "Generate" and copy the generated password
5. Use this password instead of your regular password in the `.env` file

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ericshantos/VisitTracker_API.git
   cd VisitTracker_API
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your credentials:
   ```ini
   EMAIL_ADDRESS=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   ```

5. Run the application:
   ```bash
   python run.py
   ```

## 🏗 Architecture

The API follows a modular structure with clear separation of concerns:

```
app/
├── controllers/    # Request handling logic
├── models/         # Data models and schemas
├── routers/        # Route definitions and endpoints
├── services/       # Business logic and services
├── utils/          # Helper utilities and tools
└── views/          # Response rendering and templates
```

Key components:

1. **Visit Tracking**:
   - `VisitTracker` records each endpoint access
   - Stores total count and access timestamps

2. **Report Scheduling**:
   - `ReportScheduler` sends daily reports at configurable time
   - Uses threads to operate in background

3. **Email Delivery**:
   - `EmailSender` provides SMTP interface
   - `EmailReporter` generates formatted HTML reports

4. **REST API**:
   - Routes defined via `Router` (Flask Blueprints wrapper)
   - Standardized responses with `StandardResponse`

## 🛠 Development Tools

- **Formatting**: Black and isort for consistent code style
- **Linting**: Flake8 for code quality checks
- **Type Checking**: Mypy for static type verification
- **Security**: Bandit for vulnerability analysis
- **Pre-commit**: Automated hooks before each commit

To set up pre-commit hooks:
```bash
pre-commit install
```

## 📬 Endpoints

- `GET /` - Main endpoint that tracks visits and returns welcome message

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
