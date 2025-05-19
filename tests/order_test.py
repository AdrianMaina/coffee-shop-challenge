import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):

    def test_valid_order(self):
        customer = Customer("John")
        coffee = Coffee("Americano")
        order = Order(customer, coffee, 5.0)

        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.0)

    def test_invalid_customer(self):
        coffee = Coffee("Cappuccino")
        with self.assertRaises(TypeError):
            Order("NotACustomer", coffee, 4.0)

    def test_invalid_coffee(self):
        customer = Customer("Ella")
        with self.assertRaises(TypeError):
            Order(customer, "NotACoffee", 4.0)

    def test_invalid_price_type(self):
        customer = Customer("Leo")
        coffee = Coffee("Latte")
        with self.assertRaises(TypeError):
            Order(customer, coffee, "5")

    def test_invalid_price_range(self):
        customer = Customer("Zoe")
        coffee = Coffee("Latte")
        with self.assertRaises(ValueError):
            Order(customer, coffee, 0.5)

        with self.assertRaises(ValueError):
            Order(customer, coffee, 15.0)

    def test_price_immutable(self):
        customer = Customer("Max")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 3.0)
        with self.assertRaises(AttributeError):
            order.price = 6.0

if __name__ == '__main__':
    unittest.main()
