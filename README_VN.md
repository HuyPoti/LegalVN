# ⚖️ LegalBot - Trợ Lý Pháp Luật Thông Minh (RAG-Based)

**Tiếng Việt** | [English](./README.md)

LegalBot là một hệ thống chatbot tư vấn pháp luật dành riêng cho luật pháp Việt Nam. Sử dụng công nghệ **RAG (Retrieval-Augmented Generation)** kết hợp với mô hình ngôn ngữ **Google Gemini**, hệ thống cung cấp các câu trả lời chính xác dựa trên cơ sở dữ liệu văn bản luật chính thống.

---

## 🚀 Tính Năng Chính

### 💬 Dành cho Người Dùng (Users)
- **Tư vấn pháp luật 24/7:** Giải đáp các thắc mắc về dân sự, hình sự, lao động, đất đai...
- **Truy xuất nguồn tham khảo:** Mỗi câu trả lời đi kèm với trích dẫn từ văn bản luật cụ thể (Tên file, nội dung gốc).
- **Lịch sử trò chuyện:** Lưu trữ và xem lại các phiên tư vấn cũ.
- **Mã hóa API Key:** Cho phép người dùng sử dụng API Key Gemini cá nhân để dùng không giới hạn (đã được mã hóa an toàn).
- **Hệ thống Premium:** Giới hạn lượt dùng hàng ngày cho người dùng miễn phí, yêu cầu nâng cấp để sử dụng không giới hạn.
- **Xác thực tài khoản:** Đăng ký và xác thực qua Email tự động.

### 🛡️ Dành cho Quản Trị Viên (Admin)
- **Quản lý tri thức (Knowledge Base):** Upload tài liệu pháp luật (PDF, TXT) trực tiếp lên Vector Database (Pinecone).
- **Quản lý người dùng:** Duyệt yêu cầu nâng cấp Premium, khóa/mở khóa tài khoản.
- **Cấu hình hệ thống:** Tùy chỉnh API Key Pinecone và Index ngay trên Dashboard.
- **Quản lý dữ liệu:** Xóa hoặc cập nhật các tệp tin trong cơ sở dữ liệu RAG.

---

## 🛠️ Công Nghệ Sử Dụng (Tech Stack)

### Backend
- **Framework:** FastAPI (Python 3.10+)
- **LLM:** Google Gemini AI
- **Vector Database:** Pinecone (Lưu trữ và tìm kiếm vector)
- **Database:** MongoDB (Lưu trữ thông tin người dùng và lịch sử chat)
- **Authentication:** JWT (JSON Web Token) & OAuth2
- **Email Service:** SMTP (Gmail)

### Frontend
- **Framework:** Next.js 15 (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS (Modern Glassmorphism UI)
- **State Management:** React Hooks
- **Communication:** Axios

---

## ⚙️ Cấu Hình Hệ Thống

### 1. Backend Environment (`backend/.env`)
Tạo file `.env` trong thư mục `backend/` và cấu hình các biến sau:
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
Tạo file `.env.local` trong thư mục `frontend/` và cấu hình:
```env
NEXT_PUBLIC_API_URL=http://localhost:10000
```

---

## 📦 Hướng Dẫn Cài Đặt

### Bước 1: Clone dự án
```bash
git clone https://github.com/HuyPoti/LegalVN.git
cd Legal-Consultation-Chatbot-VN
```

### Bước 2: Cài đặt Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Bước 3: Cài đặt Frontend
```bash
cd frontend
npm install
npm run dev
```

Truy cập: `http://localhost:3000` để bắt đầu.

---

## 📂 Cấu Trúc Thư Mục
```text
LegalVN/
├── backend/
│   ├── main.py           # Entry point (FastAPI)
│   ├── rag_engine.py      # Logic xử lý RAG & Pinecone
│   ├── chatbot.py        # Tích hợp Gemini LLM
│   ├── models.py         # schemas Pydantic & MongoDB
│   ├── auth.py           # Xử lý JWT & Authentication
│   └── email_utils.py    # Gửi mail xác thực/reset pass
├── frontend/
│   ├── app/              # Next.js App Router
│   │   ├── admin/        # Giao diện quản trị
│   │   ├── chat/         # Giao diện hội thoại
│   │   ├── signup/       # Đăng ký
│   │   └── verify-email/ # Xác thực tài khoản
│   └── components/       # Các UI components dùng chung
└── README_VN.md
```

---

## 🔒 Bảo Mật & Lưu Ý
- Thông tin nhạy cảm (API Keys) của người dùng được mã hóa bằng **Fernet (Cryptography)** trước khi lưu vào database.
- Không chia sẻ file `.env` lên Github (đã cấu hình `.gitignore`).

---
**Phát triển bởi [HuyPoti](https://github.com/HuyPoti)**  
*Dự án phục vụ mục đích học tập và tư vấn pháp luật cơ bản.*