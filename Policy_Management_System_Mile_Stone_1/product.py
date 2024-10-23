class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.status = 'Available'

    def update(self, new_name, new_price):
        self.name = new_name
        self.price = new_price
        print(f"Product {self.name} has been updated to {new_name} with a price of {new_price}.")

    def suspend(self):
        self.status = 'Suspended'
        print(f"Product {self.name} has been suspended.")
