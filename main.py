#import the necessary modules
import read
import operation

#welcome messages
print("\n")
print("\t \t Welcome to Mausam Rental Shop")
print("\n")
print("\t Address: Kamalpokhari | Contact: 9818123456")
print("\n")
print("Choose the option you want to continue")
print("\n")

#a function to create a formatted table
def create_table(data, headers):
    # Calculate the width of each column
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data, headers)]

    # Create the separator row
    separator = "+".join("-" * (width + 2) for width in col_widths)
    separator_row = f"+{separator}+"

    # Create the headers row
    headers_row = f"| {' | '.join(f'{header:<{width}}' for header, width in zip(headers, col_widths))} |"

    # Create the data rows
    data_rows = [f"| {' | '.join(f'{item:<{width}}' for item, width in zip(row, col_widths))} |" for row in data]

    # Combine everything to form the table
    table = "\n".join([separator_row, headers_row, separator_row] + data_rows + [separator_row])

    return table

#strating a loop for main menu
loop = True
while loop == True:

    #menu options and headers for the table
    options = [
        ["Press 1", "Rent"],
        ["Press 2", "Return"],
        ["Press 3", "Exit"]
    ]

    headers = ["Option", "Action"]

    #Create and display the table of options
    table = create_table(options, headers)
    print(table)
    print("\n")

    #setting a flag to ensure a valid option is being selected
    select_option = False
    while select_option == False:
        try:
            #Prompt for user to choose an operation
            userInput = int(input("Choose the operation you want to continue: "))
            select_option = True
            
            if userInput == 1:
                print("You are now renting items!")
                operation.rent_items()
                print("\n")
                
            elif userInput == 2:
                print("You are now returning items!")
                operation.return_items()
                print("\n")
                
            elif userInput == 3:
                print("Thank you for using our system!")
                loop = False #Exit the loop to end the program
                print("\n")
                
            else:
                print("Enter valid option")#when the user enters an invalid option
        except ValueError:  # Catch only ValueError, which is raised when conversion to int fails
            print("Entered option is invalid! Please enter shown options.")
