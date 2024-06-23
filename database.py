import sqlite3


class Database:
    def __init__(self, db_name="wildberries.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS stocks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                last_change_date TEXT,
                warehouse_name TEXT,
                supplier_article TEXT,
                nm_id INTEGER,
                barcode TEXT,
                quantity INTEGER,
                in_way_to_client INTEGER,
                in_way_from_client INTEGER,
                quantity_full INTEGER,
                category TEXT,
                subject TEXT,
                brand TEXT,
                tech_size TEXT,
                price REAL,
                discount REAL,
                is_supply BOOLEAN,
                is_realization BOOLEAN,
                sc_code TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                last_change_date TEXT,
                warehouse_name TEXT,
                country_name TEXT,
                oblast_okrug_name TEXT,
                region_name TEXT,
                supplier_article TEXT,
                nm_id INTEGER,
                barcode TEXT,
                category TEXT,
                subject TEXT,
                brand TEXT,
                tech_size TEXT,
                income_id INTEGER,
                is_supply BOOLEAN,
                is_realization BOOLEAN,
                total_price REAL,
                discount_percent INTEGER,
                spp INTEGER,
                finished_price REAL,
                price_with_disc REAL,
                is_cancel BOOLEAN,
                cancel_date TEXT,
                order_type TEXT,
                sticker TEXT,
                g_number TEXT,
                srid TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                last_change_date TEXT,
                warehouse_name TEXT,
                country_name TEXT,
                oblast_okrug_name TEXT,
                region_name TEXT,
                supplier_article TEXT,
                nm_id INTEGER,
                barcode TEXT,
                category TEXT,
                subject TEXT,
                brand TEXT,
                tech_size TEXT,
                income_id INTEGER,
                is_supply BOOLEAN,
                is_realization BOOLEAN,
                total_price REAL,
                discount_percent INTEGER,
                spp INTEGER,
                payment_sale_amount REAL,
                for_pay REAL,
                finished_price REAL,
                price_with_disc REAL,
                sale_id TEXT,
                order_type TEXT,
                sticker TEXT,
                g_number TEXT,
                srid TEXT
            )
        ''')
        self.connection.commit()

    def insert_stock_item(self, stock_item):
        self.cursor.execute('''
            INSERT INTO stocks (last_change_date, warehouse_name, supplier_article, nm_id, barcode, quantity, 
                                in_way_to_client, in_way_from_client, quantity_full, category, subject, brand, 
                                tech_size, price, discount, is_supply, is_realization, sc_code)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (stock_item.last_change_date, stock_item.warehouse_name, stock_item.supplier_article, stock_item.nm_id,
              stock_item.barcode, stock_item.quantity, stock_item.in_way_to_client, stock_item.in_way_from_client,
              stock_item.quantity_full, stock_item.category, stock_item.subject, stock_item.brand,
              stock_item.tech_size, stock_item.price, stock_item.discount, stock_item.is_supply,
              stock_item.is_realization, stock_item.sc_code))
        self.connection.commit()

    def insert_order(self, order):
        self.cursor.execute('''
            INSERT INTO orders (date, last_change_date, warehouse_name, country_name, oblast_okrug_name, region_name,
                                supplier_article, nm_id, barcode, category, subject, brand, tech_size, income_id, 
                                is_supply, is_realization, total_price, discount_percent, spp, finished_price, 
                                price_with_disc, is_cancel, cancel_date, order_type, sticker, g_number, srid)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (order.date, order.last_change_date, order.warehouse_name, order.country_name, order.oblast_okrug_name,
              order.region_name, order.supplier_article, order.nm_id, order.barcode, order.category, order.subject,
              order.brand, order.tech_size, order.income_id, order.is_supply, order.is_realization, order.total_price,
              order.discount_percent, order.spp, order.finished_price, order.price_with_disc, order.is_cancel,
              order.cancel_date, order.order_type, order.sticker, order.g_number, order.srid))
        self.connection.commit()

    def insert_sale(self, sale):
        self.cursor.execute('''
            INSERT INTO sales (date, last_change_date, warehouse_name, country_name, oblast_okrug_name, region_name,
                               supplier_article, nm_id, barcode, category, subject, brand, tech_size, income_id,
                               is_supply, is_realization, total_price, discount_percent, spp, payment_sale_amount,
                               for_pay, finished_price, price_with_disc, sale_id, order_type, sticker, g_number, srid)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (sale.date, sale.last_change_date, sale.warehouse_name, sale.country_name, sale.oblast_okrug_name,
              sale.region_name, sale.supplier_article, sale.nm_id, sale.barcode, sale.category, sale.subject,
              sale.brand, sale.tech_size, sale.income_id, sale.is_supply, sale.is_realization, sale.total_price,
              sale.discount_percent, sale.spp, sale.payment_sale_amount, sale.for_pay, sale.finished_price,
              sale.price_with_disc, sale.sale_id, sale.order_type, sale.sticker, sale.g_number, sale.srid))
        self.connection.commit()

    def get_all_stock_items(self):
        self.cursor.execute('SELECT * FROM stocks')
        return self.cursor.fetchall()

    def get_all_orders(self):
        self.cursor.execute('SELECT * FROM orders')
        return self.cursor.fetchall()

    def get_all_sales(self):
        query = "SELECT id, date, last_change_date, warehouse_name, country_name, oblast_okrug_name, region_name, supplier_article, nm_id, barcode, category, subject, brand, tech_size, income_id, is_supply, is_realization, total_price, discount_percent, spp, payment_sale_amount, for_pay, finished_price, price_with_disc, sale_id, order_type, sticker, g_number, srid FROM sales"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        sales = [
            {
                'id': row[0],
                'date': row[1],
                'last_change_date': row[2],
                'warehouse_name': row[3],
                'country_name': row[4],
                'oblast_okrug_name': row[5],
                'region_name': row[6],
                'supplier_article': row[7],
                'nm_id': row[8],
                'barcode': row[9],
                'category': row[10],
                'subject': row[11],
                'brand': row[12],
                'tech_size': row[13],
                'income_id': row[14],
                'is_supply': row[15],
                'is_realization': row[16],
                'total_price': row[17],
                'discount_percent': row[18],
                'spp': row[19],
                'payment_sale_amount': row[20],
                'for_pay': row[21],
                'finished_price': row[22],
                'price_with_disc': row[23],
                'sale_id': row[24],
                'order_type': row[25],
                'sticker': row[26],
                'g_number': row[27],
                'srid': row[28]
            }
            for row in rows
        ]
        return sales

    def close(self):
        self.connection.close()
