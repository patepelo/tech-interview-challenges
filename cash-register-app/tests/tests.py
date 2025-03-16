import pytest

from app.products import load_products_from_csv
from app.checkout import Checkout
#Test data
# Load product data from CSV
PRODUCTS = load_products_from_csv("data/products.csv")

def test_buy_one_get_one_free():
    '''Test case: GR1,GR1'''

    assert Checkout.total() == 3.11

def test_strawberry_bulk_discount():
    '''Test case: SR1,SR1,GR1,SR1'''

    assert Checkout.total() == 16.61

def test_coffee_quantity_discount():
    '''Test case: GR1,CF1,SR1,CF1,CF1'''

    assert Checkout.total() == 30.57
