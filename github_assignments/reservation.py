#BCE0001125
# NAme: Muminatou BArrow


# Create a ticket reservation program. You've recently been employed as a developer by La vie 
# travel and tours to design a python based program for the company to manage its ticket reservatiion
# process. The program allows a user to first log into it by providing their username and password.
# Upon verfication and authentication, he/she is redirected to a menu page
# Exercise1: When the user selects option 1 from the menu, the location sub-menu is displayed
# Check book for display
#     a. Write a simple python function which will allow the user to allow a new location to their database
#     The location has a price per person and double for a night
#   Specify if there is discount
#     The location has a name which represents a location in a country
#     The location also has a city and country in which it is located
#     e.g. labadi beach, Accra, Ghana
    
#    ********* b. write/create a function to add a location count when a new location is added 
    
#     c. Upon selection of option 2, the user should be allowed to enter the name of a location
#     if the location exists in the database, it should be removed. This should also update the location count

#     d. Option 3 should take the user back to the previous menu and option 4 exits the user from the programm
# Note: U

from datetime import datetime
loc_list = []

def loc_count():
    global loc_list
    return len(loc_list)

def location():
    global new_location
    global loc_list

    print("---------------------")
    print(f"|     LOCATION {loc_count()}    |")
    print("---------------------")
    

    while True:
        print("1.\tAdd new location\n2.\tRemove a location\n3.\tBack\n4.\tExit")
        
        try:
            op1 = int(input("Choose from 1-4: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        
        
        if op1 == 1:
            
            while True:
                new_location = input("Input a new location: ")
                new_city = input("Enter name of the city: ")
                new_country = input("Enter name of the country: ")
                price_per_one = float(input("Cost for one-to-a-room: "))
                price_per_double = float(input("Cost for double-to-a-room: "))
                discount = float(input("What discount percentage is available? "))

                loc_dict = {
                    "Name": new_location,
                    "City": new_city,
                    "Country": new_country,
                    "Room for one": price_per_one,
                    "Room for two": price_per_double,
                    "Discount": discount
                }
                loc_list.append(loc_dict)
                print(f"Location Added: \n")
                print(loc_dict)
                print("---------------------")
                print(f"|     LOCATION {loc_count()}    |")
                print("---------------------")
    
            
                ask1 = int(input("\n\nDo you want to add another location? \n1. Yes\n2. No "))
                if ask1 not in [1, 2]:
                    print("Invalid option, Please choose 1 or 2!")
                    break
                elif ask1 == 2:
                    break
                    
        
        elif op1 == 2:
            for loc_dict in loc_list:
                print(loc_dict)
            print("Which location do you want to remove?")

            remove_location = int(input("Enter index here: "))
            if 0 <= remove_location < len(loc_list):
                del loc_list[remove_location]
                print(f"\nSuccess! Location on index {remove_location} has been removed")
                print("Updated List:\n ")
                print("---------------------")
                print(f"|     LOCATION {loc_count()}    |")
                print("---------------------")
    
                for loc_dict in loc_list:
                    print(loc_dict)
                continue
        elif op1 == 3:
            break
        elif op1 == 4:
            break
        else:
            print("Select correct option!")
            continue

def reservation():
    global new_location
    global loc_list

    print("-----------------------------")
    print("|  Welcome to Reservation!  |")
    print("-----------------------------")
    
    customer_name = input("Enter your name: ")
    customer_number = int(input("Enter your phone number: "))

    for loc_dict in loc_list:
        print(loc_dict)

    while True:
        reserve = int(input("\nWrite in the index of the location you want to make a reservation on: "))
        if 0 <= reserve < len(loc_list):
            selected_location = loc_list[reserve]
            print(selected_location)
            room_reserve = int(input("\nPlease select room option from the two prices: \n1. Room for one \n2. Room for two "))
            if room_reserve == 1:
                room_price = selected_location["Room for one"]             
                room_num = int(input("How many rooms for one each do you want to reserve? "))
                price = room_num * room_price
                print(f"\nPrice is {price}\n")

                another_room = int(input("Would you like to add another room for the other option? \n1. Yes\n2. No "))
                if another_room == 1:
                    pass
                else:
                    break

            elif room_reserve == 2:
                room_price2 = selected_location["Room for two"]             
                room_num2 = int(input("How many rooms for two each do you want to reserve? "))
                price2 = room_num2 * room_price2
                print(f"\nPrice is {price2}\n")

                another_room = int(input("Would you like to add another room for the other option? \n1. Yes\n2. No "))
                if another_room == 1:
                    pass
                else:
                    break

            else:
                print("Wrong option! Please select 1 or 2!\n")
                continue

           

        else:
            print("Select a correct index!")
            continue

    
    total = price or price + price2 or price2
    print("----------------------------")
    print("|  Reservation Cost Total  |")
    print("|         Checkout         |")
    print("----------------------------")      
    print(f"\nTotal price for reservation: \t{total}")
    print(f"Reserved by: \t\t\t\t{customer_name}")
    print(f"Phone Number: \t\t\t\t{customer_number}")
    print(f"Time:  \t\t\t\t\t{datetime.now()}\n\n")
        


    # try:
    #    with open('C:/Users/user/Documents/level300/Semester 2/github_assignments/reservation.txt', 'a') as to_File:
    #         for loc_dict in loc_list:
    #             to_File.write(f"{loc_dict} {datetime.now()}\n")
                
    # except Exception as e:
    #      print(f"Error: {e}")

    with open('C:/Users/user/Documents/level300/Semester 2/github_assignments/reservation.txt', 'a') as to_File:
        for loc_dict in loc_list:
            to_File.write(f"{loc_dict} {datetime.now()}\n")
             

    
def save_data():
    
    with open("C:/Users/user/Documents/level300/Semester 2/github_assignments/reservation.txt", 'r') as file:
        data = file.read()
        print(data)
    
 


print("***WELCOME TO LA VIE TRAVEL AND TOURS***")
print("----------------")
print("|  LOGIN HERE  |")
print("----------------")
name = input("Username: ")
password = input("Password: ")

username = "mumi"
pwd = "password"
while True:
    if name == username and password == pwd:
        print("------------")
        print("|   MENU   |")
        print("------------")
        print("1.\tLocation\n2.\tReservation\n3.\tSave Data\n4. \tExit\n")
        menu = int(input("Choose from 1-4: "))
        if menu == 1:
            location()
        elif menu == 2:
            reservation()
        elif menu == 3:
            save_data() 
        elif menu == 4:
            break
        else:
            print("Please choose from 1-4")
            continue
    else:
        print("Invalid login details!")
        continue

            
