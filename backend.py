import csv  # The csv module provides functionality for working with CSV files
import os   # The os module provides functionality for working with the file system

class BackEndManager:
    def __init__(self):
        self.data_file = ""  # Initialize the data_file attribute to an empty string

# The AddValueToCSV class represents a CSV file and provides a method for adding a value to it.
class AddValueToCSV:
    def __init__(self, file_name):
        # Check if the specified file exists, and raise an error if it doesn't
        if not os.path.exists(file_name):
            raise ValueError(f"File {file_name} does not exist.")
        
        # Store the file name as an instance variable
        self.file_name = file_name

    # Add a value to the CSV file
    def add_value(self, value):
        # Open the CSV file in append mode
        with open(self.file_name, 'a') as file:
            # Create a csv writer object
            writer = csv.writer(file)
            # Write a row to the CSV file containing the given value
            writer.writerow([value])

# The ComplexValue class represents a complex value consisting of a name, age, and ID
class ComplexValue:
    def __init__(self, name, age, id, file_name):
        # Store the name, age, ID, and file name as instance variables
        self.name = name
        self.age = age
        self.id = id
        self.file_name = file_name

        # Open the file in append mode and write the name, age, and ID as a comma-separated string
        with open(file_name, 'a') as my_file:
            my_file.write(f"{name}, {age}, {id}\n")

# Display the contents of a CSV file
def display_record(file_name):
    # Open the CSV file in read mode
    with open(file_name, "r") as file:
        # Read the contents of the file
        contents = file.read()
        # Print the contents to the console
        print(contents)

# The CreateCSV class represents a CSV file and provides a method for creating an empty file
class CreateCSV:
    def __init__(self, filename):
        # Store the filename as an instance variable
        self.filename = filename

    # Create an empty CSV file
    def create_file(self):
        # Check if the filename ends with '.csv', and raise an error if it doesn't
        if not self.filename.endswith('.csv'):
            raise ValueError("File name must end with '.csv'")
        # Open the file in write mode with newline='' to ensure that newlines are handled correctly
        with open(self.filename, 'w', newline='') as file:
            # Do nothing to create an empty file
            pass
