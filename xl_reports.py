import pandas
import pandas as pd
from collections import defaultdict
from naming.column_name import ColumnName
from order import Order


def export_deliveries(orders: list[Order], f_name: str = "deliveries.xlsx"):
    orders_type = defaultdict(int)
    for order in orders:
        orders_type[order.order_type] += 1
    df = pd.DataFrame(orders_type, index=[0]).T
    df.to_excel(f_name)
    print(f"deliveries report is done\nresults are at: {f_name}")


def export_sum(orders: list[Order], f_name: str = "sum.xlsx"):
    summery = dict(order_id=[],
                   name=[],
                   phone=[],
                   city=[],
                   address=[],
                   order_type=[],
                   comment=[])

    for order in orders:
        summery["order_id"].append(order.id)
        summery["name"].append(order.name)
        summery["phone"].append(order.phone)
        summery["city"].append(order.city)
        summery["address"].append(order.address)
        summery["order_type"].append(order.order_type)
        summery["comment"].append(order.comment)
    df = pd.DataFrame(summery)
    df.to_excel(f_name)
    print(f"summery report is done\nresults are at: {f_name}")


def make_total_report(df: pandas.DataFrame, is_holiday_store: bool = False):
    """make the total product/ packages  report """
    total_product = []
    if is_holiday_store:  # in holiday all products coms in one package
        for what, product in df.groupby([ColumnName.PRODUCT_ID.value]):
            total = {'product_name': product.iloc[0][ColumnName.ITEM.value],
                     'product_sum': product[[ColumnName.AMOUNT.value]].sum()[0]}
            total_product.append(total)

    else:
        for what, product in df.groupby([ColumnName.PRODUCT_ID.value, ColumnName.PACKAGE.value]):
            total = {'product_name': product.iloc[0][ColumnName.ITEM.value],
                     'package': product.iloc[0][ColumnName.PACKAGE.value].split(':')[-1],
                     'product_sum': product[[ColumnName.AMOUNT.value]].sum()[0]}
            total_product.append(total)
            print(product.iloc[0][ColumnName.PACKAGE.value].split(':')[-1])
    total_df = pd.DataFrame(total_product)
    total_df.to_excel("total_packs.xlsx")
