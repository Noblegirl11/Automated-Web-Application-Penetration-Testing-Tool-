# 🔍 Automated Web Application Penetration Testing Tool

## 📌 Overview  
This project is an **Automated Web Application Penetration Testing Tool** that scans web applications for **common security vulnerabilities** such as:  
- ✅ **SQL Injection (SQLi)**  
- ✅ **Cross-Site Scripting (XSS)**  
- ✅ **Cross-Site Request Forgery (CSRF)**  
- ✅ **Open Ports & Security Misconfigurations**  

It automates web security assessments and generates a **detailed vulnerability report**.  

---

## 🚀 Features  
✔ **Automated scanning for SQLi, XSS, CSRF**  
✔ **Open port & subdomain enumeration**  
✔ **Screenshot-based reporting**  
✔ **Uses OWASP ZAP API for advanced security scans**  
✔ **Command-line interface (CLI) + GUI support**  

---

## 🛠️ Tech Stack  
- **Python 3.x**  
- **BeautifulSoup, Selenium** (Web Scraping)  
- **OWASP ZAP API** (Vulnerability Scanning)  
- **Requests, Scapy** (Network Analysis)  

---

## 📥 Installation  

Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

Download OWASP ZAP (For advanced scanning)
Download from: OWASP ZAP Official Site
Start ZAP manually before running the scan.

[✔] Target: https://example.com
[✔] Checking for SQL Injection... Potential Vulnerability Found! 
[✔] Checking for XSS... Safe ✅
[✔] Checking for CSRF... Warning! Potential Risk 🚨

