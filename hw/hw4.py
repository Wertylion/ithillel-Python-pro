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


class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product, qty):
        if qty > product.quantity:
            print(f"Недостатньо товару '{product.name}'")
            return
        product.quantity -= qty
        self.products.append({"product": product, "qty": qty})

    def calculate_total_price(self):
        total = 0
        for item in self.products:
            total += item["product"].price * item["qty"]
        return total


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self):
        order = Order()
        self.orders.append(order)
        return order


products = []
customers = []

with open('hw4list.txt', "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(";")

        if parts[0] == 'product':
            product = Product(parts[1], parts[2], int(parts[3]), int(parts[4]))
            products.append(product)

        elif parts[0] == 'customer':
            customer = Customer(parts[1], parts[2])
            customers.append(customer)

        elif parts[0] == 'order':
            customer_name, product_name, qty = parts[1], parts[2], int(parts[3])

            customer = None
            for c in customers:
                if c.name == customer_name:
                    customer = c
                    break

            product = None
            for p in products:
                if p.name == product_name:
                    product = p
                    break

            if customer is None:
                print(f"Клієнта '{customer_name}' не знайдено")
                continue
            if product is None:
                print(f"Товар '{product_name}' не знайдено")
                continue

            order = customer.add_order()
            order.add_product(product, qty)


print('-----Клієнти-----')
for customer in customers:
    total = sum(o.calculate_total_price() for o in customer.orders)
    print(f'Name: {customer.name}, Email: {customer.email}, Orders: {len(customer.orders)}, Total: {total} грн')

print('\n-----Товари-----')
for product in products:
    print(f'Product: {product.name}, Category: {product.category}, Price: {product.price} $, Stock: {product.quantity}')