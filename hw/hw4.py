class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def change_price(self, new_price):
        self.price = new_price

    def change_quantity(self, new_quantity):
        self.quantity = new_quantity


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

class Order:
    def __init__(self):
        self.products = []
        self.total_price = 0

    def add_product(self, product):
        self.products.append(product)
        self.total_price += product.price * product.quantity

    def calculate_total_price(self):
        return self.total_price


products = []
customers = []
order = Order()

with open('hw4list.txt', "r", encoding="utf-8") as file:

    for line in file:
        parts = line.strip().split(";")

        if parts[0] == 'product':
            name = parts[1]
            category = parts[2]
            price = int(parts[3])
            quantity = int(parts[4])


            product = Product(name, category, price, quantity)

            products.append(product)
            order.add_product(product)

        elif parts[0] == 'customer':
            name = parts[1]
            email = parts[2]

            customer = Customer(name, email)

            customers.append(customer)


print('-----Клієнти----')
for customer in customers:
    print(f'Name: {customer.name}, Email: {customer.email}')

print('-----Товар----')
for product in products:
    print(f'Product: {product.name}, Category: {product.category}, Price: {product.price}$, Quantity: {product.quantity}')
print(f'Total price: {order.total_price}$')