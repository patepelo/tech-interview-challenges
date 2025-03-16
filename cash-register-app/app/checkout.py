# This file is for handling the logic of the functions:
# 1. Store a list of scanned products.
# 2. Apply discounts dynamically.
# 3. Calculate the correct total price.

from app.products import load_products_from_csv

class Checkout:
    def __init__(self, products):
        """Initialize checkout system with product data"""
        self.products = products
        self.cart = {}

    def enter_codes(self, product_codes):
        """Scan one or multiple product codes (comma-separated) and add them to the cart."""

        # Ensure input is a string and split by commas
        items = [code.strip().upper() for code in product_codes.split(",")]

        for product_code in items:
            if product_code in self.products:
                self.cart[product_code] = self.cart.get(product_code, 0) + 1
            else:
                raise ValueError(f"Product {product_code} not found.")

    def apply_discounts(self):
        """Applies discounts before calculating total"""
        total_discount = 0
        for product_code, quantity in self.cart.items():
            product = self.products[product_code]

            # Buy 2 get 1 free and similars
            if quantity >= product["product_discount_minimum"] and product["discount_type"] == "free_item_discount":
                free_items = quantity // (product["product_discount_minimum"] + 1)
                total_discount += free_items * product["product_price"]

            # Price discount
            elif quantity >= product["product_discount_minimum"] and product["discount_type"] == "price_discount":
                total_discount += (product["product_price"] - product["product_discount_price"]) * quantity

            # Percentage discount
            elif quantity >= product["product_discount_minimum"] and product["discount_type"] == "percentage_discount":
                total_discount += product["product_price"] * product["product_discount_percentage"] * quantity
        print(total_discount)
        return total_discount

    def calculate_total(self):
        """Calculates the final total after applying discounts"""
        total_price = 0

        for product_code, quantity in self.cart.items():
            product = self.products[product_code]
            total_price += quantity * product["product_price"]

        total_discount = self.apply_discounts()
        total = total_price - total_discount

        return round(total, 2)

# Test the functionality
if __name__ == "__main__":
    products = load_products_from_csv('data/products.csv')
    checkout = Checkout(products)
    checkout.enter_codes("GR1,SR1,GR1,GR1,CF1")
    total = checkout.calculate_total()
    print(f"Test GR1,SR1,GR1,GR1,CF1 (should: 30.57)/ is: {total}")

if __name__ == "__main__":
    products = load_products_from_csv('data/products.csv')
    checkout = Checkout(products)
    checkout.enter_codes("GR1, GR1")
    total = checkout.calculate_total()
    print(f"Test GR1, GR1 (should: 3.11)/ is: {total}")
