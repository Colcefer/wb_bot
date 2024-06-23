class StockItem:
    def __init__(self, last_change_date, warehouse_name, supplier_article, nm_id, barcode, quantity,
                 in_way_to_client, in_way_from_client, quantity_full, category, subject, brand,
                 tech_size, price, discount, is_supply, is_realization, sc_code):
        self.last_change_date = last_change_date
        self.warehouse_name = warehouse_name
        self.supplier_article = supplier_article
        self.nm_id = nm_id
        self.barcode = barcode
        self.quantity = quantity
        self.in_way_to_client = in_way_to_client
        self.in_way_from_client = in_way_from_client
        self.quantity_full = quantity_full
        self.category = category
        self.subject = subject
        self.brand = brand
        self.tech_size = tech_size
        self.price = price
        self.discount = discount
        self.is_supply = is_supply
        self.is_realization = is_realization
        self.sc_code = sc_code

class Order:
    def __init__(self, date, last_change_date, warehouse_name, country_name, oblast_okrug_name, region_name,
                 supplier_article, nm_id, barcode, category, subject, brand, tech_size, income_id, is_supply,
                 is_realization, total_price, discount_percent, spp, finished_price, price_with_disc, is_cancel,
                 cancel_date, order_type, sticker, g_number, srid):
        self.date = date
        self.last_change_date = last_change_date
        self.warehouse_name = warehouse_name
        self.country_name = country_name
        self.oblast_okrug_name = oblast_okrug_name
        self.region_name = region_name
        self.supplier_article = supplier_article
        self.nm_id = nm_id
        self.barcode = barcode
        self.category = category
        self.subject = subject
        self.brand = brand
        self.tech_size = tech_size
        self.income_id = income_id
        self.is_supply = is_supply
        self.is_realization = is_realization
        self.total_price = total_price
        self.discount_percent = discount_percent
        self.spp = spp
        self.finished_price = finished_price
        self.price_with_disc = price_with_disc
        self.is_cancel = is_cancel
        self.cancel_date = cancel_date
        self.order_type = order_type
        self.sticker = sticker
        self.g_number = g_number
        self.srid = srid

class Sale:
    def __init__(self, date, last_change_date, warehouse_name, country_name, oblast_okrug_name, region_name,
                 supplier_article, nm_id, barcode, category, subject, brand, tech_size, income_id, is_supply,
                 is_realization, total_price, discount_percent, spp, payment_sale_amount, for_pay, finished_price,
                 price_with_disc, sale_id, order_type, sticker, g_number, srid):
        self.date = date
        self.last_change_date = last_change_date
        self.warehouse_name = warehouse_name
        self.country_name = country_name
        self.oblast_okrug_name = oblast_okrug_name
        self.region_name = region_name
        self.supplier_article = supplier_article
        self.nm_id = nm_id
        self.barcode = barcode
        self.category = category
        self.subject = subject
        self.brand = brand
        self.tech_size = tech_size
        self.income_id = income_id
        self.is_supply = is_supply
        self.is_realization = is_realization
        self.total_price = total_price
        self.discount_percent = discount_percent
        self.spp = spp
        self.payment_sale_amount = payment_sale_amount
        self.for_pay = for_pay
        self.finished_price = finished_price
        self.price_with_disc = price_with_disc
        self.sale_id = sale_id
        self.order_type = order_type
        self.sticker = sticker
        self.g_number = g_number
        self.srid = srid
