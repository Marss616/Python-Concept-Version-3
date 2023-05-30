import sys      # The sys module provides access to some variables used or maintained by the Python interpreter
import backend  # The backend module provides the back-end functionality

# The FrontEndUI class provides a user interface for interacting with the back-end functionality
class FrontEndUI:
    def __init__(self, backend):
        # Store the back-end functionality as an instance variable
        self.backend = backend

    # Display the user interface
    def show_ui(self):
        # Define a message to display to the user
        message = "\n"
        message += "Welcome to stock tracker for Generic Company PTY LTD \n"
        message += "1. To Add one value to a record \n"
        message += "2. To Display records \n"
        message += "3. To create a new file \n"
        message += "4. To add a record with three values \n"
        message += "5. To exit \n"
        message += "Whats your option "
        # Write the message to the standard output
        sys.stdout.write(message)
        # Read the user's input from the standard input
        user_input = int(sys.stdin.readline())
        question = "what do you want to add? \n"

        # Continue looping until the user chooses to exit
        while user_input != 5:
            if user_input == 1:
                # Ask the user for the name of the existing CSV file
                question_name_of_csv_file = "Enter the name of the existing CSV file: "
                sys.stdout.write(question_name_of_csv_file)
                file_name = input()
                # Ask the user for the value to add to the CSV file
                question_one_value_add = "Enter the value to add to the CSV file: "
                sys.stdout.write(question_one_value_add)
                value = input()
                # Create an AddValueToCSV object with the specified file name
                add_value_to_csv = backend.AddValueToCSV(file_name)
                # Add the value to the CSV file using the AddValueToCSV object
                add_value_to_csv.add_value(value)
                # Write the message to the standard output
                sys.stdout.write(message)
                # Read the user's input from the standard input
                user_input = int(sys.stdin.readline())

            elif user_input == 2:
                # Ask the user for the name of the file to display
                print("what file do you want display : try 'test_case.txt")
                file2 = str(sys.stdin.readline().strip())
                # Display the contents of the specified file
                backend.display_record(file2)
                # Write the message to the standard output
                sys.stdout.write(message)
                # Read the user's input from the standard input
                user_input = int(sys.stdin.readline())

            elif user_input == 3:
                # Ask the user for the name of the CSV file to create
                print("Enter the name of the .csv file to create, make sure to add the '.csv' at the end to avoid a error message: ")
                filename = sys.stdin.readline().strip()
                try:
                    # Create a new CSV file with the specified name
                    csv_file = backend.CreateCSV(filename)
                    csv_file.create_file()
                    # Display a success message
                    print("File created successfully.\n")
                    # Write the message to the standard output
                    print(message)
                    # Read the user's input from the standard input
                    user_input = int(sys.stdin.readline())
                except Exception as e:
                    # Display an error message if the file creation fails
                    print(str(e))
            elif user_input == 4:
                name = input("Enter the name of the item: ")
                age = input("Enter the shelf life of the item: ")
                id = input("Enter the ID of the item: ")
                file_name = input("Enter the name of the CSV file to store the record in: ")
                record = backend.ComplexValue(name, age, id, file_name)
                sys.stdout.write(message)
                user_input = int(sys.stdin.readline())
                # The reason I went with this method for the user to add muilt values to the .csv file is so that it can be upscaled if required, next best thing would to take one input and split the value up and then add it to the .csv file 

FrontEndUI.show_ui(self=0)