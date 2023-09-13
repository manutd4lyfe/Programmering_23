# Define a room
description = "big room with a chandeler hanging from the roof, and paintings all"
doors = ["north", "south", "east", "west"]

# Welcome screen
print("Hej och välkommen till Jimmys Berlin textäventyr")
print("************************************************")
print()

# Main loop/Gameloop
run = True
while run:
    # Print room
    print("You are standing in a " + description)
    print("There are doors to your: ")
    
    # Format and print out all the directions that are available in the room
    directions = ""
    for direction in doors:
        directions = directions + ", " + direction
    directions = directions[2:]
    print(directions)
    print()
    
    # Print menu
    print("What do you want to do?")
    print("1. Go north")
    print("2. Go south")
    print("3. Go east")
    print("4. Go west")
    print("5. Look")
    print("0. Quit game")

    # Ask user for input
    choice = input("Please enter your choice: ")

    # Sanitize user input
    if not choice.isnumeric():
        print("Sorry! I did not understand what you meant.")
        continue

    choice = int(choice)
    if choice == 0:
        run = False
    elif choice == 1:
        print("You are going north.")
    elif choice == 2:
        print("You are going south.")
    elif choice == 3:
        print("You are going east.")
    elif choice == 4:
        print("You are going west.")
    elif choice == 5:
        print("You are looking really hard, but can't find anything new.")
    else:
        print("Invalid choice. Please select a valid option.")
    