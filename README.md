# 📈 BudgetWise

BudgetWise is a simple, smart, and efficient web application that helps users track their income, expenses, set budgets, and manage finances securely.

Built using:
- **Flask** (Python Web Framework)
- **MySQL** (Database)
- **HTML/CSS** (Frontend Templates)

---

## 🚀 Features

- 📝 **User Registration and Login**
- 💼 **Add and Track Income**
- 💒 **Add and Track Expenses (with Categories)**
- 🎯 **Set Monthly Budgets**
- 📊 **Dashboard Overview**
- 🔒 **Session-based Authentication**
- 💬 **Flash Messaging for User Feedback**

---

## 🛠️ Installation and Setup

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/budgetwise.git
cd budgetwise
```

2. **Install Required Python Libraries**  
```bash
pip install flask mysql-connector-python
```

3. **Set up the MySQL Database**
- Create a database named `BudgetWise`
- Create the following tables:

```sql
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE Category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255)
);

CREATE TABLE Income (
    income_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    source VARCHAR(255),
    amount DECIMAL(10, 2),
    income_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Expense (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category_id INT,
    amount DECIMAL(10, 2),
    expense_date DATE,
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

CREATE TABLE Budget (
    budget_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    month_year VARCHAR(20),
    budget_amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
```

4. **Configure your database connection** inside `app.py`
```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="BudgetWise"
)
```

5. **Run the Flask Application**
```bash
python app.py
```

6. **Visit your app!**
```bash
Open your browser and go to: http://127.0.0.1:5000/
```

---

## 🖼️ Folder Structure

```
/budgetwise
    /templates
        - login.html
        - register.html
        - dashboard.html
    /static
        - (CSS, JS, Images here if needed)
    app.py
    README.md
```

---

## ⚡ Technologies Used

- Python
- Flask
- MySQL
- HTML5/CSS3
- Bootstrap (optional for styling)

---

## 💡 Future Enhancements (Coming Soon!)

- Password encryption (using Hashing algorithms 🔐)
- Better UI/UX with Bootstrap or TailwindCSS
- Graphical financial reports (Pie charts, bar graphs 📊)
- Email Notifications / Monthly Reports
- API version (for mobile apps!)

---

## ✨ Author

| Name | GitHub | LinkedIn |
|:---|:---|:---|
| Ankit Bhaumik | [GitHub Profile](https://github.com/your-username) | [LinkedIn Profile](https://linkedin.com/in/your-linkedin) |

---

## 📝 License

This project is open-source and free to use!  
Feel free to fork, modify, and improve it.

---

# 🌟 Let's Make Money Management Smarter with **BudgetWise**!

