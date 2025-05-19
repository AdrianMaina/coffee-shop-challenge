import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):

    def test_valid_name(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            Customer(123)

    def test_invalid_name_length(self):
        with self.assertRaises(ValueError):
            Customer("A" * 16)

    def test_orders_and_coffees(self):
        c = Customer("Bob")
        latte = Coffee("Latte")
        mocha = Coffee("Mocha")
        c.create_order(latte, 4.5)
        c.create_order(mocha, 5.0)
        c.create_order(latte, 4.0)

        self.assertEqual(len(c.orders()), 3)
        self.assertIn(latte, c.coffees())
        self.assertIn(mocha, c.coffees())
        self.assertEqual(len(c.coffees()), 2)

if __name__ == '__main__':
    unittest.main()
