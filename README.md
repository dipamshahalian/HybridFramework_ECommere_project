**HybridFramework_ECommerce_project**:  

---

# 🛒 Hybrid Framework for E-Commerce Testing  

![Selenium](https://img.shields.io/badge/Selenium-Automation-blue?style=for-the-badge&logo=selenium)  
![Python](https://img.shields.io/badge/Python-Testing-green?style=for-the-badge&logo=python)  
![Pytest](https://img.shields.io/badge/Pytest-Test_Framework-orange?style=for-the-badge&logo=pytest)  
![MySQL](https://img.shields.io/badge/MySQL-Data_Driven-red?style=for-the-badge&logo=mysql)  

## 📌 Overview  
This **Hybrid Test Automation Framework** is designed for testing **E-Commerce applications** using **Selenium WebDriver, Python, and Pytest**. The framework follows a **data-driven, keyword-driven, and modular approach** to ensure efficient, scalable, and maintainable test automation.  

## 🚀 Features  
✅ **Hybrid Framework** (Data-Driven + Keyword-Driven + Page Object Model)  
✅ **Pytest Integration** for structured test execution  
✅ **Selenium WebDriver** for browser automation  
✅ **MySQL Database** for data-driven testing  
✅ **Logging & Reporting** with **pytest-html**  
✅ **Cross-browser testing** support  

## 🏗️ Tech Stack  
- **Language:** Python 🐍  
- **Testing Framework:** Pytest 🧪  
- **Automation Tool:** Selenium WebDriver 🌐  
- **Database:** MySQL 🗄️  
- **Logging & Reporting:** Python Logging, pytest-html 📜  

## 📂 Project Structure  
```
HybridFramework_ECommerce_project/
│── tests/              # Test cases
│── pages/              # Page Object Model (POM) classes
│── utilities/          # Utility functions (logging, DB connection, etc.)
│── config/             # Configurations (URLs, credentials, etc.)
│── reports/            # Test reports (HTML/XML)
│── logs/               # Log files
│── conftest.py         # Pytest fixtures and setup
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```  

## 🔧 Setup & Installation  
1️⃣ Clone the repository:  
```bash
git clone https://github.com/dipamshahalian/HybridFramework_ECommere_project.git
cd HybridFramework_ECommere_project
```  

2️⃣ Install dependencies:  
```bash
pip install -r requirements.txt
```  

3️⃣ Update **config/config.ini** with your application URL and credentials.  

4️⃣ Run tests:  
```bash
pytest --html=reports/test_report.html --self-contained-html
```  

## 📊 Reporting & Logs  
- **Test Reports:** Generated in **reports/** as HTML files.  
- **Logs:** Execution logs stored in **logs/** for debugging.  

## 🤝 Contributing  
Feel free to **fork** this repo, create a branch, and submit a **pull request** if you'd like to contribute!  

## 📜 License  
This project is licensed under the **MIT License**.  

---

🔥 **Let's automate E-Commerce testing efficiently!** 🚀
