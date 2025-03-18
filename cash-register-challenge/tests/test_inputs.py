import pytest
from app.cash_register.products import load_products_from_csv
from app.cash_register.checkout import Checkout

# Load product data from CSV
PRODUCTS = load_products_from_csv()

def test_invalid_product_code():
    '''Test case: Invalid product code'''
    checkout = Checkout(PRODUCTS)
    with pytest.raises(ValueError):
        checkout.enter_codes("INVALID")

def test_empty_cart():
    '''Test case: Empty cart'''
    checkout = Checkout(PRODUCTS)
    with pytest.raises(ValueError):
        checkout.enter_codes("")
