from flask import Flask, jsonify, render_template
from database import Database
from fetch_data import main as fetch_data_main

app = Flask(__name__)

@app.route('/api/stocks', methods=['GET'])
def get_stocks():
    db = Database()
    stocks = db.get_all_stock_items()
    db.close()
    return jsonify(stocks)

@app.route('/api/orders', methods=['GET'])
def get_orders():
    db = Database()
    orders = db.get_all_orders()
    db.close()
    return jsonify(orders)

@app.route('/api/sales', methods=['GET'])
def get_sales():
    db = Database()
    sales = db.get_all_sales()
    db.close()
    return jsonify(sales)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

if __name__ == "__main__":
    #fetch_data_main()
    app.run(debug=True, port=8080)
