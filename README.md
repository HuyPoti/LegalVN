# ⚖️ LegalBot - Intelligent Legal Assistant (RAG-Based)

[Tiếng Việt](./README_VN.md) | **English**

LegalBot is a legal consultation chatbot system specifically designed for Vietnamese law. Using **RAG (Retrieval-Augmented Generation)** technology combined with the **Google Gemini** language model, the system provides accurate answers based on official legal document databases.

---

## 🚀 Key Features

### 💬 For Users
- **24/7 Legal Consultation:** Answer queries about civil, criminal, labor, land laws, etc.
- **Reference Retrieval:** Each answer comes with citations from specific legal documents (File name, original content).
- **Chat History:** Store and review past consultation sessions.
- **API Key Encryption:** Allows users to use personal Gemini API Keys safely for unlimited usage.
- **Premium System:** Daily usage limits for free users, with upgrade requests for unlimited access.
- **Account Verification:** Automated registration and verification via Email.

### 🛡️ For Administrators (Admin)
- **Knowledge Base Management:** Upload legal documents (PDF, TXT) directly to the Vector Database (Pinecone).
- **User Management:** Approve Premium upgrade requests, lock/unlock accounts.
- **System Configuration:** Customize Pinecone API Key and Index directly on the Dashboard.
- **Data Management:** Delete or update files in the RAG database.

---

## 🛠️ Tech Stack

### Backend
- **Framework:** FastAPI (Python 3.10+)
- **LLM:** Google Gemini AI
- **Vector Database:** Pinecone (Vector storage and search)
- **Database:** MongoDB (User info and chat history storage)
- **Authentication:** JWT (JSON Web Token) & OAuth2
- **Email Service:** SMTP (Gmail)

### Frontend
- **Framework:** Next.js 15 (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS (Modern Glassmorphism UI)
- **State Management:** React Hooks
- **Communication:** Axios

---

## ⚙️ System Configuration

### 1. Backend Environment (`backend/.env`)
Create a `.env` file in the `backend/` directory and configure the following variables:
```env
# MongoDB Connection
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/your-db-name

# Security
SECRET_KEY=yoursecretkeyhere
ALGORITHM=HS256

# AI & Vector DB
GOOGLE_API_KEY=your_gemini_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=legal-chatbot

# Email Config (Gmail App Password)
EMAIL_FROM=your_email@gmail.com
EMAIL_PASSWORD=your_app_password

# API Config
PORT=10000
API_URL=http://localhost:10000
```

### 2. Frontend Environment (`frontend/.env.local`)
Create a `.env.local` file in the `frontend/` directory and configure:
```env
NEXT_PUBLIC_API_URL=http://localhost:10000
```

---

## 📦 Installation Guide

### Step 1: Clone the project
```bash
git clone https://github.com/HuyPoti/LegalVN.git
cd Legal-Consultation-Chatbot-VN
```

### Step 2: Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Step 3: Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Visit: `http://localhost:3000` to get started.

---

## 📂 Project Structure
```text
LegalVN/
├── backend/
│   ├── main.py           # Entry point (FastAPI)
│   ├── rag_engine.py      # RAG logic & Pinecone handling
│   ├── chatbot.py        # Gemini LLM integration
│   ├── models.py         # Pydantic schemas & MongoDB
│   ├── auth.py           # JWT & Authentication handling
│   └── email_utils.py    # Verification/Reset password emails
├── frontend/
│   ├── app/              # Next.js App Router
│   │   ├── admin/        # Admin interface
│   │   ├── chat/         # Chat interface
│   │   ├── signup/       # Signup
│   │   └── verify-email/ # Account verification
│   └── components/       # Shared UI components
└── README.md
```

---

## 🔒 Security & Notes
- Sensitive information (User API Keys) is encrypted using **Fernet (Cryptography)** before being saved to the database.
- Do not share the `.env` file on Github (`.gitignore` is already configured).

---
**Developed by [HuyPoti](https://github.com/HuyPoti)**  
*This project is for educational purposes and basic legal consultation.*
