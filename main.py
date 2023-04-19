import os
import pandas as pd
import requests
import yaml
from naming.column_name import ColumnName
from order import Order
from os_tools import find_exl_file_in_dir
from xl_reports import export_sum, export_deliveries, make_total_report
from oreders_doc import make_orders_doc


def get_store_config(path="store_config.yaml") -> dict:
    with open(path, "r") as f:
        t = yaml.safe_load(f)
    return t


def get_products(web_token: str) -> dict:
    """return products name and price by id aka sku"""
    products = {}
    page = 1
    while True:
        page_products = load_products_page(istores_token=web_token, api=f"/products/100/{page}")
        products.update(page_products)
        page += 1

        if len(page_products) < 100:
            break
    print(f"got a total of {len(products)} products")
    return products


def load_products_page(istores_token: str, gw: str = "https://api.istores.co.il",
                       api: str = "/products/100/1") -> dict:
    """return products name and price by id from the given URL"""
    print(f"getting products from {api}, this might take a while...")
    response = requests.get(gw + api, headers={'x-token': istores_token})
    products = {}
    if response.status_code != 200:
        raise ConnectionError("can't connect to istores swg, please try to connect manually")
    raw: list[dict] = response.json().get('products')

    for product in raw:
        sku = product.get('sku')
        if not products.get(sku):
            products[product.get('sku')] = {'name': product.get('product_description').get('3').get('name'),
                                            'price': float(product.get('price')),
                                            }
        else:

            # print(f"You need to fix products DB, dabble sku: {sku} !")
            raise ValueError(f"You need to fix products DB, dabble sku: {sku},"
                             f"{products.get(sku)}"
                             f" {product.get('product_description').get('3').get('name')}!")
    print("successfully load  products from the Web")
    return products


def load_xl(file_name: str) -> pd.DataFrame:
    try:
        xl = pd.ExcelFile(file_name)
    except FileNotFoundError:
        raise FileNotFoundError(f"file name: [{file_name}], is not in [{os.getcwd()}] ")
    return xl.parse(xl.sheet_names[0], converters={ColumnName.PHONE.value: str,
                                                   })


def make_orders(df: pd.DataFrame, products: dict) -> list[Order]:
    orders = []

    for order_id, group in df.groupby(ColumnName.ORDER_NUM.value):
        order = Order(order_id, group, products_t=products)
        orders.append(order)
    print(f"Total orders: {len(orders)}, for the report")
    return orders


def make_report(file_name: str, web_token: str, is_holiday_store: bool):
    df = load_xl(file_name)

    products = get_products(web_token)

    orders = make_orders(df, products)

    # creating XL reports
    export_deliveries(orders)
    export_sum(orders)
    make_total_report(df, is_holiday_store)

    # creating word document
    make_orders_doc(orders)
    print("DONE!")


if __name__ == '__main__':
    store = get_store_config()
    orders_file_path = find_exl_file_in_dir()
    make_report(file_name=orders_file_path, web_token=store.get("token"), is_holiday_store=store.get("is_holiday"))
