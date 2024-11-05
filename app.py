
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'database/chocolate_house.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

# Seasonal Flavors Routes
@app.route('/flavors')
def flavors():
    conn = get_db_connection()
    flavors = conn.execute('SELECT * FROM seasonal_flavors').fetchall()
    conn.close()
    return render_template('flavors.html', flavors=flavors)

@app.route('/flavors/add', methods=('GET', 'POST'))
def add_flavor():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        conn = get_db_connection()
        conn.execute('INSERT INTO seasonal_flavors (name, description) VALUES (?, ?)', (name, description))
        conn.commit()
        conn.close()
        return redirect(url_for('flavors'))

    return render_template('add_flavor.html')

# Ingredient Inventory Routes
@app.route('/ingredients')
def ingredients():
    conn = get_db_connection()
    ingredients = conn.execute('SELECT * FROM ingredients').fetchall()
    conn.close()
    return render_template('ingredients.html', ingredients=ingredients)

@app.route('/ingredients/add', methods=('GET', 'POST'))
def add_ingredient():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']

        conn = get_db_connection()
        conn.execute('INSERT INTO ingredients (name, quantity) VALUES (?, ?)', (name, quantity))
        conn.commit()
        conn.close()
        return redirect(url_for('ingredients'))

    return render_template('add_ingredient.html')

# Customer Suggestions and Allergies
@app.route('/suggestions', methods=('GET', 'POST'))
def suggestions():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        suggestion = request.form['suggestion']
        allergy_info = request.form['allergy_info']

        conn = get_db_connection()
        conn.execute('INSERT INTO customer_suggestions (customer_name, suggestion, allergy_info) VALUES (?, ?, ?)',
                     (customer_name, suggestion, allergy_info))
        conn.commit()
        conn.close()
        return redirect(url_for('suggestions'))

    conn = get_db_connection()
    suggestions = conn.execute('SELECT * FROM customer_suggestions').fetchall()
    conn.close()
    return render_template('suggestions.html', suggestions=suggestions)


@app.errorhandler(500)
def internal_error(error):
    return "Internal Server Error: " + str(error), 500

# Your existing routes and logic here

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


