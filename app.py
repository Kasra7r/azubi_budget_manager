
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_bcrypt import Bcrypt
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budget.db'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    categories = db.relationship('Category', backref='user', lazy=True)
    transactions = db.relationship('Transaction', backref='user', lazy=True)
    budgets = db.relationship('Budget', backref='user', lazy=True)

@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(10), default='expense')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    transactions = db.relationship('Transaction', backref='category', lazy=True)
    budgets = db.relationship('Budget', backref='category', lazy=True)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10))
    description = db.Column(db.String(200))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)
    amount = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        h=bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        u=User(username=request.form['username'], email=request.form['email'], password_hash=h)
        db.session.add(u); db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        u=User.query.filter_by(email=request.form['email']).first()
        if u and bcrypt.check_password_hash(u.password_hash, request.form['password']):
            login_user(u); return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user(); return redirect(url_for('login'))

@app.route('/')
@login_required
def dashboard():
    incomes = db.session.query(db.func.sum(Transaction.amount)).filter_by(user_id=current_user.id, type='income').scalar() or 0
    expenses = db.session.query(db.func.sum(Transaction.amount)).filter_by(user_id=current_user.id, type='expense').scalar() or 0
    balance = incomes-expenses

    current_month = date.today().month
    current_year = date.today().year
    user_budgets = Budget.query.filter_by(user_id=current_user.id, month=current_month, year=current_year).all()
    budget_info=[]
    for b in user_budgets:
        spent = db.session.query(db.func.sum(Transaction.amount)).filter_by(
            user_id=current_user.id, category_id=b.category_id, type='expense').scalar() or 0
        budget_info.append({'category':b.category.name,'limit':b.amount,'spent':spent,'remaining':b.amount-spent})

    return render_template('dashboard.html', incomes=incomes, expenses=expenses, balance=balance,
                           budget_info=budget_info, current_month=current_month, current_year=current_year)

@app.route('/categories', methods=['GET','POST'])
@login_required
def categories():
    if request.method=='POST':
        c=Category(name=request.form['name'], type=request.form['type'], user_id=current_user.id)
        db.session.add(c); db.session.commit()
        return redirect(url_for('categories'))
    cats=Category.query.filter_by(user_id=current_user.id).all()
    return render_template('categories.html', categories=cats)

@app.route('/transactions', methods=['GET','POST'])
@login_required
def transactions():
    cats=Category.query.filter_by(user_id=current_user.id).all()
    if request.method=='POST':
        t=Transaction(
            amount=float(request.form['amount']),
            type=request.form['type'],
            description=request.form['description'],
            category_id=int(request.form['category_id']),
            user_id=current_user.id,
            date=date.fromisoformat(request.form['date']) if request.form['date'] else date.today()
        )
        db.session.add(t); db.session.commit()
        return redirect(url_for('transactions'))
    tx=Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.date.desc()).all()
    return render_template('transactions.html', transactions=tx, categories=cats)

@app.route('/budgets', methods=['GET','POST'])
@login_required
def budgets():
    cats=Category.query.filter_by(user_id=current_user.id).all()
    if request.method=='POST':
        b=Budget(
            month=int(request.form['month']),
            year=int(request.form['year']),
            amount=float(request.form['amount']),
            category_id=int(request.form['category_id']),
            user_id=current_user.id
        )
        db.session.add(b); db.session.commit()
        return redirect(url_for('budgets'))
    bgs=Budget.query.filter_by(user_id=current_user.id).all()
    return render_template('budgets.html', budgets=bgs, categories=cats)

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
