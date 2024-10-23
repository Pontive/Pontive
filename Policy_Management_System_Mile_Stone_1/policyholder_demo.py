from policyholder import Policyholder
from product import Product
from payment import Payment

# Creating insurance policy products with their id
health_insurance = Product(9, "Health Insurance", 1000)
morgage_insurance = Product(10, "Morgage Insurance", 850)

# Create two policyholders with their id
mike = Policyholder(23, "Mike Musambe")
ruth = Policyholder(30, "Ruth Ndung'u")

# Summation of products to policyholders
mike.add_product(health_insurance)
ruth.add_product(morgage_insurance)

# Create payments and their ids  for the policyholders
payment1 = Payment(45, 1000, mike.holder_id)
payment2 = Payment(49, 8500, ruth.holder_id)

# Payments processing
mike.make_payment(payment1)
ruth.make_payment(payment2)

# Display details
print(f"Policyholder {mike.name} has {len(mike.products)} product(s).")
print(f"Policyholder {ruth.name} has {len(ruth.products)} product(s).")

