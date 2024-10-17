# Define the path to the zip file
zip_file <- "C:/Users/YD/Documents/GETTING STARTED/Pontive/Employee_Profile.zip"
unzip_dir <- "C:/Users/YD/Documents/GETTING STARTED/Pontive/"

# Unzip the file
unzip(zip_file, exdir = unzip_dir)

# Define the path to the CSV file
csv_file <- "C:/Users/YD/Documents/GETTING STARTED/Pontive/Gary Jimenez_details.csv"

# Read the CSV file and display the data
employee_data <- read.csv(csv_file, stringsAsFactors = FALSE, na.strings = c("", "NA"))
print(head(employee_data))  # Display the first few rows
