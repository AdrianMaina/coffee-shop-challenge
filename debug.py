from customer import Customer
from coffee import Coffee
from order import Order

def main():
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")

    # Create coffees
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    # Alice creates orders
    order1 = Order(alice, espresso, 3.5)
    order2 = Order(alice, latte, 4.0)

    # Bob creates an order
    order3 = Order(bob, espresso, 3.0)

    # Print customers and their orders
    print(f"{alice.name} orders: {[o.coffee.name for o in alice.orders()]}")
    print(f"{bob.name} orders: {[o.coffee.name for o in bob.orders()]}")

    # Print coffees and their customers
    print(f"{espresso.name} customers: {[c.name for c in espresso.customers()]}")
    print(f"{latte.name} customers: {[c.name for c in latte.customers()]}")

    # Print some aggregates
    print(f"Number of Espresso orders: {espresso.num_orders()}")
    print(f"Average price for Latte: {latte.average_price()}")

if __name__ == "__main__":
    main()
