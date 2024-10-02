
def createKnight(knights):

    # Creates a new list for the knight
    knights_data = []

    print("Lets create your knight")

    # Input the knights information
    knights_data.append(str(input("What is your knights name?: ")))

    # Adds information to the knight
    knights.append(knights_data)

# Change the information of selected knight
def changeData(knights):

    print("--- What would you like to update? --- ")
    print("1: Knights name: " + knights[0])

    try:

        selection = int(input("Selection of your option: "))

        if selection == 1:
            if knights_number == 0:
                print("You have a knight!")
            knights[0] = str(input("What is your new name?: "))
            print("Your knights new name is: " + knights[0])
            print("\n")
            return
        else: 
            print("--- Please select a valid option ---")

    except:
        print("--- Try Again ---")
        changeData(knights)

# Show the current knights and select one
def selectKnight(knights):

    # Reset the list to print all the knights you have
    knights_number = 0
    print("What knight would you like to update?: \n")
    while knights_number < int(len(knights)):
        print(str(knights_number + 1) + " Knight's name:" + str(knights[knights_number][0]))
        knights_number += 1

    selection = (int(input("\nSelect the knights number: ")) - 1)
    changeData(knights[selection])

# This is the menu and we make our selections here
def menu(knights_number):

    # Print the display options
    print("What do you want to do?")
    print("1: Create a new knight")
    print("2: Update your knight")
    print("0: Exit")

    # Allows a selection to be tested
    try: 

        # Takes the users selection option
        select = int(input("Selection number: "))
        print() # Creates a blank line

        # Creates a new knight

        if select == 1:
            createKnight(knights)

            # Print confirmation of the knight that was made
            print("\n--- Your knight ---\n")
            print("Knights's name: " + str(knights[knights_number][0] + "\n"))
            knights_number += 1
            menu(knights_number)

        elif select == 2:
            if int(len(knights)) == 0:
                print("You need to create a knight first!! \n")
            else:
                selectKnight(knights)


        elif select == 0:
            print("--- All your knights ---")

            # Reset the knights_number, to count all the knights
            knights_number = 0

            while knights_number < int(len(knights)):
                print(str(knights_number + 1) + " Knight's name:" + str(knights[knights_number][0]))
                knights_number += 1

        # Required for catching an integer
        else: 
            print("--- Try Again! ---")
            menu(knights_number)
    # This happens when we are looking for an integer selection
    except: 
        print("--- Try Again! ---")
        menu(knights_number)

# Setting the scene
knights_number = 0
knights = []

# Run the program
menu(knights_number)
