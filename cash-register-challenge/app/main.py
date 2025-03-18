import os
from cash_register.checkout import Checkout
from cash_register.products import load_products_from_csv


BASE_DIR = os.path.dirname(os.path.realpath(__file__))  # This gives path to `app/`
DATA_PATH = os.path.join(BASE_DIR, "data", "products.csv")  # Correct path to CSV

print(f'Current data path is {DATA_PATH}')

products = load_products_from_csv(DATA_PATH)

# Create a Checkout instance
checkout = Checkout(products)



while True:


    # Get user input for product codes
    print("\n----------------------------------")
    user_products = input("Enter the product codes (comma-separated)").strip()



    # Enter product codes into the checkout system
    checkout.enter_codes(user_products)

    # Calculate the total price
    total = checkout.calculate_total()
    print("\n----------------------------------")
    print(f"Total: {round(total,2)} €")
    print("\n----------------------------------")
