#final
#VARIABLES
name = ""
choice = ""
searchdrawer = ""
hearts = 3

print("Hello player")
print("Welcome to the game!")
print("First, you have to pick a room: ROOM 1 or ROOM 2") #here you want to have a choice - what choice do you want them to pick? you can make it so that if they pick the wrong choice, the game restarts

print("you have now entered ROOM 1")
print("WELCOME TO THE HAUNTED HOUSE")
print("Hello you have entered the game.")
name = input("Enter your character name: ")
print("Welcome" + name + ".You wake up in a dark house.") #also print the number of hearts you have at the start

print("Decision 1: Which bedroom do you enter?")
print("1. Bedroom 1 (Dark room)")
print("2. Bedroom 2 (Light switch)")
choice = input("Enter 1 or 2:")
if choice == "1":
    print("you have chosen to enter the dark room")
    print("BEDROOM 1")
    print("Mission: Find the battery for the flashlight in the dark room")
    print("Don't let the ghost get you!")
    searchdrawer = input("Do you search the drawers? (yes/no): ").lower()
    if searchdrawer == "yes":
        print("You found the battery!")
        battery = True
    if searchdrawer == "no":
        print("You decide not to search the drawers.")
        print("Mission: Search for a key to escape.")
        print("You see a Purple Door and a Green Door.")
        door_choice = input("Which door do you choose? (purple/green): ").lower()
        if door_choice == "purple":
            print("You open the purple door... a ghost jumps out!")
            print("You LOSE one heart.")
            hearts = hearts - 1
elif choice == "2":
    print("you have chosen to enter the light room")
    print("oh no you fell into a cliff")
    print("you lost all your heart")
    hearts = hearts - hearts
    print("GAME OVER - You lost all your hearts.")

else:
    print("Invalid choice. The ghost scared you away! Try again")
