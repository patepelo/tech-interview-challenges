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
