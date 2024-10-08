
# This function will be used to create a new knight
def createKnight(knights):

    # Creates an empty array for the knights data

    knights_data = []

    print("Lets create your knight!")

    # Add the knights data to the empty array by appending

    knights_data.append(str(input("What is your knights name?: ")))

    # Adds information
    knights.append(knights_data)

# Create an different Armys for knights to pick

def createArmy(army):

    army_data = []

    # Usilizing the capitalize function for the users response

    print("Would you like to create a new army? ")
    response = str(input("Y/N?:  ").capitalize())

    # Setting up new army and adding it to the Army Array
    if response == "Y":
        army_name = str(input("What would you like to call your army?: "))
        army_data.append(army_name)
        army.append(army_data)
        print("Your new army is called: ", army_name)

    # Returing to Main Menu
    elif response == "N":
        menu(knights_number)

    else:
        print("---Invalid Option. Try Again!--")


# Change the information of selected knight
def changeData(knights):

    # Open with question from the console to user
    print("--- What would you like to update? ---")
    print("1: Knight's name: " + knights[0])

    # User makes a selection
    try:

        selection = int(input("Select your option: "))

        if selection == 1:
            if knights_number == 0:
                print("\n")
            knights[0] = str(input("Please type the new name for your knight: "))
            print("Your knight's name is now: " + knights[0])
            print('\n')
            menu(knights_number)
            return

        else: 
            print("Please enter a valid name!")
    except:
        print("--- Try again ---")
        changeData(knights)

# Show the current list of knights and select one
def selectKnight(knights):

    # reset the list to print all the knights
    knights_number = 0
    print("Which knight would you like to update?: \n")
    while knights_number < int(len(knights)):
        print(str(knights_number + 1) + " Knight's name:" + str(knights[knights_number][0]))
        knights_number += 1
    
    selection = (int(input("\nSelect the knights number: ")) - 1)
    print("\n")
    changeData(knights[selection])


# This is the menu and we make our selections here

def menu(knights_number):

    # Menu options
    print("What would you like to do?:")
    print("1: Create a new knight")
    print("2: Update your knight")
    print("3: List of Knights")
    print("4: Create a new Army")
    print("5: Update Your Army")
    print("6: List of Armys")
    print("0: Exit")

    try:

        selection = int(input("Selection: "))
        print()

        if selection == 1:
            createKnight(knights)
            
            # Print confirmation of the knight that was made
            print("\n --- Your Knight ---")
            print("Knight's name: " + str(knights[knights_number][0] + "\n"))
            knights_number += 1
            menu(knights_number)
            
        # if not knight created then alert displayed to user to create one    
        elif selection == 2:
            if int(len(knights)) == 0:
                print("You need to create a knight first! \n")
            else:
                selectKnight(knights)
                menu(knights_number)

        elif selection == 3:
            print("--- Your knights ---")
            knights_number = 0
            
            # Display the list of current knights

            while(knights_number < int(len(knights))):
                print(str(knights_number + 1) + ": Knights name: " + str(knights[knights_number][0]))
                knights_number += 1

            menu(knights_number)

        elif selection == 4:
            createArmy(army)

        elif selection == 0:
            print("--- Your Knights ---")
            
            # Reset the knight_numbers to count all the knights
            knights_number = 0

            # Prints all the knights names

            while knights_number < int(len(knights)):
                print(str(knights_number + 1) + ": Knights name: " + str(knights[knights_number][0]))
                knights_number += 1
            

        else:
            print("--- Try Again ---")
            menu(knights_number)
    except:
        print(" --- Try Again ---")
        menu(knights_number)
                
knights_number = 0
knights = []

army_number = 0
army = []

menu(knights_number)



