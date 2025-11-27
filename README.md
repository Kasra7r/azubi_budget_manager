Azubi Budget Manager
Personal Finance & Budget Tracking App for Apprentices (Azubis)
Web-Anwendung zur Verwaltung persönlicher Finanzen für Auszubildende

🇩🇪 Deutsch
📌 Über das Projekt

Der Azubi Budget Manager ist eine vollständige Web-Anwendung, die Auszubildenden hilft, ihre persönlichen Finanzen zu organisieren.
Benutzer können Einnahmen, Ausgaben, Kategorien und monatliche Budgets verwalten und erhalten im Dashboard eine übersichtliche Darstellung ihrer finanziellen Situation.

Dieses Projekt wurde im Rahmen der Vorbereitung auf eine Ausbildung zum
Fachinformatiker Anwendungsentwicklung entwickelt.

🚀 Funktionen
✔ Benutzer-Registrierung & Login

Sichere Passwort-Hashing (Flask-Bcrypt)

Login geschützte Bereiche (Flask-Login)

✔ Einnahmen & Ausgaben

Erstellen, Auflisten, Kategorisieren

Beschreibung, Datum, Typ (income/expense)

✔ Kategorien

Kategorien für Ausgaben & Einnahmen

z. B. Miete, Lebensmittel, Ticket, Freizeit, Vergütung

✔ Monatliche Budgets

Budget pro Kategorie festlegen

Dashboard zeigt: Budget, Ausgegeben, Restbetrag

Warnung bei Überschreitung (roter Text)

✔ Dashboard

Gesamt-Einnahmen

Gesamt-Ausgaben

Aktuelle Balance

Budgetübersicht des aktuellen Monats

(optional erweiterbar mit Diagrammen)

🛠 Technologien

Python 3

Flask

Flask-SQLAlchemy (SQLite)

Flask-Login & Flask-Bcrypt

HTML, CSS, Bootstrap 5

Chart.js (optional)

📦 Installation & Start
# Repository klonen
git clone https://github.com/DEIN_USERNAME/azubi_budget_manager.git
cd azubi_budget_manager

# Virtuelle Umgebung erstellen
python -m venv venv
venv\Scripts\activate   # Windows

# Abhängigkeiten installieren
pip install -r requirements.txt

# Anwendung starten
python app.py


Dann öffnen:
👉 http://127.0.0.1:5000

🗂 Benutzung

Unter /register ein neues Benutzerkonto erstellen

Unter /login einloggen

Kategorien anlegen

Einnahmen/Ausgaben hinzufügen

Monatliche Budgets zuweisen

Dashboard ansehen

🎯 Ziel des Projekts

Dieses Projekt zeigt:

Verständnis von Web-Entwicklung mit Flask

Umgang mit Datenbanken (SQLAlchemy)

Implementierung von Login-Systemen

Strukturierung von Templates & Routen

Planung einer vollständigen Anwendung

🇬🇧 English
📌 About the Project

The Azubi Budget Manager is a complete web application designed to help apprentices (Azubis) manage their personal finances efficiently.
Users can track income, expenses, categories, and monthly budgets, and visualize everything in a clean and simple dashboard.

This project was created as part of my preparation for an apprenticeship as a
Software Developer (Fachinformatiker Anwendungsentwicklung).

🚀 Features
✔ User Registration & Login

Secure password hashing (Flask-Bcrypt)

Login-protected pages (Flask-Login)

✔ Income & Expense Tracking

Add, list, organize by category

Description, date, type (income/expense)

✔ Categories

Create expense & income categories

Examples: Rent, Food, Transport, Leisure, Salary

✔ Monthly Budgets

Set monthly budgets per category

Dashboard shows: limit, spent, remaining

Highlight when budget exceeded

✔ Dashboard

Total incomes

Total expenses

Current balance

Monthly budget summary

(Can be extended with charts)

🛠 Tech Stack

Python 3

Flask

Flask-SQLAlchemy (SQLite)

Flask-Login & Flask-Bcrypt

HTML, CSS, Bootstrap 5

Chart.js (optional)

📦 How to Install & Run
# Clone the repository
git clone https://github.com/YOUR_USERNAME/azubi_budget_manager.git
cd azubi_budget_manager

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Start the app
python app.py


Open in browser:
👉 http://127.0.0.1:5000

🗂 How to Use

Register a new user via /register

Log in via /login

Create categories

Add income and expenses

Set monthly budgets

View everything on the dashboard

🎯 Purpose of This Project

This project demonstrates:

Understanding of backend development with Flask

Database modeling with SQLAlchemy

Secure authentication concepts

Clean template and routing structure

Ability to design a complete, useful application
