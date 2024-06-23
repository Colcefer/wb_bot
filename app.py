from flask import Flask, jsonify, render_template, request
from database import Database
from datetime import datetime

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


def filter_sales_by_date(sales, start_date, end_date):
    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        sales = [sale for sale in sales if datetime.strptime(sale['date'], '%Y-%m-%dT%H:%M:%S').date() >= start_date]
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        sales = [sale for sale in sales if datetime.strptime(sale['date'], '%Y-%m-%dT%H:%M:%S').date() <= end_date]
    return sales


@app.route('/api/sales', methods=['GET'])
def get_sales():
    db = Database()
    sales = db.get_all_sales()
    db.close()

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if start_date or end_date:
        sales = filter_sales_by_date(sales, start_date, end_date)

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
    app.run(debug=True, port=8080)
