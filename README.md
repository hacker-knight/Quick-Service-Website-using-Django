
# 🛒 Quick-Service Website using Django

A dynamic e-commerce platform built using Django to empower **local small shop owners** by bringing their businesses online and enabling **same-day, no-extra-cost delivery** to nearby customers.

## 📌 Project Overview

**Quick-Service Website** aims to create a hyperlocal e-commerce ecosystem where:
- **Shopkeepers** can list their products and manage their storefronts.
- **Users** can browse nearby shops, place orders, and receive products the same day without extra delivery charges.

This platform bridges the gap between **local trust** and **digital convenience**, helping communities thrive while keeping commerce local.

## 👥 User Roles

### 🧑‍💼 Shopkeepers
- Register and manage their shop profiles
- List products for sale
- Manage inventory
- Handle order deliveries (the platform does not manage delivery logistics)

### 🛍️ Users
- Browse local shops and products
- Place orders from nearby trusted stores
- Track order status and confirm delivery upon arrival

## 🚀 Key Features

- User and Shopkeeper authentication system
- Product listing and categorization
- Order placement and tracking system
- Admin panel for backend management
- Localized product discovery and search

## ⚙️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite
- **Other**: Django Admin, Django Forms, Session Management

## 💡 Benefits

- Supports local economy and small business growth
- Eliminates high delivery charges of big e-commerce platforms
- Same-day delivery from trusted local shops
- Simple interface for shopkeepers and customers alike

## 📷 Screenshots

*Coming Soon: Add screenshots of Shopkeeper Dashboard, User Panel, and Product Pages.*

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hacker-knight/Quick-Service-Website-using-Django.git
   cd quick-service-django
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations and run server**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

5. **Access the website**
   - Visit `http://127.0.0.1:8000/` in your browser

## 🧪 Testing

- Create a shopkeeper and user account to test both panels
- Add products via shopkeeper panel
- Place and track an order from user panel

## 🔐 Admin Credentials (for demo)

> Update with your demo credentials if needed, or remove this section before public release.
