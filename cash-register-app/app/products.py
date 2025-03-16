import pandas as pd
import os

# Construct the absolute path to the CSV file
current_dir = os.path.dirname(__file__)
path = os.path.join(current_dir, "data/products.csv")

# Print the path to verify it
print(f"Loading data from: {path}")

def load_products_from_csv(file_path=path):
    """Load products and discounts applied from CSV into a pandas DataFrame and return as a dictionary"""

    # Create dataframe from CSV
    df = pd.read_csv(file_path)

    # Convert DataFrame to dictionary for easy lookup
    products = df.set_index("product_code").to_dict(orient="index")

    return products

# Call the function
load_products_from_csv(path)
