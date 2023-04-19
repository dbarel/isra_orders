from enum import Enum


class ColumnName(Enum):
    ORDER_NUM = "מס הזמנה"

    # header
    NAME = "שם לקוח"
    DATE = "תאריך"
    EMAIL = "אימייל"
    PHONE = "טלפון"
    TOTAL = "סה״כ תשלום"
    ORDER_TYPE = "סוג משלוח"
    ADDRESS = "כתובת המשלם"
    CITY = "עיר המשלם"
    STATUS = "סטטוס"
    COMMENT = "הערה"
    APPROVAL_ID = "מספר אישור"
    CREDIT_NUM = "4 ספרות של הכרטיס"

    # item
    ITEM = "פריטים בהזמנה"
    PACKAGE = "אפשרויות מוצר"
    AMOUNT = "כמות פריטים"
    PRODUCT_ID = "מק''ט"
