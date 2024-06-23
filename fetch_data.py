import requests
from models import StockItem, Order, Sale
from database import Database

def fetch_data(api_url, headers):
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjQwNTA2djEiLCJ0eXAiOiJKV1QifQ'
                         '.eyJlbnQiOjEsImV4cCI6MTczNDM5MzU0NiwiaWQiOiJiNDIzNzAyNi1hZDlmLTQ5ODAtODc3Ni1kMTNm'
                         'YTU5NTgxZmIiLCJpaWQiOjEwNTc4ODU5NCwib2lkIjoxMjI2MjExLCJzIjoxMDczNzQ1OTE4LCJzaWQiOiJl'
                         'ZDM0MWMwOS0xNzFiLTQ3OWUtODM1NC0wNjk4ZjU3MzJhNmUiLCJ0IjpmYWxzZSwidWlkIjoxMDU3ODg1OTR9.Q'
                         '6M2rBUOHQI1WpUWiNnnxoIk6oCAgx5HurWQST5H8XaALNJIEjQwzNB38bpfL2rIv5q8K4nXzI7FmHc8Pexkcg '
    }

    stocks_url = "https://statistics-api.wildberries.ru/api/v1/supplier/stocks?dateFrom=2023-06-20T00:00:00"
    orders_url = "https://statistics-api.wildberries.ru/api/v1/supplier/orders?dateFrom=2023-06-20T00:00:00"
    sales_url = "https://statistics-api.wildberries.ru/api/v1/supplier/sales?dateFrom=2023-06-20T00:00:00"

    stocks_data = fetch_data(stocks_url, headers)
    orders_data = fetch_data(orders_url, headers)
    sales_data = fetch_data(sales_url, headers)

    db = Database()

    for item in stocks_data:
        stock_item = StockItem(
            last_change_date=item["lastChangeDate"],
            warehouse_name=item["warehouseName"],
            supplier_article=item["supplierArticle"],
            nm_id=item["nmId"],
            barcode=item["barcode"],
            quantity=item["quantity"],
            in_way_to_client=item["inWayToClient"],
            in_way_from_client=item["inWayFromClient"],
            quantity_full=item["quantityFull"],
            category=item["category"],
            subject=item["subject"],
            brand=item["brand"],
            tech_size=item["techSize"],
            price=item["Price"],
            discount=item["Discount"],
            is_supply=item["isSupply"],
            is_realization=item["isRealization"],
            sc_code=item["SCCode"]
        )
        db.insert_stock_item(stock_item)

    for item in orders_data:
        order = Order(
            date=item["date"],
            last_change_date=item["lastChangeDate"],
            warehouse_name=item["warehouseName"],
            country_name=item["countryName"],
            oblast_okrug_name=item["oblastOkrugName"],
            region_name=item["regionName"],
            supplier_article=item["supplierArticle"],
            nm_id=item["nmId"],
            barcode=item["barcode"],
            category=item["category"],
            subject=item["subject"],
            brand=item["brand"],
            tech_size=item["techSize"],
            income_id=item["incomeID"],
            is_supply=item["isSupply"],
            is_realization=item["isRealization"],
            total_price=item["totalPrice"],
            discount_percent=item["discountPercent"],
            spp=item["spp"],
            finished_price=item["finishedPrice"],
            price_with_disc=item["priceWithDisc"],
            is_cancel=item["isCancel"],
            cancel_date=item["cancelDate"],
            order_type=item["orderType"],
            sticker=item["sticker"],
            g_number=item["gNumber"],
            srid=item["srid"]
        )
        db.insert_order(order)

    for item in sales_data:
        sale = Sale(
            date=item["date"],
            last_change_date=item["lastChangeDate"],
            warehouse_name=item["warehouseName"],
            country_name=item["countryName"],
            oblast_okrug_name=item["oblastOkrugName"],
            region_name=item["regionName"],
            supplier_article=item["supplierArticle"],
            nm_id=item["nmId"],
            barcode=item["barcode"],
            category=item["category"],
            subject=item["subject"],
            brand=item["brand"],
            tech_size=item["techSize"],
            income_id=item["incomeID"],
            is_supply=item["isSupply"],
            is_realization=item["isRealization"],
            total_price=item["totalPrice"],
            discount_percent=item["discountPercent"],
            spp=item["spp"],
            payment_sale_amount=item["paymentSaleAmount"],
            for_pay=item["forPay"],
            finished_price=item["finishedPrice"],
            price_with_disc=item["priceWithDisc"],
            sale_id=item["saleID"],
            order_type=item["orderType"],
            sticker=item["sticker"],
            g_number=item["gNumber"],
            srid=item["srid"]
        )
        db.insert_sale(sale)

    db.close()

if __name__ == "__main__":
    main()
