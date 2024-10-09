
# This function will be used to create a new knight

def create_Knight(knights):

    # Creates a dictionary with empty values for the knights data

    knights_data = {
        'Name' : '',
        'Gender' : '',
        'Weapon' : '',
    }

    print("Lets create your knight!")

    # Add the knights data to the dictionary by appending

    knights_data['Name'] = str(input("What will be this fine knights name?: "))
    print("Ok great! Your knights name is: " + knights_data['Name'])

    # While loop in place until a valid input is recieved

    while True:
        print("What is the gender of your knight?: ")
        response = str(input("M/F?: ").capitalize())

        if response == "M":
            knights_data['Gender'] = 'Male'
            print("Your knight is a male")
            break
        
        elif response == "F":
            knights_data['Gender'] = 'Female'
            print("Your knight is a female")
            break

        else:
            print("---Invalid input. Try again---")

    

    knights_data['Weapon'] = str(input("What is your knights weapon of choice?: "))
    print("A bold choice sir/madam. The " + knights_data['Weapon'] + " can do much damage!"  )
    print("\n")

    # Appends information to the knights then once complete returns to menu

    knights.append(knights_data)
    menu(knights_number)


# Change the information of selected knight
def changeData(knights, knights_index):

    # Retrieving a selected knight
    knight_data = knights[knights_index]

    # Open with question from the console to user
    print("--- What would you like to update with your Knight? ---")
    print("1: Name: ")
    print("2: Gender: ")
    print("3: Weapon: ")

    # User makes a selection
    try:

        selection = int(input("Select your option: "))

        if selection == 1:
            if knights_number == 0:
                print("\n")
            new_name = str(input("Please type the new name for your knight: "))
            knight_data['Name'] = new_name
            print("Your knights new name is: " + knight_data['Name'])
            print('\n')
            menu(knights_number)
            return
        
        elif selection == 2:
            print("\n")
            print("Please choose the new gender for your knight: ")
            new_gender = str(input("M/F?: ").capitalize())

            while True: 
                if new_gender == "M":
                    knight_data['Gender'] = 'Male'
                    print("Your knight is a male")
                    break
                
                elif new_gender == "F":
                    knight_data['Gender'] = 'Female'
                    print("Your knight is a female")
                    break

                else:
                    ValueError
                    print("---Invalid input. Try again---")

            knight_data['Gender'] = new_gender
            print("Your knights gender has been set to: " + knight_data['Gender'])
            print("\n")
            menu(knights_number)
            return
        
        elif selection == 3:
            print("\n")
            new_weapon = str(input("Please choose the new weapon for your knight"))
            knight_data['Weapon'] = new_weapon
            print("Your knights weapon of choice is now: " + knight_data['Weapon'])
            print("\n")
            menu(knights_number)
            return

        else: 
            print("Please enter a valid number")

    except:
        ValueError
        print("--- Invalid input. Try again ---")
        changeData(knights, knights_index)


# Show the current list of knights and select one
def selectKnight(knights):

    # reset the list to print all the knights
    knights_number = 0

    while knights_number < int(len(knights)):
        print(str(knights_number + 1) + ": " + str(knights[knights_number]['Name']))
        knights_number += 1

    selection = (int(input("\nSelect the knight you would like to update?: \n or Press 0 to go back to Main Menu: ")) - 1 )
    
    try:

        if selection == -1:
            menu(knights_number)

        elif selection < 0 or selection >= len(knights):
            print("--- Invalid number. Please try again --- ")

        else:
            changeData(knights, selection)
    
    except: 
        ValueError("----Invalid number----")


# Create Army stable

def create_Army(army):

    army_data = []

    # Usilizing the capitalize function for the users response

    print("Would you like to create a new army? ")
    response = str(input("Y/N?:  ").capitalize())

    # Setting up new army and adding it to the Army Array
    while True:
        if response == "Y":
            army_name = str(input("What would you like to call your army?: "))
            army_data.append(army_name)
            army.append(army_data)
            print("Your new army is called: ", army_name)
            menu(knights_number)
            break

        # Returing to Main Menu
        elif response == "N":
            menu(knights_number)
            break

        else:
            print("---Invalid Option. Try Again!--")
            create_Army(army)

# This is the menu and we make our selections here

def menu(knights_number):

    # Menu options
    print("What would you like to do?:")
    print("1: Create a new knight")
    print("2: Update your knight")
    print("3: List of Knights")
    print("4: Create a new Army")
    print("5: Update Your Army")
    print("0: Exit")

    try:

        selection = int(input("Selection: "))
        print()

        if selection == 1:
            create_Knight(knights)
            
            # Print confirmation of the knight that was made
            print("\n --- Your Knight ---")
            print("Knight's name: " + str(knights[knights_number][0]) + "\n")
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
            create_Army(army)

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



