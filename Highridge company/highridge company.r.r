# Install and load the required package
install.packages("dplyr")
library(dplyr)

# Set seed for reproducibility
set.seed(123)

# Function to generate employees dynamically
generate_employees <- function(num_employees) {
  # Create a data frame to store employee details
  employees <- data.frame(
    id = 1:num_employees,
    salary = sample(3000:35000, num_employees, replace = TRUE),
    gender = sample(c("Male", "Female"), num_employees, replace = TRUE)
  )
  return(employees)
}

# Function to generate payment slips for employees
generate_payment_slips <- function(employees) {
  for (i in 1:nrow(employees)) {
    tryCatch({
      salary <- employees$salary[i]
      gender <- employees$gender[i]
      employee_level <- "Unassigned"
      
      # Conditional statements for employee levels
      if (salary > 10000 & salary < 20000) {
        employee_level <- "A1"
      } else if (salary > 7500 & salary < 30000 & gender == "Female") {
        employee_level <- "A5-F"
      }
      
      # Print employee details
      cat(sprintf("Employee ID: %d | Salary: %d | Gender: %s | Level: %s\n", 
                  employees$id[i], salary, gender, employee_level))
    }, error = function(e) {
      cat(sprintf("Error: Missing information for employee ID %d. Details: %s\n", 
                  employees$id[i], e$message))
    }, warning = function(w) {
      cat(sprintf("Warning for employee ID %d: %s\n", 
                  employees$id[i], w$message))
    })
  }
}

# Create a list of 400 employees
employees_list <- generate_employees(400)

# Generate payment slips for all employees
generate_payment_slips(employees_list)

