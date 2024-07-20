import read
from datetime import datetime

#display rental bill for customer
def display_rent_bill(name, phone_number, today_date_and_time, item_info, grand_total):

    #print the header and customer details
    print("\n")
    print("\t \t Welcome to Mausam Rental Shop")
    print("\n")
    print("\t Address: Kamalpokhari | Contact: 9818123456")
    print("\n")
    print("----------------------------------------------------------------------------------------------")
    print("Items Details are:")
    print("----------------------------------------------------------------------------------------------")
    print("Name of the customer:" + str(name))
    print("Contact number:" + str(phone_number))
    print("Date and time of purchase:" + str(today_date_and_time))    
    print("----------------------------------------------------------------------------------------------")
    print("\n")
    print("Purchase Details are:")

    #print the table headers
    print("----------------------------------------------------------------------------------------------")
    print("  Item Name   \t\t Total Quantity    \t\t Unit Price \t\t\tTotal")
    print("----------------------------------------------------------------------------------------------")
    #print each item's details
    for i in item_info:
        print(i[0],"\t\t",i[1],"\t\t\t",str( i[2]), "\t\t\t", "$",str(i[3]))
    #print the footer and additional information
    print("----------------------------------------------------------------------------------------------")
    print("Grand Total: $" + str(grand_total))
    print("Rent is for 5 days.")
    print("**Note: Fine cost will added to the grand total in case of delay**")
    print("----------------------------------------------------------------------------------------------")

#print rental bill to a text file
def print_bill1(name, phone_number, today_date_and_time, item_info, grand_total):
    file_name = str(name) + "_" + str(phone_number) + ".txt"                
    with open(file_name, 'w') as file:
        today_date_and_time = datetime.now()
        file.write("\n")
        file.write("\t \t Welcome to Mausam Rental Shop")
        file.write("\n")
        file.write("\t Address: Kamalpokhari | Contact: 9818123456")
        file.write("\n")
        file.write("-------------------------------------------------------------------------------")
        file.write("Items Details are:")
        file.write("-------------------------------------------------------------------------------")
        file.write("Name of the customer:" + str(name))
        file.write("Contact number:" + str(phone_number))
        file.write("Date and time of purchase:" + str(today_date_and_time))    
        file.write("-------------------------------------------------------------------------------") 
        file.write("\n")
        file.write("Purchase Details are:")  
        file.write("-------------------------------------------------------------------------------")
        file.write("Item Name \t\t Total Quantity \t\t Unit Price \t\t\tTotal")
        file.write("-------------------------------------------------------------------------------")
        for i in item_info:
            file.write(str(i[0]) + "\t\t\t"+ str(i[1])+ "\t\t\t"+str( i[2])+ "\t\t\t"+ "$"+ str(i[3]))
        file.write("-------------------------------------------------------------------------------")
        file.write("Grand Total: $" + str(grand_total))
        file.write("\n")
        file.write("***Note: Fine cost will added to the grand total in case of delay***")
        file.write("\n")

#display return bill for customer
def display_return_bill(name1, phone_number, today_date_and_time, return_info, fine, grand_total):
    print("\n")
    print("\t \t Welcome to Mausam Rental Shop")
    print("\n")
    print("\t Address: Kamalpokhari | Contact: 9818123456")
    print("\n")
    print("----------------------------------------------------------------------------------------------")
    print("Items Details are:")
    print("----------------------------------------------------------------------------------------------")
    print("Name of the customer:" + str(name1))
    print("Contact number:" + str(phone_number))
    print("Date and time of purchase:" + str(today_date_and_time))    
    print("----------------------------------------------------------------------------------------------") 
    print("\n")
    print("Returned Details are:")  
    print("----------------------------------------------------------------------------------------------")
    print("  Item Name   \t\t Total Quantity    \t\t Unit Price \t\t\tTotal")
    print("----------------------------------------------------------------------------------------------")
    for i in return_info:
        print(i[0],"\t\t",i[1],"\t\t\t",str( i[2]), "\t\t\t", "$",str(i[3]))
    print("----------------------------------------------------------------------------------------------")
    print("Fine after exceeding 5 days of overdue: " + str(fine))
    print("Grand Total: $" + str(grand_total))
    print("Return within 5 days.")
    print("**Note: Fine cost will added to the grand total in case of delay**")
    print("----------------------------------------------------------------------------------------------")

#print return bill to a text file
def print_bill2(name1, phone_number, today_date_and_time, return_info, fine, grand_total):
    file_name = str(name1) + "_" + str(phone_number) + ".txt"                
    with open(file_name, 'w') as file:
        today_date_and_time = datetime.now()
        file.write("\n")
        file.write("\t \t Welcome to Mausam Rental Shop")
        file.write("\n")
        file.write("\t Address: Kamalpokhari | Contact: 9818123456")
        file.write("\n")
        file.write("-------------------------------------------------------------------------------")
        file.write("Items Details are:")
        file.write("-------------------------------------------------------------------------------")
        file.write("Name of the customer:" + str(name1))
        file.write("Contact number:" + str(phone_number))
        file.write("Date and time of purchase:" + str(today_date_and_time))    
        file.write("-------------------------------------------------------------------------------") 
        file.write("\n")
        file.write("Purchase Details are:")  
        file.write("-------------------------------------------------------------------------------")
        file.write("Item Name \t\t Total Quantity \t\t Unit Price \t\t\tTotal")
        file.write("-------------------------------------------------------------------------------")
        for i in return_info:
            file.write(str(i[0]) + "\t\t\t"+ str(i[1])+ "\t\t\t"+str( i[2])+ "\t\t\t"+ "$"+ str(i[3]))
        file.write("-------------------------------------------------------------------------------")
        file.write("\n")
        file.write("\n")
        file.write("Fine after exceeding 5 days of overdue: " + str(fine)) 
        file.write("Grand Total: $" + str(grand_total))
        file.write("\n")
        file.write("***Note: Fine cost will added to the grand total in case of delay***")
        file.write("\n")
