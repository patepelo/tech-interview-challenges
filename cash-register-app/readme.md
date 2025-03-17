# Coding Challenge: Cash Register

## Objective
Build a simple and flexible cash register application that:
- Allows adding products to a cart
- Calculates the total price, considering special promotions
- Is maintainable, and easy to extend



## Pricing Rules and Promotions
- Products may have 2x1 discounts, bulk discounts in the form of percentage or general price discount
- The checkout system should handle items in any order
- Pricing rules should be easy to modify


## Example prices

| Product Code | Name         | Price  |
|-------------|-------------|--------|
| GR1         | Green Tea   | 3.11€  |
| SR1         | Strawberries | 5.00€  |
| CF1         | Coffee      | 11.23€ |

## Tests
- Use TDD methodology, meaning tests will be written before in order to ensure code correctness from the start
- Test data will be added to compare results

# App Structure
- The app is based on a simple .csv file the marketing team can easily edit
- products.py logic reads from that .csv and converts to a dictionary
- checkout.py encompanses the logic of discount rules and evaluating inputed strings to calculate the total
- main.py runs the app and a simple interface in the console to interact with the user
- tests/test.py is based on the pytest library for structuring tests. It has been added 5 basic tests, but could be added more to ensure correct functionality, for example evaluate wether the csv file is well structured after marketing edits.
- setup.py is to facilitate the first time setup in a different environment

## Requirements
- The app is light and only needs the few libraries listed in requirement.txt, pandas could be avoided and a different method could be used to import csv to dictionaries but it's not critical since pandas is robust and well supported.

## Setup

- Consider creating a new Python Virtual Environment, although it shouldn't be that necessary due to the current simplicity of the app.
- Use setup.py to run from there and install the necessary packages and dependencies if you don't want to install manually. Use:
```sh
pip install .
```
- Run Tests to ensure everything works in the new environment
```sh
python tests/tests.py
```

# Next Steps (optional)
- Create a receipt generator with details, see:
  - https://dev.to/spiff/build-a-product-receipt-generator-using-python-49nm?utm_source=chatgpt.com
  - https://www.geeksforgeeks.org/creating-a-receipt-calculator-using-python/
- Create a web app interface with Streamlit or Flask
