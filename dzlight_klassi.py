class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price


class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"Customer(name={self.name}, orders={len(self.orders)})"

    def __repr__(self):
        return f"Customer(name={self.name}, orders={len(self.orders)})"


class Order:
    total_orders = 0
    total_amount = 0

    def __init__(self, products, discount=None):
        self.products = products
        self.discount = discount
        Order.total_orders += 1
        Order.total_amount += self.calculate_total()

    def calculate_total(self):
        total = sum(product.price for product in self.products)
        if self.discount:
            total = self.discount.apply_discount(total)
        return total

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders

    @classmethod
    def get_total_amount(cls):
        return cls.total_amount

    def __str__(self):
        return f"Order(products={self.products}, total={self.calculate_total()})"

    def __repr__(self):
        return f"Order(products={self.products}, total={self.calculate_total()})"


class Discount:
    def __init__(self, description, discount_percent):
        self.description = description
        self.discount_percent = discount_percent

    def apply_discount(self, total):
        return total * (1 - self.discount_percent / 100)

    @staticmethod
    def seasonal_discount(total):
        return total * 0.9  # 10% сезонная скидка

    @staticmethod
    def promo_code_discount(total):
        return total * 0.85  # 15% скидка по промокоду

    def __str__(self):
        return f"Discount(description={self.description}, discount_percent={self.discount_percent}%)"

    def __repr__(self):
        return f"Discount(description={self.description}, discount_percent={self.discount_percent}%)"


# Создание продуктов
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)
product3 = Product("Headphones", 100)

# Создание клиентов
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Создание скидок
seasonal_discount = Discount("Seasonal Discount", 10)
promo_discount = Discount("Promo Code Discount", 15)

# Создание заказов
order1 = Order([product1, product2], seasonal_discount)
order2 = Order([product2, product3], promo_discount)
order3 = Order([product1, product3])

# Добавление заказов клиентам
customer1.add_order(order1)
customer1.add_order(order2)
customer2.add_order(order3)

# Вывод информации о клиентах, заказах и продуктах
print(customer1)
print(customer2)
print(order1)
print(order2)
print(order3)
print(product1)
print(product2)
print(product3)

# Подсчет общего количества заказов и общей суммы
print(f"Total orders: {Order.get_total_orders()}")
print(f"Total amount: {Order.get_total_amount()}")

