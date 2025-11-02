# 🎓 Placement Eligibility Streamlit Application

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![SQL](https://img.shields.io/badge/Database-SQL-green?logo=postgresql)
![Faker](https://img.shields.io/badge/Data-Faker-orange)
![OOP](https://img.shields.io/badge/Concepts-OOP-yellow)
![Domain](https://img.shields.io/badge/Domain-EdTech-purple)

---

## 📘 Overview
**Placement Eligibility Streamlit Application** is a data-driven web application designed to help educational institutions and placement teams identify eligible students for recruitment opportunities.  

The app integrates **Python (OOP)**, **SQL**, and **Streamlit** to deliver an interactive experience — allowing users to set **eligibility filters**, analyze **student performance**, and visualize **placement readiness insights** in real-time.  

This project demonstrates the complete journey from **synthetic dataset generation using Faker** to **interactive analytics through Streamlit dashboards**.

---

## 🎯 Problem Statement
Design and develop a **Streamlit-based Placement Eligibility System** where users can input criteria (e.g., coding performance, soft skills, internship experience) to identify students who meet placement requirements.  

The solution must integrate:
- 🎓 A **relational database** storing interconnected student data  
- 🧠 **SQL-based analytics** for performance and eligibility insights  
- ⚡ An **interactive dashboard** for real-time decision-making  

---

## 💼 Business Use Cases

### 1. 🧾 Placement Management
- Filter and shortlist students based on **custom eligibility criteria**  
- Identify **top-performing candidates** for specific job profiles  

### 2. 📊 Student Performance Tracking
- Analyze readiness for placements based on **technical** and **soft skills**  
- Track overall progress across batches and departments  

### 3. 📈 Interactive Analytics
- Visualize trends such as **average coding scores**, **mock interview performance**, or **soft skill distribution**  
- Enable **data-driven decisions** for placement coordinators and faculty  

---

## 🧠 Skills Takeaway
- **Streamlit** – Building interactive web applications  
- **Faker Library** – Generating synthetic relational datasets  
- **Python OOP** – Implementing class-based architecture for data handling  
- **SQL** – Writing optimized queries for analytics and insights  
- **Relational Databases** – Managing student data across multiple linked tables  
- **Data Visualization** – Presenting insights dynamically using Streamlit  

---

## ⚙️ Approach Summary

### 🧩 Step 1: Dataset Creation
- Generate **synthetic data** using the `Faker` library for four relational tables:
  - **Students Table:** Basic student details (name, age, contact, enrollment)  
  - **Programming Table:** Performance metrics (problems solved, projects completed)  
  - **Soft Skills Table:** Communication, teamwork, and presentation scores  
  - **Placements Table:** Placement readiness, mock interview scores, internship data  
- Establish **relationships** among the tables using unique student IDs.  

### 🗄️ Step 2: Data Storage
- Store generated data in a **relational database** such as **SQLite** or **MySQL**.  
- Use **Python OOP** classes for database connection, query execution, and CRUD operations.  

### 🖥️ Step 3: Streamlit Application
- Build an intuitive **user interface** to:
  - Input eligibility criteria (e.g., coding score > 70, soft skills > 75).  
  - View **filtered eligible students** dynamically.  
  - Display **analytics dashboards** summarizing performance and placement readiness.  

### 📊 Step 4: SQL Insights & Analytics
- Develop and execute **10 SQL queries** for data-driven insights, such as:
  - Average programming performance per batch  
  - Top 5 students ready for placement  
  - Soft skills distribution visualization  
- Embed these analytical results within the **Streamlit dashboard**.  


<details>
<summary>📸 Click to view Streamlit UI screenshots</summary>

#### Home Page  
![Home Page]("D:\AI Images\Home Page.jpg")

#### Results Page  
![Results Page](assets/results_page.png)

#### Analytics Dashboard  
![Dashboard](assets/dashboard.png)

</details>

---

## 🧩 Project Structure
```bash
Placement-Eligibility-App/
│
├── app/
│   ├── streamlit_app.py          # Main Streamlit user interface
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
