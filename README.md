# 📱 WhatsApp Product Review Collector

A full-stack application that collects product reviews via WhatsApp conversations, stores them in a PostgreSQL database, and displays them through a modern React interface.

![Project Demo](https://img.shields.io/badge/Status-Production%20Ready-success)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![React](https://img.shields.io/badge/React-18.2-61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-009688)

---

## 🎯 Project Overview

This application enables businesses to collect structured product reviews through WhatsApp, making it easy for customers to share feedback through a familiar messaging interface.

### Key Features

- 🤖 **Conversational Interface**: Natural conversation flow via WhatsApp
- 💾 **Persistent Storage**: All reviews stored in PostgreSQL database
- 📊 **Real-time Dashboard**: React frontend displays reviews instantly
- 🔄 **RESTful API**: Clean API endpoints for review management
- 🚀 **Production Ready**: Error handling, validation, and proper architecture

---

## 🏗️ Architecture

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│  WhatsApp   │─────▶│    Twilio    │─────▶│   FastAPI   │
│   (User)    │      │   Webhook    │      │   Backend   │
└─────────────┘      └──────────────┘      └──────┬──────┘
                                                   │
                                                   ▼
                                            ┌─────────────┐
                                            │ PostgreSQL  │
                                            │  Database   │
                                            └──────┬──────┘
                                                   │
                                                   ▼
                                            ┌─────────────┐
                                            │    React    │
                                            │  Frontend   │
                                            └─────────────┘
```

### Tech Stack

**Backend:**
- FastAPI (Python web framework)
- SQLAlchemy (ORM)
- PostgreSQL (Database)
- Pydantic (Data validation)

**Frontend:**
- React 18
- Vite (Build tool)
- Native JavaScript (No additional libraries)

**Integration:**
- Twilio WhatsApp Business API
- ngrok (Local development tunneling)

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+** ([Download](https://www.python.org/downloads/))
- **Node.js 18+** and npm ([Download](https://nodejs.org/))
- **PostgreSQL 12+** ([Download](https://www.postgresql.org/download/))
- **ngrok** ([Download](https://ngrok.com/download))
- **Twilio Account** (Free tier available at [twilio.com](https://www.twilio.com))

---

## 🚀 Quick Start Guide

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd whatsapp-product-review-collector
```

### Step 2: Database Setup

```bash
# Start PostgreSQL service (if not running)
# On Windows: Check Services or use pgAdmin
# On Mac: brew services start postgresql
# On Linux: sudo systemctl start postgresql

# Create database
psql -U postgres
CREATE DATABASE reviews_db;
\q
```

### Step 3: Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
# Edit backend/.env with your database credentials
# DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/reviews_db

# Create database tables
python -m backend.create_tables

# Start backend server
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

**Backend will be available at:** `http://localhost:8000`

### Step 4: Frontend Setup

Open a **new terminal** window:

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

**Frontend will be available at:** `http://localhost:5173`

### Step 5: WhatsApp Integration Setup

#### A. Start ngrok

Open a **new terminal** window:

```bash
ngrok http 8000
```

Copy the **HTTPS forwarding URL** (e.g., `https://abc123.ngrok-free.app`)

#### B. Configure Twilio

1. **Create Twilio Account:**
   - Go to [twilio.com](https://www.twilio.com) and sign up
   - Verify your phone number

2. **Access WhatsApp Sandbox:**
   - Navigate to: `Console → Messaging → Try it out → Send a WhatsApp message`
   - Note the sandbox phone number (e.g., +1 415 523 8886)

3. **Join Sandbox:**
   - Open WhatsApp on your phone
   - Send the join code to the Twilio sandbox number
   - Example: `join happy-elephant`
   - Wait for confirmation message

4. **Configure Webhook:**
   - Go to: `Messaging → Settings → WhatsApp Sandbox Settings`
   - Under "WHEN A MESSAGE COMES IN":
     - URL: `https://your-ngrok-url.ngrok-free.app/webhook/whatsapp`
     - Method: `POST`
   - Click **Save**

---

## 💬 Usage

### Testing the Application

1. **Open WhatsApp** on your phone

2. **Start a conversation** with the Twilio sandbox number:

```
You: Hi
Bot: Which product is this review for?

You: iPhone 15 Pro
Bot: What's your name?

You: John Doe
Bot: Please send your review for iPhone 15 Pro.

You: Excellent camera quality and battery life. Highly recommended!
Bot: Thanks John Doe -- your review for iPhone 15 Pro has been recorded.
```

3. **View the review:**
   - Open browser: `http://localhost:5173`
   - Your review appears in the table!

---

## 📁 Project Structure

```
whatsapp-product-review-collector/
│
├── backend/
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── review_router.py      # API endpoints for reviews
│   │   └── webhook_router.py     # WhatsApp webhook handler
│   │
│   ├── __init__.py
│   ├── .env                       # Environment variables
│   ├── create_tables.py          # Database initialization
│   ├── database.py               # Database connection
│   ├── main.py                   # FastAPI application
│   ├── models.py                 # SQLAlchemy models
│   ├── requirements.txt          # Python dependencies
│   └── schemas.py                # Pydantic schemas
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx               # Main React component
│   │   └── index.jsx             # React entry point
│   │
│   ├── public/                   # Static assets
│   ├── .env                      # Frontend environment
│   ├── index.html                # HTML template
│   ├── package.json              # Node dependencies
│   └── vite.config.js            # Vite configuration
│
└── README.md
```

---

## 🔌 API Endpoints

### Health Check
```http
GET /health
```
Returns server and database status.

**Response:**
```json
{
  "status": "ok",
  "database": "ok"
}
```

### Get All Reviews
```http
GET /api/reviews
```
Returns all reviews ordered by creation date (newest first).

**Response:**
```json
[
  {
    "id": 1,
    "contact_number": "whatsapp:+917719826466",
    "user_name": "John Doe",
    "product_name": "iPhone 15 Pro",
    "product_review": "Excellent camera quality!",
    "created_at": "2025-11-19T14:30:00Z"
  }
]
```

### Create Review (Manual)
```http
POST /api/reviews
Content-Type: application/json

{
  "contact_number": "+1234567890",
  "user_name": "Jane Smith",
  "product_name": "MacBook Pro",
  "product_review": "Amazing performance!"
}
```

### WhatsApp Webhook
```http
POST /webhook/whatsapp
Content-Type: application/x-www-form-urlencoded

From=whatsapp:+1234567890&Body=Hello
```
Handles incoming WhatsApp messages (called by Twilio).

---

## 🗃️ Database Schema

### Reviews Table

| Column          | Type      | Description                    |
|-----------------|-----------|--------------------------------|
| id              | INTEGER   | Primary key (auto-increment)   |
| contact_number  | VARCHAR   | User's WhatsApp number         |
| user_name       | VARCHAR   | User's name                    |
| product_name    | VARCHAR   | Product being reviewed         |
| product_review  | TEXT      | Review content                 |
| created_at      | TIMESTAMP | Review creation time (UTC)     |

---

## 🧪 Testing

### Manual Testing

**Test Backend API:**
```bash
# Health check
curl http://localhost:8000/health

# Get reviews
curl http://localhost:8000/api/reviews

# Create review
curl -X POST http://localhost:8000/api/reviews \
  -H "Content-Type: application/json" \
  -d '{
    "contact_number": "+1234567890",
    "user_name": "Test User",
    "product_name": "Test Product",
    "product_review": "Great product!"
  }'
```

**Test Database:**
```bash
# Connect to database
psql -U postgres -d reviews_db

# View all reviews
SELECT * FROM reviews ORDER BY created_at DESC;

# Exit
\q
```

---

## 🐛 Troubleshooting

### Backend Issues

**Problem:** `ModuleNotFoundError: No module named 'fastapi'`
```bash
# Solution: Ensure virtual environment is activated
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

**Problem:** `Database connection failed`
```bash
# Solution: Check PostgreSQL is running
# Windows: Services → postgresql
# Mac: brew services list
# Linux: sudo systemctl status postgresql

# Verify credentials in backend/.env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/reviews_db
```

**Problem:** `Column does not exist error`
```bash
# Solution: Recreate database tables
psql -U postgres -d reviews_db -c "DROP TABLE reviews;"
python -m backend.create_tables
```

### Frontend Issues

**Problem:** `Cannot find module 'vite'`
```bash
# Solution: Reinstall dependencies
cd frontend
rm -rf node_modules package-lock.json
npm install
```

**Problem:** `404 Not Found` when accessing frontend
```bash
# Solution: Ensure index.html exists in frontend/ directory
# Check that it contains: <script type="module" src="/src/index.jsx"></script>
```

### WhatsApp Integration Issues

**Problem:** Bot doesn't respond to messages

**Solution 1:** Check ngrok is running and URL is correct
```bash
# Visit ngrok dashboard
http://localhost:4040

# Verify webhook URL in Twilio includes /webhook/whatsapp
https://your-url.ngrok-free.app/webhook/whatsapp
```

**Solution 2:** Check backend logs for errors
```bash
# Backend terminal should show:
Received message from whatsapp:+1234567890: Hi
Sending response: Which product is this review for?
```

**Solution 3:** Test webhook manually
```bash
curl -X POST http://localhost:8000/webhook/whatsapp \
  -d "From=whatsapp:+1234567890&Body=Hi"
```



# Set environment variable
# VITE_API_URL=https://your-backend-url.herokuapp.com
```

### Production Considerations

- [ ] Replace in-memory session storage with Redis
- [ ] Add authentication/authorization
- [ ] Implement rate limiting
- [ ] Add request logging and monitoring
- [ ] Use production Twilio number (not sandbox)
- [ ] Enable HTTPS
- [ ] Set up database backups
- [ ] Add input sanitization
- [ ] Implement error tracking (Sentry)
- [ ] Add unit and integration tests

---

## 🔒 Security Notes

- Never commit `.env` files to version control
- Use environment variables for sensitive data
- Validate and sanitize all user inputs
- Implement rate limiting in production
- Use HTTPS for all production endpoints
- Regularly update dependencies

---

## 📝 Environment Variables

### Backend (.env)
```env
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/reviews_db
HOST=0.0.0.0
PORT=8000
```

### Frontend (.env)
```env
VITE_API_URL=http://localhost:8000
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

Kindly reach out to me before contributing in the repo!


## 👨‍💻 Author

**Your Name**
- GitHub: [samruddhi kadam](https://github.com/SamruddhiKadam115)
- LinkedIn: [samruddhi kadam](https://www.linkedin.com/in/samruddhi-kadam-475b84292/)
- Email: kadamsamruddhi115@gmail.com

---

## 🙏 Acknowledgments

- FastAPI documentation
- Twilio WhatsApp API documentation
- React documentation
- PostgreSQL community

---

## 📞 Support

For issues or questions:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Open an issue on GitHub
3. Contact: kadamsamruddhi115@gmail.com

---

