import random

# This function will be used to create a new knight

def create_Knight(knights):

    # Creates a dictionary with empty values for the knights data
    # Generating a random integer for the knights strength attribute

    knights_data = {
        'Name': '',
        'Gender': '',
        'Weapon': '',
        'Strength': random.randint(10, 100),
    }

    print("Lets create your knight!")

    # Add the knights data to the dictionary by appending

    knights_data['Name'] = str(input("What will be this fine knight's name?: "))
    print("Ok great! Your knight's name is: " + knights_data['Name'])

    # While loop in place until a valid input is received

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

    knights_data['Weapon'] = str(input("What is your knight's weapon of choice?: "))
    print("A bold choice sir/madam. The " + knights_data['Weapon'] + " can do much damage!")
    print("\n")

    print("Congratulations on creating your knight: " + knights_data["Name"] + " who is a " + knights_data["Gender"] + " with a chosen weapon of a" +
          knights_data['Weapon'] + ". Their strength is " + str(knights_data['Strength']))

    # Appends information to the knights then once complete returns to menu

    knights.append(knights_data)
    menu(knights_number)


# Change the information of selected knight
def changeData(knights, knights_index):

    # Retrieving a selected knight
    knight_data = knights[knights_index]
    army_number = 0

    # Open with question from the console to user
    print("--- What would you like to update with your Knight? ---")
    print("1: Name: ")
    print("2: Gender: ")
    print("3: Weapon: ")
    print("4: Join Army")

    # User makes a selection
    try:

        selection = int(input("Select your option: "))

        if selection == 1:
            if knights_number == 0:
                print("\n")
                new_name = str(input("Please type the new name for your knight: "))
                knight_data['Name'] = new_name
                print("Your knight's new name is: " + knight_data['Name'])
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
                    print(knight_data['Name'] + " is a male")
                    break

                elif new_gender == "F":
                    knight_data['Gender'] = 'Female'
                    print(knight_data['Name'] + " is a female")
                    break

                else:
                    ValueError
                    print("---Invalid input. Try again---")

            knight_data['Gender'] = new_gender
            print("\n")
            menu(knights_number)
            return

        elif selection == 3:
            print("\n")
            new_weapon = str(input("Please choose the new weapon for your knight"))
            knight_data['Weapon'] = new_weapon
            print("Your knight's weapon of choice is now: " + knight_data['Weapon'])
            print("\n")
            menu(knights_number)
            return

        elif selection == 4:
            print("\nArmies available: ")

            for index, armies in enumerate(army):
                print(str(index + 1) + ": " + armies['Name'])

            army_selection = int(input("Select which army for your knight to join? ")) - 1

            if len(army) == 0:
                print("There are no armies currently available! ")
                return

            elif 0 <= army_selection < len(army):
                army[army_selection]['Knights'].append(knight_data['Name'])
                print(knight_data['Name'] + " has joined " + army[army_selection]['Name'] + " army.")

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

    selection = (int(input("\nSelect the knight you would like to update?: \n or Press 0 to go back to Main Menu: ")) - 1)

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

    # Dictionary created to store army data
    # List to store the knights

    army_data = {
        'Name': '',
        'Knights': []
    }

    print("Would you like to create a new army?")
    response = str(input("Y/N?: ").capitalize())

    while True:
        if response == "Y":
            army_name = str(input("What would you like to call your army?: "))
            army_data['Name'] = army_name
            army.append(army_data)  # Append the created army to the army list
            print("Your new army is called:" + army_name)
            menu(knights_number)
            break

        elif response == "N":
            menu(knights_number)
            break

        else:
            print("--- Invalid Option. Try Again! ---")
            create_Army(army)


# This is the menu and we make our selections here

def menu(knights_number):

    # Menu options

    print("What would you like to do?:")
    print("1: Create a new knight")
    print("2: Update your knight")
    print("3: List of Knights")
    print("4: Create a new Army")
    print("5: Delete knight")
    print("6: List of armies")
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
                menu(knights_number)
            else:
                selectKnight(knights)
                menu(knights_number)

        elif selection == 3:
            displayKnights(knights)
            menu(knights_number)

        elif selection == 4:
            create_Army(army)

        elif selection == 5:
            deleteKnight(knights)
            menu(knights_number)

        elif selection == 6:
            displayArmies(army)
            menu(knights_number)

        elif selection == 0:
            print("--- Your Knights ---")

            # Reset the knight_numbers to count all the knights
            knights_number = 0

            # Prints all the knights names

            while knights_number < int(len(knights)):
                print(str(knights_number + 1) + ": Knight's name: " + str(knights[knights_number][0]))
                knights_number += 1

        else:
            print("--- Try Again ---")
            menu(knights_number)
    except:
        print(" --- Try Again ---")
        menu(knights_number)


def displayKnights(knights):

    if len(knights) == 0:
        print("There are currently no knights available")

        print(knights)


def deleteKnight(knights):

    # Check if any knights created
    if len(knights) == 0:

        print("No knights available to delete!")
        return

    # Loop through knights list
    else:
        print("Select the number of the knight you want to delete: ")
        for i, knight in enumerate(knights):
            print(str(i + 1) + ": " + knight['Name'])

        # The 'pop' method removes the selection from the list

        try:
            selection = int(input("Enter the number of the knight to delete: ")) - 1  # Adjust for 1-based input
            if 0 <= selection < len(knights):
                deleted_knight = knights.pop(selection)
                print(deleted_knight['Name'] + " has been deleted.")
            else:
                print("--- Invalid selection ---")
        except ValueError:
            print("Invalid input. Enter a valid number.")


# Displaying armies with knights within each army

def displayArmies(army):

    if len(army) == 0:
        print("No armies currently created")

    # Loop through the army index and print the knights names to joined with armies

    else:
        for index, armies in enumerate(army):
            print(str(index + 1) + ": " + armies['Name'] + " with knights: " + ', '.join(armies['Knights']))


# Initiate setup

knights_number = 0
knights = []

army_number = 0
army = []

# Opens up the menu when code is run

menu(knights_number)
