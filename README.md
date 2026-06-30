<div align="center">

# 🏥 PatientCare API
### *A Modern Patient Management System built with FastAPI*

<p align="center">
<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
<img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white">
<img src="https://img.shields.io/badge/REST_API-000000?style=for-the-badge">
<img src="https://img.shields.io/badge/JSON-Database-yellow?style=for-the-badge">
<img src="https://img.shields.io/github/license/yourusername/MediTrack-API?style=for-the-badge">
</p>

### 🚀 Fast • Secure • Lightweight • RESTful

*A complete Patient Management REST API featuring CRUD operations, automatic BMI calculation, intelligent health assessment, and robust data validation using FastAPI & Pydantic.*

</div>

---

# 📖 Overview

**MediTrack API** is a backend application developed using **FastAPI** that enables healthcare systems to efficiently manage patient records.

Instead of only storing patient information, the application performs **real-time BMI calculation**, provides **health status evaluation**, validates incoming data using **Pydantic**, and exposes a clean **RESTful API** for seamless integration with frontend or mobile applications.

This project demonstrates backend development best practices including:

- REST API Development
- CRUD Operations
- Data Validation
- Computed Fields
- JSON-based Data Storage
- Error Handling
- API Documentation

---

# ✨ Features

## 👨‍⚕️ Patient Management

- Create New Patient
- Update Existing Patient
- Delete Patient
- View All Patients
- View Individual Patient

---

## 🧠 Smart BMI Analysis

Automatically calculates:

- BMI
- Health Verdict

Health Categories:

- Underweight
- Normal
- Obese

---

## 🔍 Sorting Support

Sort patient records by:

- Height
- Weight
- BMI

Ascending or Descending order.

---

## 🛡 Data Validation

Powered by **Pydantic**

✔ Age Validation

✔ Height Validation

✔ Weight Validation

✔ Gender Validation

✔ Required Field Validation

---

## ⚡ FastAPI Features

- Interactive Swagger UI
- Automatic API Documentation
- JSON Responses
- HTTP Exception Handling
- Path Parameters
- Query Parameters

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| Pydantic | Data Validation |
| JSON | Lightweight Database |
| Uvicorn | ASGI Server |

---

# 📂 Project Structure

```
PatientCare-API
│
├── main.py
├── patients.json
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/aryxn-builds/PatientCare-API.git
```

---

### Move into Project

```bash
cd PatientCare-API
```

---

### Create Virtual Environment

Windows

```bash
python -m venv myenv
```

Activate

```bash
myenv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Server

```bash
uvicorn main:app --reload
```

Server will start at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

Redoc Documentation

```
http://127.0.0.1:8000/redoc
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Welcome Route |
| GET | /about | About API |
| GET | /view | Get All Patients |
| GET | /patients/{id} | Get Patient by ID |
| GET | /sort | Sort Patients |
| POST | /create | Create Patient |
| PUT | /edit/{id} | Update Patient |
| DELETE | /delete/{id} | Delete Patient |

---

# 📥 Example Request

```json
{
    "id": "P001",
    "name": "Aryan",
    "city": "Delhi",
    "age": 21,
    "gender": "male",
    "height": 1.75,
    "weight": 68
}
```

---

# 📤 Example Response

```json
{
    "name": "Aryan",
    "city": "Delhi",
    "age": 21,
    "gender": "male",
    "height": 1.75,
    "weight": 68,
    "bmi": 22.2,
    "verdict": "Normal"
}
```

---

# 🎯 Key Concepts Demonstrated

- REST API Design
- CRUD Operations
- FastAPI Routing
- Request Validation
- Response Models
- JSON Storage
- Computed Fields
- Exception Handling
- Path Parameters
- Query Parameters
- Clean Backend Architecture

---

# 📈 Future Improvements

- SQLite/PostgreSQL Integration
- JWT Authentication
- User Login System
- Role-Based Access Control
- Docker Support
- Unit Testing
- Pagination
- Search API
- Filtering
- Logging
- Cloud Deployment
- CI/CD Pipeline

---

# 🎓 Learning Outcomes

This project helped strengthen practical knowledge of:

- FastAPI
- Pydantic v2
- Backend Development
- API Design
- Data Validation
- JSON Handling
- CRUD Architecture
- Python Type Hinting

---

# 🤝 Contributing

Contributions are always welcome.

1. Fork the repository
2. Create your feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# ⭐ Support

If you found this project helpful:

⭐ Star this repository

🍴 Fork it

💡 Share it with others

---

<div align="center">

## 👨‍💻 Developed with ❤️ using FastAPI

### ⭐ If you like this project, don't forget to give it a Star!

</div>