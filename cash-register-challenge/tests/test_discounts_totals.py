import pytest
from app.cash_register.products import load_products_from_csv
from app.cash_register.checkout import Checkout

# Load product data from CSV
PRODUCTS = load_products_from_csv()

def test_buy_one_get_one_free():
    '''Test case: GR1,GR1'''
    input_test_string = "GR1, GR1"
    checkout = Checkout(PRODUCTS)
    checkout.enter_codes(input_test_string)
    total = checkout.calculate_total()
    assert total == 3.11


def test_strawberry_bulk_discount():
    '''Test case: SR1,SR1,GR1,SR1'''
    input_test_string = "SR1, SR1, GR1, SR1"
    checkout = Checkout(PRODUCTS)
    checkout.enter_codes(input_test_string)
    total = checkout.calculate_total()
    assert total == 16.61

def test_coffee_quantity_discount():
    '''Test case: GR1,CF1,SR1,CF1,CF1'''
    input_test_string = "GR1, CF1, SR1, CF1, CF1"
    checkout = Checkout(PRODUCTS)
    checkout.enter_codes(input_test_string)
    total = checkout.calculate_total()
    assert total == 30.57
