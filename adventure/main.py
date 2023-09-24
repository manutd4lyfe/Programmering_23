import os
import random

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Mystical realms and random realm selection
realms = ["Enchanted Forest", "Elven Glade", "Dragon's Lair", "Lake of the Water Elemental"]
choose_realm = lambda: random.choice(realms)

# Player's enchanted inventory
inventory = []

# Function to display inventory and convert 'y' and 'n' to 'yes' and 'no'
def display_inventory():
    clear_screen()
    if not inventory:
        print("Your enchanted inventory is empty.")
    else:
        print("Your enchanted inventory contains the following items:")
        [print("- " + item) for item in inventory]

def yes_no_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'yes']:
            return 'yes'
        elif choice in ['n', 'no']:
            return 'no'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

while True:
    current_realm = choose_realm()
    print("Welcome to the mystical adventure!")
    print("You have entered the realm of " + current_realm)

    # Random encounter with a magical being
    beings = ["Wise Elf", "Fierce Dragon", "Enigmatic Water Elemental"]
    random_being = random.choice(beings)
    print("You encounter a formidable " + random_being + " in the realm of " + current_realm + "!")

    # Ask the player if they wish to interact with the magical being
    choice = yes_no_input("Do you wish to approach the " + random_being + "? (yes/no): ")

    # Interaction with the magical being
    if choice == "yes":
        if random_being == "Wise Elf":
            print(random_being + ": Greetings, traveler. Solve my ancient riddle, and you shall receive a mystical artifact!")
            answer = input("Which riddle would you like to answer? (moon/sun): ")
            if answer.lower() == "moon":
                print(random_being + ": Correct! Here's your Moonstone Amulet!")
                inventory.append("Moonstone Amulet")
                display_inventory()
            else:
                print(random_being + ": Alas, incorrect. But fear not, for your journey holds great promise.")
        elif random_being == "Fierce Dragon":
            print(random_being + ": Halt, traveler! I'll permit your passage only in exchange for a rare treasure.")
            if "Dragon Scale" in inventory:
                print("You present the Dragon Scale, and the dragon allows you to proceed.")
            else:
                print("You have no Dragon Scale to offer the dragon. It guards the path ahead.")
        elif random_being == "Enigmatic Water Elemental":
            print(random_being + ": Your collection of mystical artifacts intrigues me. Would you like to trade for my Enchanted Trident?")
            choice = yes_no_input("Would you like to make a trade? (yes/no): ")
            if choice == "yes":
                print(random_being + ": Excellent! Here's my Enchanted Trident.")
                inventory.append("Enchanted Trident")
                display_inventory()
            else:
                print(random_being + ": Should you reconsider, return to me.")

    else:
        print(random_being + ": May the ancient spirits guide your path.")

    # Random Mystical Events (Add more for variety)
    mystical_event = random.randint(1, 10)
    if mystical_event == 1:
        print("You stumble upon a hidden chamber filled with ancient scrolls of arcane knowledge!")
        inventory.append("Arcane Scrolls")
        display_inventory()
    elif mystical_event == 2:
        print("The sky above you comes alive with celestial lights, infusing you with mystical energy.")
    elif mystical_event == 3:
        print("A spectral merchant materializes before you. 'Greetings, traveler. Would you like to trade for a Potion of Vitality?'")
        print("Merchant: The cost is 5 Ether Crystals.")
        merchant_choice = yes_no_input("Make the trade? (yes/no): ")
        if merchant_choice == "yes":
            if "Ether Crystals" in inventory and inventory.count("Ether Crystals") >= 5:
                print("Merchant: A wise choice! Here's the Potion of Vitality.")
                inventory.append("Potion of Vitality")
                display_inventory()
                inventory.remove("Ether Crystals")
            else:
                print("Merchant: You lack the required Ether Crystals.")
        else:
            print("Merchant: Farewell, traveler.")
    elif mystical_event == 4:
        print("You discover an ancient portal, but you decide to postpone your journey through it for now.")

    # Ask the player if they want to continue their mystical adventure
    choice = yes_no_input("Do you wish to continue your exploration of the mystical world? (yes/no):")