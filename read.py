def read_file_txt():
    with open("equipment.txt", "r") as file:
        #read the content of the equipment.txt file and store item details in a dictionary
        item_id = 1
        item_dictionary = {}
        for line in file:
            line = line.replace("\n", "")
            item_dictionary[item_id]= line.split(",")
            item_id = item_id+1

    return item_dictionary

def display_stock():
    with open("equipment.txt", "r") as file:
        i = 1

        #display the stock of items in a formatted table-like format
        for line in file:
           print(i, "\t" + line.replace(",", "\t"))
           i = i + 1
    print("---------------------------------------------------------------------------")
    print("\n")

def items_header(name):
    print("\n")
    print("*---------------------------------------------------------------------------*")
    #display a welcome message with the customer's name and header for item details
    print("Thank you for your name, ", name)
    print("Given below are the list of items. Provide the details required")
    print("*---------------------------------------------------------------------------*")
    print("S.N. \titem Name  \t Company Name               Price    \t  Quantity")
    print("*---------------------------------------------------------------------------*")  


