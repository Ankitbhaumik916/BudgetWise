from flask import Flask, render_template, request, redirect, session, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="KAERMORHEN2311",
    database="BudgetWise"
)
cursor = db.cursor()

@app.route('/')
def home():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check if email already exists
        cursor.execute("SELECT * FROM Users WHERE email=%s", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            flash('Email already registered. Please login.', 'error')
            return redirect('/login')
        
        cursor.execute("INSERT INTO Users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        db.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        print(f"Attempting login with: {email} / {password}")  # Debugging

        cursor.execute("SELECT * FROM Users WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()

        print(f"User fetched: {user}")  # Debugging

        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Login successful! Welcome back.', 'success')
            return redirect('/dashboard')
        else:
            flash('Invalid Email or Password. Please try again.', 'error')
            return redirect('/login')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('You must be logged in to access the dashboard.', 'error')
        return redirect('/login')
    
    cursor.execute("SELECT SUM(amount) FROM Income WHERE user_id=%s", (session['user_id'],))
    total_income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM Expense WHERE user_id=%s", (session['user_id'],))
    total_expenses = cursor.fetchone()[0] or 0

    cursor.execute("SELECT category_id, category_name FROM Category")
    categories = cursor.fetchall()

    remaining = total_income - total_expenses

    return render_template('dashboard.html', username=session['username'], total_income=total_income, total_expenses=total_expenses, remaining=remaining, categories=categories)

@app.route('/add_income', methods=['POST'])
def add_income():
    if 'user_id' not in session:
        flash('Please login first.', 'error')
        return redirect('/login')
    
    source = request.form['source']
    amount = request.form['amount']
    income_date = request.form['income_date']
    cursor.execute("INSERT INTO Income (user_id, source, amount, income_date) VALUES (%s, %s, %s, %s)", (session['user_id'], source, amount, income_date))
    db.commit()
    flash('Income added successfully!', 'success')
    return redirect('/dashboard')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    if 'user_id' not in session:
        flash('Please login first.', 'error')
        return redirect('/login')

    category_id = request.form['category_id']
    amount = request.form['amount']
    expense_date = request.form['expense_date']
    description = request.form['description']
    cursor.execute("INSERT INTO Expense (user_id, category_id, amount, expense_date, description) VALUES (%s, %s, %s, %s, %s)", (session['user_id'], category_id, amount, expense_date, description))
    db.commit()
    flash('Expense added successfully!', 'success')
    return redirect('/dashboard')

@app.route('/set_budget', methods=['POST'])
def set_budget():
    if 'user_id' not in session:
        flash('Please login first.', 'error')
        return redirect('/login')
    
    month_year = request.form['month_year']
    budget_amount = request.form['budget_amount']
    cursor.execute("INSERT INTO Budget (user_id, month_year, budget_amount) VALUES (%s, %s, %s)", (session['user_id'], month_year, budget_amount))
    db.commit()
    flash('Budget set successfully!', 'success')
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully.', 'success')
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)
