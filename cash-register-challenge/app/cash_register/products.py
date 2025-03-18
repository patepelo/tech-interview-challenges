import pandas as pd
from pathlib import Path

# Define BASE_DIR at the correct package level (app/)
BASE_DIR = Path(__file__).resolve().parent.parent  # Moves up from cash_register/
DATA_PATH = BASE_DIR / "data" / "products.csv"  # Centralized path

def load_products_from_csv(file_path=None):
    """Load products and discounts applied from CSV into a pandas DataFrame and return as a dictionary"""

    file_path = file_path or DATA_PATH  # Use default unless overridden
    print(f"Loading product data from: {file_path}")

    # Create dataframe from CSV
    df = pd.read_csv(file_path)

    # Convert DataFrame to dictionary for easy lookup
    products = df.set_index("product_code").to_dict(orient="index")

    return products
