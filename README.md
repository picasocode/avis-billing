
# 🚀 Avis Billing

Avis Billing is a modern **Point of Sale (POS) and Billing SaaS Platform** inspired by Ezo Billing.
It is built with **Django** for backend and designed to support **shop owners and staff** with seamless billing, subscription management, and PhonePe payment gateway integration.

---

## ✨ Features

* 🧾 **POS System**

  * Generate and manage bills
  * Send invoices via WhatsApp
  * Real-time updates

* 💳 **Subscription & Payments**

  * Yearly subscription via PhonePe API
  * SuperAdmin control to block unpaid users
  * Subscription status management

* 👨‍💼 **User Roles**

  * Shop Owner & Staff login
  * Role-based access control
  * SuperAdmin full control

* 📊 **Dashboard**

  * Manage products, sales, and customers
  * Track subscription plans
  * Analytics & reports

* 🔒 **Secure & Scalable**

  * Django backend with REST API
  * Modern UI (Next.js + shadcn planned)

---

## 🛠️ Tech Stack

* **Backend**: Django, Django REST Framework
* **Database**: PostgreSQL / MySQL
* **Frontend**: Next.js + shadcn (planned)
* **Payments**: PhonePe API integration
* **Messaging**: WhatsApp Business API (for invoices)
* **Containerization**: Docker

---

## 📦 Installation

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

### 4. Run Database Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Now visit 👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```ini
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/avis_billing
PHONEPE_MERCHANT_ID=your_merchant_id
PHONEPE_API_KEY=your_api_key
WHATSAPP_API_TOKEN=your_whatsapp_token
```

---

## 🐳 Docker Setup (Optional)

```bash
docker build -t avis-billing .
docker run -p 8000:8000 avis-billing
```

---

## 📖 Roadmap

* [ ] Complete POS module
* [ ] Add subscription & PhonePe integration
* [ ] Implement WhatsApp billing
* [ ] Deploy SaaS version with multi-tenancy

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

Developed by **[Picasocode](https://github.com/Picasocode)** ✨

---
