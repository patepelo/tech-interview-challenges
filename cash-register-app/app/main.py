from checkout import Checkout
from products import load_products_from_csv

def main():
    # Load product data from CSV
    products = load_products_from_csv('data/products.csv')

    # Create a Checkout instance
    checkout = Checkout(products)

    while True:
        # Get user input for product codes
        user_products = input("Enter the product codes (comma-separated)").strip()



        # Enter product codes into the checkout system
        checkout.enter_codes(user_products)

        # Calculate the total price
        total = checkout.calculate_total()
        print(f"Total: {round(total,2)} €")

if __name__ == "__main__":
    main()
