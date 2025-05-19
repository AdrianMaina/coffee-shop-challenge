import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):

    def test_valid_name(self):
        c = Coffee("Espresso")
        self.assertEqual(c.name, "Espresso")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("Al")

    def test_add_orders_and_customers(self):
        c = Coffee("Latte")
        cust1 = Customer("Alice")
        cust2 = Customer("Bob")

        # Create orders
        order1 = Order(cust1, c, 4.5)
        order2 = Order(cust2, c, 5.0)
        order3 = Order(cust1, c, 4.0)

        # Link orders manually since Coffee doesn't create them
        c.orders().extend([order1, order2, order3])

        self.assertEqual(len(c.orders()), 3)
        self.assertEqual(set(c.customers()), {cust1, cust2})
        self.assertEqual(c.num_orders(), 3)
        self.assertAlmostEqual(c.average_price(), (4.5 + 5.0 + 4.0) / 3)

if __name__ == '__main__':
    unittest.main()
