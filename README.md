# 🔐 Security Exposure Scanner

A modular web-based security exposure assessment tool built using Python.  
The application performs reconnaissance and security checks against domains and email addresses to identify potential exposure risks.

---

## 🚀 Core Features

- 🔎 Subdomain Enumeration
- 🌐 Open Port Scanning
- 📧 Email Exposure Scanning
- 🔐 SSL Certificate Analysis
- 🛡 Breach Detection
- 📊 Risk Scoring Engine
- 🗄 Scan Result Storage (Database Integration)
- 🐳 Docker Support

---

## 🏗 Architecture

```
Security-Exposure-Scanner/
│
├── app.py
├── config.py
├── Dockerfile
├── requirements.txt
│
├── models/
│   └── database.py
│
├── modules/
│   ├── breach_checker.py
│   ├── email_scanner.py
│   ├── port_scanner.py
│   ├── risk_engine.py
│   ├── ssl_checker.py
│   └── subdomain_scanner.py
│
├── templates/
│   ├── dashboard.html
│   └── index.html
│
├── static/
│   └── style.css
│
└── scans/
```



## 🛠 Tech Stack

- Python 3
- Flask
- SQLite / Database Layer
- Docker
- OSINT Techniques
- Git & GitHub

---

## 📦 Installation (Local Setup)

Clone the repository:

git clone https://github.com/sakshamcy/Security-Exposure-Scanner.git

Navigate into the folder:

cd Security-Exposure-Scanner

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

---

## 🐳 Run With Docker

docker build -t security-scanner .

docker run -p 5000:5000 security-scanner

---

## 🎯 Project Objective

This project was built to:

- Practice real-world reconnaissance techniques
- Implement modular cybersecurity scanning logic
- Understand exposure analysis workflows
- Strengthen skills for VAPT and Security Analyst roles

---

## ⚠️ Disclaimer

This tool is intended strictly for educational and authorized security testing purposes.  
Unauthorized scanning of systems is illegal.

---

## 👨‍💻 Author

Saksham  
Cybersecurity Enthusiast | VAPT Learner | Security Analyst Aspirant
