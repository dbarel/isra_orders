import pandas as pd

from naming import Heb
from naming.column_name import ColumnName
from naming.oredr_types import OrderTypes
from naming.package import Package


class Order:
    def __init__(self, order_id: int, df: pd.DataFrame, products_t: dict):
        """Order details,  personal customer information and shopping cart"""
        self.id = order_id
        self.name = df[ColumnName.NAME.value].iloc[0]
        self.email = df[ColumnName.EMAIL.value].iloc[0]
        self.phone = df[ColumnName.PHONE.value].iloc[0]
        self.date = df[ColumnName.DATE.value].iloc[0]
        self.comment = df[ColumnName.COMMENT.value].iloc[0]
        self.total = df[ColumnName.TOTAL.value].iloc[0]
        self.status = df[ColumnName.STATUS.value].iloc[0]
        self.credit = df[ColumnName.CREDIT_NUM.value].iloc[0]

        self.order_type = df[ColumnName.ORDER_TYPE.value].iloc[0]
        self.address = df[ColumnName.ADDRESS.value].iloc[0]
        self.city = df[ColumnName.CITY.value].iloc[0]
        self.approval_id = df[ColumnName.APPROVAL_ID.value].iloc[0]

        self.products_t = products_t

        self.produces = []
        for _, row in df.iterrows():
            self.pars_item(row)

    def pars_item(self, row):
        """add shopping item to  produces"""
        product_id = str(int(row[ColumnName.PRODUCT_ID.value]))

        try:
            product_name = self.products_t.get(product_id).get('name')
        except AttributeError:
            print(f"new product: {product_id} found you'll need to add the new json file")
            raise AttributeError(f"new product: {product_id} found you'll need to update the json file!")

        base_price = self.products_t.get(product_id).get('price')
        amount = row[ColumnName.AMOUNT.value]
        package = row[ColumnName.PACKAGE.value]
        if pd.isnull(package):
            package = Package.u
        else:
            package = package.split(':')[-1]
        unit_price = base_price * Package().package_factor(package)
        total = unit_price * amount
        self.produces.append([product_name, package, unit_price, amount, total])

    def has_credit(self) -> str:
        """:return if there credit card information"""
        if pd.isnull(self.credit):
            return f"{Heb.credit} {Heb.not_entered}"
        else:
            return f"{Heb.credit} {Heb.entered}"

    def to_dict(self) -> dict:
        """format order to be readable by xl_to_doc"""
        order = dict()
        order['title'] = f"""{Heb.status}: {self.status}
                            {self.has_credit()}
                            {Heb.delivery_method}: {self.order_type}
                            {Heb.name}: {self.name}
                            {Heb.phone}: {self.phone}"""
        order["is_delivery"] = OrderTypes().is_delivery(self.order_type)

        if order["is_delivery"]:
            order['address'] = f"{Heb.address}: {self.address}"
            self.produces.append([f"{Heb.delivery}", "", "", "1", "25"])
        if not pd.isnull(self.comment):
            order['comment'] = f"{Heb.comment} : {self.comment}"
        order['total'] = self.total
        self.produces.append([f'{Heb.total}', "", "", "", f"{self.total}"])
        order['produces'] = self.produces

        return order
