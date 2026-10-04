print("========================================")
print("              GAME 24")
print("========================================")
print()
print("This is a placeholder Python game.")
print("Replace this file with the student's code.")
print()

name = input("What is your name? ")
print()
print("Welcome, " + name + "!")

choice = input("Choose LEFT or RIGHT: ")

if choice.lower() == "left":
    print("You found a hidden path. Nice choice!")
elif choice.lower() == "right":
    print("You discovered a mysterious door...")
else:
    print("You wandered off the map!")
