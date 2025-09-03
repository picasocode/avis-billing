# 🚀 Avis Billing

Avis Billing is a modern **Point of Sale (POS) & Billing SaaS Platform** inspired by Ezo Billing.  
Built with **Django** on the backend, it empowers shop owners and staff to manage billing, subscriptions, and PhonePe payments with ease.

---

## ✨ Key Features

- 🧾 **POS System**
  - Effortlessly generate and manage bills
  - Send invoices directly via WhatsApp
  - Real-time updates for transactions

- 💳 **Subscriptions & Payments**
  - Hassle-free yearly subscriptions using PhonePe API
  - SuperAdmin control to block unpaid users
  - Automated subscription status management

- 👨‍💼 **User Roles & Access**
  - Separate logins for Shop Owners & Staff
  - Role-based access control ensures security
  - SuperAdmin has full system access

- 📊 **Intuitive Dashboard**
  - Monitor products, sales, and customers
  - Track subscription plans
  - Advanced analytics & reporting

- 🔒 **Security & Scalability**
  - Robust Django backend with RESTful API
  - Modern UI (Next.js + shadcn coming soon)
  - Scalable architecture for growing businesses

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL / MySQL  
- **Frontend:** Next.js + shadcn *(planned)*  
- **Payments:** PhonePe API integration  
- **Messaging:** WhatsApp Business API (invoices)  
- **Containerization:** Docker  

---

## 📦 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Picasocode/avis-billing.git
cd avis-billing
```

### 2. Setup Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Launch the Development Server

```bash
python manage.py runserver
```

Visit 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔑 Configuration

Create a `.env` file in the project root and add your environment variables:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/avis_billing
PHONEPE_MERCHANT_ID=your_merchant_id
PHONEPE_API_KEY=your_api_key
WHATSAPP_API_TOKEN=your_whatsapp_token
```

---

## 🐳 Docker Deployment (Optional)

Build and run using Docker:

```bash
docker build -t avis-billing .
docker run -p 8000:8000 avis-billing
```

---

## 📖 Roadmap

- [ ] Complete POS module
- [ ] Integrate subscription & PhonePe payments
- [ ] Enable WhatsApp invoice delivery
- [ ] Deploy SaaS version with multi-tenancy

---

## 🤝 Contributing

We welcome contributions! To get started:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

Developed by [Picasocode](https://github.com/Picasocode) ✨

```
