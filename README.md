# coffee-shop-challenge
A Python-based object-oriented modeling project that simulates a coffee shop with customers, coffee types, and orders. The goal is to create classes with proper relationships, validations, and methods — tested using `pytest`.

## 📁 Project Structure

coffee-shop-challenge/
├── customer.py # Customer class
├── coffee.py # Coffee class
├── order.py # Order class
├── tests/
│ ├── customer_test.py # Unit tests for Customer
│ ├── coffee_test.py # Unit tests for Coffee
│ └── order_test.py # Unit tests for Order
├── README.md
└── requirements.txt # Dependencies

markdown
Copy
Edit


## 🧠 Key Concepts

- Object-Oriented Programming (OOP)
- Class Relationships
- Data Validation
- Aggregate Methods
- Unit Testing with `pytest`

## 📦 Classes

### `Customer`
- Attributes: `name`
- Methods:
  - `orders()`
  - `coffees()`
  - `create_order(coffee, price)`

### `Coffee`
- Attributes: `name`
- Methods:
  - `orders()`
  - `customers()`
  - `num_orders()`
  - `average_price()`

### `Order`
- Attributes: `customer`, `coffee`, `price`
- Validation:
  - `price`: must be a float between 1.0 and 10.0

## ✅ Testing

This project uses [`pytest`](https://docs.pytest.org/) for unit testing.

To run the test suite:

```bash
pytest -x
