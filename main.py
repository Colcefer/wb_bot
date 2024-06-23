import requests
from models import StockItem
from database import Database


def fetch_data(api_url):
    import requests

    payload = {}
    headers = {
        'Authorization': ''
    }

    response = requests.request("GET", api_url, headers=headers, data=payload)

    return response.json()


def main():
    api_url = "https://statistics-api.wildberries.ru/api/v1/supplier/stocks?dateFrom=2023-06-20T00:00:00"
    data = fetch_data(api_url)
    api_url = "https://statistics-api.wildberries.ru/api/v1/supplier/orders"
    orders = fetch_data(api_url)

    db = Database()

    for item in data:
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

    db.close()


if __name__ == "__main__":
    main()
