# 🛒 Coding Challenge: Cash Register

## 🏆 Objective
Build a simple and flexible cash register application that:
- Allows adding products to a cart
- Calculates the total price, considering special promotions
- Is maintainable, and easy to extend
- The checkout system must:
  - Handle items **in any order**.
  - Allow **easy modification of pricing rules**.

## 🎯 Pricing Rules and Promotions
- Products may have **Buy 1 Get 1 Free discounts**, **bulk discounts**, or **fixed price discounts**.
- The checkout system should handle items **in any order**.
- Pricing rules should be **easy to modify**.


## 🛒 Example Prices

| 🏷️ Product Code | 📦 Name         | 💰 Price  |
|---------------|-------------|--------|
| **GR1**       | 🍵 Green Tea   | **3.11€**  |
| **SR1**       | 🍓 Strawberries | **5.00€**  |
| **CF1**       | ☕ Coffee      | **11.23€**  |

## ✅ Tests
- The project should follow **Test-Driven Development (TDD)**, meaning **tests were written before** implementation.
- Test cases are included to validate **pricing logic, discount application, and error handling**.

# 🏗️ App Structure

- data/products.csv → Stores products and pricing details. The marketing team can edit this file easily.
- cash_register/products.py → Reads product data from .csv and converts it into a dictionary.
- cash_register/checkout.py → Handles discount rules and processes user input to calculate totals.
- cash_register/main.py → Runs the app and provides a simple console interface.
- tests/ → Contains unit tests for verifying the correctness of calculations. It has been added 5 basic tests, but could be added more to ensure correct functionality, for example evaluate wether the csv file is well structured after marketing edits.
- setup.py → Facilitates first-time installation in any environment.

## Requirements
- The app is light and only needs the few libraries listed in [requirements.txt](app/requirements.txt), pandas could be avoided and a different method could be used to import csv to dictionaries but it's not critical since pandas is robust and well supported.

## Setup and Running

- Consider creating a new Python Virtual Environment, although it shouldn't be that necessary due to the current simplicity of the app.

### Clone the Repository
```bash
git clone https://github.com/patepelo/tech-interview-challenges
cd cash-register-challenge
```

- Run the following command in the project root to install all dependencies from requirements.txt and install the package cash_register:
```sh
pip install .
```
- Make sure you to go to the cash-register-challenge location to run commands from there
- Run Tests to ensure everything works in the new environment
```sh
pytest tests/
```
- Alternatively, try this command to ensure Python finds the package:
```sh
PYTHONPATH=. pytest tests/
```

- After passing all the tests, you can run the code with:
```sh
python app/main.py
```


## 📜 Usage Instructions

Enter product codes separated by commas (e.g., GR1, SR1, CF1).
The app calculates the total price and applies discounts automatically.
If you enter a wrong code, the app will exit. This could be improved later.

# Next Steps (optional)
- Create a receipt generator with details, see:
  - https://dev.to/spiff/build-a-product-receipt-generator-using-python-49nm?utm_source=chatgpt.com
  - https://www.geeksforgeeks.org/creating-a-receipt-calculator-using-python/
- Create a web app interface with Streamlit or Flask
