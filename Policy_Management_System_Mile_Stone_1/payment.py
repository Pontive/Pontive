class Payment:
    def __init__(self, payment_id, amount, policyholder_id):
        self.payment_id = payment_id
        self.amount = amount
        self.policyholder_id = policyholder_id

    def process(self):
        print(f"Processing payment of {self.amount} for policyholder {self.policyholder_id}.")
    
    def apply_penalty(self, penalty_amount):
        self.amount += penalty_amount
        print(f"Penalty of {penalty_amount} applied. New amount due: {self.amount}.")
    
    def send_reminder(self):
        print(f"Reminder sent for payment of {self.amount}.")
