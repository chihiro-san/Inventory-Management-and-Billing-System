from datetime import datetime
import write
import read

#function to get the name of the renting customer
def get_name_of_renting_customer():
    """
    get the name of customer renting items.

    Returns:
        str: Name of customer.
    """
    name = input("Enter the name of customer: ")
    while not name.isalpha():
        print("Invalid name!! Please enter alphabetic characters only.")
        name = input("Enter the name of the customer: ")
    return name

#function to get the name of the returning customer
def get_name_of_returning_customer():
    """
    get the name of customer returning items.

    Returns:
        str: Name of customer.
    """
    name1 = input("Enter the name of customer: ")
    while not name1.isalpha():
        print("Invalid name!! Please enter alphabetic characters only.")
        name1 = input("Enter the name of the customer: ")
    return name1

#function to get a valid phone number from the user
def get_number():
    """
    get a valid phone number from the user.

    Returns:
        str: The valid 10-digit phone number.
    """
    phone_number = input("Enter the phone number of the customer: ")
    while not (phone_number.isdigit() and len(phone_number) == 10):
        print("Invalid phone number. Please enter a valid 10-digit number.")
        phone_number = input("Enter the phone number of the customer: ")
    return phone_number

#function to get the number of days for returning items
def get_no_of_days():
    """
    get the number of days the items are returned in.

    Returns:
        int: The number of days.
    """
    while True:
        try:
            no_of_days = int(input("Enter the number of days the items are returned in: "))
            if no_of_days < 0:
                raise ValueError("Number of days cannot be negative.")
            break
        except ValueError as e:
            print(e)
    return no_of_days

#function to rent items to customers and generate rent invoices   
def rent_items():
    '''
    this function let customers rent items and generate invoice on the basis of user input
    additionally, it also update stocks in .txt file after renting items
    '''
    
    bought_item = {}  # Initialize an empty dictionary to store item details
    item_info = []    # Initialize an empty list to store selected item info
    want_more = True  # Initialize a flag for looping

    print("*-------------------------------------------------------------------------*")
    print("\tTo generate a rent invoice, Enter the details of the customer")
    print("*-------------------------------------------------------------------------*")

    name = get_name_of_renting_customer()
    phone_number = get_number()

    #display header and stock table
    read.items_header(name)
    read.display_stock()

    #read item details from file    
    bought_item = read.read_file_txt()  # Use read.read_file_txt() to get the item details
            
    while True:
        try:
            valid_id = int(input("Enter the id of the item you want to rent: "))
            if valid_id <= 0 or valid_id > len(bought_item):
                raise ValueError("Invalid ID!!. Please enter a valid item ID.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            quantity = int(input("Enter the quantity you want to rent: "))
            get_quantity_of_item = int(bought_item[valid_id][3])
            if quantity <= 0 or quantity > len(bought_item):
                raise ValueError("Invalid quantity!!. Please enter a valid item quantity.")
            break
        except ValueError as e:
            print(e)

    #update equipment.txt
    bought_item[valid_id][3] = int(bought_item[valid_id][3]) - int(quantity)

    with open("equipment.txt", "w") as file:
        for values in bought_item.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+",")
            file.write("\n")


    #calculate total price and store item info
    product_name = bought_item[valid_id][0]
    item_price = bought_item[valid_id][2]
    selected_item_price = item_price.replace("$", '')
    total_price_to_pay = int(selected_item_price) * int(quantity)
    item_info.append([product_name, quantity, item_price, total_price_to_pay])

    while want_more:
        try:
            user_req = input("Do you want to rent more items? (Y/N): ").upper()
            if user_req == "Y":
                try:
                    valid_id = int(input("Enter the id of the item you want to rent: "))
                    quantity = int(input("Enter the quantity you want to rent: "))

                    bought_item[valid_id][3] = int(bought_item[valid_id][3]) - int(quantity)

                    with open("equipment.txt", "w") as file:
                        for values in bought_item.values():
                            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+",")
                            file.write("\n")
                    
                    # Calculate total price and store item info
                    product_name = bought_item[valid_id][0]
                    item_price = bought_item[valid_id][2]
                    selected_item_price = item_price.replace("$", '')
                    total_price_to_pay = int(selected_item_price) * int(quantity)
                    item_info.append([product_name, quantity, item_price, total_price_to_pay])
                except ValueError as e:
                    print("Invalid input. Please enter valid numeric values.")
            elif user_req == "N":
                want_more = False
            else:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        except ValueError as e:
            print("Invalid input. Please enter valid values.")  

    total = sum(i[3] for i in item_info)
    grand_total = total
    today_date_and_time = datetime.now()

    #calling the functions from write module
    write.display_rent_bill(name, phone_number, today_date_and_time, item_info, grand_total)
    write.print_bill1(name, phone_number, today_date_and_time, item_info, grand_total)

#for returning item
def return_items():
    '''
    this function let customers return items and generate invoice on the basis of user input
    additionally, it also update stocks in .txt file after returning items
    '''
    returned_item = {}  # Initialize an empty dictionary to store returned item details
    return_info = []    # Initialize an empty list to store returned item info
    want_more = True    # Initialize a flag for looping

    print("*-------------------------------------------------------------------------*")
    print("\tTo generate a return invoice, Enter the details of the customer")
    print("*-------------------------------------------------------------------------*")

    name1 = get_name_of_returning_customer()
    phone_number = get_number()

    #display header and stock table
    read.items_header(name1)
    read.display_stock()

    returned_item = read.read_file_txt()  # Use read.read_file_txt() to get the item details

    while True:
        try:
            valid_id = int(input("Enter the id of the item you want to return: "))
            if valid_id <= 0 or valid_id > len(returned_item):
                raise ValueError("Invalid ID!!. Please enter a valid item ID.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            quantity = int(input("Enter the quantity you want to return: "))
            if quantity <= 0:
                raise ValueError("Invalid quantity!!. Please enter a valid item quantity.")
            break
        except ValueError as e:
            print(e)
    

    # Update equipment.txt
    returned_item[valid_id][3] = int(returned_item[valid_id][3]) + int(quantity)

    with open("equipment.txt", "w") as file:
        for values in returned_item.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+",")
            file.write("\n")


    # Store returned returned info
    product_name = returned_item[valid_id][0]
    item_price = returned_item[valid_id][2]
    selected_item_price = item_price.replace("$", '')
    total_price_to_pay = int(selected_item_price) * int(quantity)
    return_info.append([product_name, quantity, item_price, total_price_to_pay])

        
    while want_more:
        try:
            user_req = input("Do you want to return more items? (Y/N): ").upper()
            if user_req == "Y":
                try:
                    valid_id = int(input("Enter the id of the item you want to return: "))
                    quantity = int(input("Enter the quantity you want to return: "))

                    returned_item[valid_id][3] = int(returned_item[valid_id][3]) + int(quantity)

                    with open("equipment.txt", "w") as file:
                        for values in returned_item.values():
                            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+",")
                            file.write("\n")

                    # Calculate total price and store returned item info
                    product_name = returned_item[valid_id][0]
                    item_price = returned_item[valid_id][2]
                    selected_item_price = item_price.replace("$", '')
                    total_price_to_pay = int(selected_item_price) * int(quantity)
                    return_info.append([product_name, quantity, item_price, total_price_to_pay])
                except ValueError as e:
                    print("Invalid input. Please enter valid numeric values.")
            elif user_req == "N":
                want_more = False
            else:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        except ValueError as e:
            print("Invalid input. Please enter valid values.")

    no_of_days = get_no_of_days()
    fine_per_days = 30
    fine = 0
    while fine == 0:    
        if no_of_days > 5:
            extra_days = no_of_days - 5
            fineday = (extra_days//5)+1
            fine = fine_per_days * fineday
            print("Total fine is: ", fine)
            break
        else:
            print("No fine is added", fine)
                            
    total_price_to_pay = sum(i[3] for i in return_info)
    grand_total = total_price_to_pay + fine
    today_date_and_time = datetime.now()

    #calling the functions from write module
    write.display_return_bill(name1, phone_number, today_date_and_time, return_info, fine, grand_total)
    write.print_bill2(name1, phone_number, today_date_and_time, return_info, fine,grand_total)
