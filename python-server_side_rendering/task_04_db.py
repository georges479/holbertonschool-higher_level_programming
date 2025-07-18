from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def read_json_products(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return [dict(p) for p in data]
    except Exception:
        return None

def read_csv_products(filepath):
    try:
        with open(filepath, newline='') as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                try:
                    row['id'] = int(row['id'])
                except Exception:
                    row['id'] = row['id']
                try:
                    row['price'] = float(row['price'])
                except Exception:
                    row['price'] = row['price']
                data.append(row)
        return data
    except Exception:
        return None

def read_sql_products(db_path, id_value=None):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        if id_value is not None:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id=?", (id_value,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        # Convert to list of dicts (header: id, name, category, price)
        products = [
            {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
            for row in rows
        ]
        return products
    except Exception:
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    error_msg = None
    products = []

    if source == 'json':
        products = read_json_products('products.json')
    elif source == 'csv':
        products = read_csv_products('products.csv')
    elif source == 'sql':
        # We must convert id_param to int if used
        if id_param:
            try:
                id_value = int(id_param)
            except Exception:
                error_msg = "Invalid id parameter."
                return render_template("product_display.html", error=error_msg, products=None)
        else:
            id_value = None
        products = read_sql_products('products.db', id_value)
    else:
        error_msg = "Wrong source"
        return render_template("product_display.html", error=error_msg, products=None)

    if products is None:
        if source == 'sql':
            error_msg = f"Could not query database."
        else:
            error_msg = f"Could not read {source} data."
        return render_template("product_display.html", error=error_msg, products=None)

    # For JSON and CSV, handle id filtering here
    if source in ('json', 'csv') and id_param:
        try:
            id_value = int(id_param)
        except Exception:
            error_msg = "Invalid id parameter."
            return render_template("product_display.html", error=error_msg, products=None)
        filtered = [prod for prod in products if int(prod.get('id', -1)) == id_value]
        if not filtered:
            error_msg = "Product not found"
            return render_template("product_display.html", error=error_msg, products=None)
        else:
            products = filtered

    # For SQL, if we asked for id and no product was found...
    if source == 'sql' and id_param and len(products) == 0:
        error_msg = "Product not found"
        return render_template("product_display.html", error=error_msg, products=None)

    return render_template("product_display.html", error=None, products=products)

if __name__ == "__main__":
    app.run(debug=True, port=5000)