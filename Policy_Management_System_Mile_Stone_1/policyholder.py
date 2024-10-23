class Policyholder:
    def __init__(self, holder_id, name, status='Active'):
        self.holder_id = holder_id
        self.name = name
        self.status = status
        self.products = []
        self.payments = []

    def register(self):
        print(f"Policyholder {self.name} has been registered.")

    def suspend(self):
        self.status = 'Suspended'
        print(f"Policyholder {self.name} has been suspended.")

    def reactivate(self):
        if self.status == 'Suspended':
            self.status = 'Active'
            print(f"Policyholder {self.name} has been reactivated.")
        else:
            print(f"Policyholder {self.name} is already active.")
    
    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added to {self.name}'s policy.")
    
    def make_payment(self, payment):
        self.payments.append(payment)
        print(f"Payment of {payment.amount} received from {self.name}.")
