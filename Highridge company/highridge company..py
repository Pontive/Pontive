import random

def generate_employees(num_employees):
    # Create a list of employees dynamically
    employees = []
    for i in range(num_employees):
        # Generate a random salary between 3000 and 35000
        salary = random.randint(3000, 35000)
        # Randomly assign gender
        gender = random.choice(["Male", "Female"])
        # Add employee details to the list
        employees.append({"id": i+1, "salary": salary, "gender": gender})
    return employees

def generate_payment_slips(employees):
    for employee in employees:
        try:
            salary = employee["salary"]
            gender = employee["gender"]
            employee_level = "Unassigned"

            # Conditional statements for employee levels
            if 10000 < salary < 20000:
                employee_level = "A1"
            elif 7500 < salary < 30000 and gender == "Female":
                employee_level = "A5-F"

            print(f"Employee ID: {employee['id']} | Salary: {salary} | Gender: {gender} | Level: {employee_level}")

        except KeyError as e:
            print(f"Error: Missing information for employee ID {employee['id']}. Details: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Create a list of 400 employees
employees_list = generate_employees(400)

# Generate payment slips for all employees
generate_payment_slips(employees_list)
