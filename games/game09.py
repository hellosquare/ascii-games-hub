#Third Checkpoint - Ms. Christine - check the comments
#your if statements are a bit confusing - let's edit some of them for clarity - it should be if == (option 1) or (option 2) rather than if in (option 1 , option 2) for readability
#remember to add your art

#------imports------#
import time
TYPEWRITER_SPEED = 0.03

#------functions------#
def typewriter(message):
    for character in message:
        print(character, end="", flush=True)
        time.sleep(TYPEWRITER_SPEED)
    print()


def restart_story():
    typewriter("A hidden gate opens.")
    typewriter("An old guide says, 'You can try again.'")
    choice = input("Try again? Type 'restart' or 'quit': ").strip().lower()
    if choice == "restart":
        typewriter("You go through the gate and start again.")
        return True
    typewriter("You leave the gate. The game ends.")
    return False

#------constants------#
ENEMY_STARTING_HEALTH = 100
BOSS_STARTING_HEALTH = 200
TEAM_STARTING_HEALTH = 75
HEALTH_POTION = 45


def start_game():
    #------variables------#
    global playerName, superpower, health, event1_won
    playerName = ""
    superpower = ""
    health = 100
    event1_won = False

    typewriter("Welcome to the game!")
    playerName = input("What is your name: ")
    characterchoice = input("Pick a wizard or a hero with a power. Type 1 or 2: ")
    typewriter("==============================================================")
    typewriter("                    PICK YOUR HERO                             ")
    typewriter("==============================================================")

    while True:
        if characterchoice == "1":
            superpower = "Wizard"
            typewriter("You picked a wizard!")
            break
        elif characterchoice == "2":
            superpower = "Super power"
            typewriter("You picked a hero with a power!")
            break
        else:
            typewriter("Invalid input. Please type 1 or 2.")
            characterchoice = input("Pick a wizard or a hero with a power. Type 1 or 2: ")

    typewriter("Your name is " + playerName + ". You picked: " + superpower + ".")
    typewriter("You have " + str(health) + " health.")
    typewriter("You can play this trip again any time.")
    typewriter("===============================================================")
    typewriter("                       START THE GAME!                         ")
    typewriter("===============================================================")

    #----EVENT 1----#
    if superpower == "Wizard":
        typewriter("You reach a town. Bad guys are there!")
        typewriter("The bad guys have " + str(ENEMY_STARTING_HEALTH) + " health.")

        while True:
            action = input("Do you fight alone or make a team? Type 'alone' or 'team': ").strip().lower()
            if action in ("alone", "attack alone"):
                typewriter("You chose to fight alone.")
                typewriter("The bad guys are too strong. You must leave the town.")
                typewriter("An old man points to a gate and says, 'You can try again.'")
                if restart_story():
                    start_game()
                    return
                return
            elif action in ("team", "make a team"):
                typewriter("You join a team of wizards!")
                typewriter("You beat the bad guys and save the town.")
                typewriter("You go on to Event 2!")
                event1_won = True
                break
            else:
                typewriter("Invalid choice. Please type 'alone' or 'team'.")

    if superpower == "Super power":
        typewriter("You reach a town. Bad guys are there!")
        typewriter("The bad guys have " + str(ENEMY_STARTING_HEALTH) + " health.")

        while True:
            action = input("Do you fight or run away? Type 'fight' or 'run': ").strip().lower()
            if action in ("fight"):
                typewriter("You chose to fight.")
                typewriter("You beat the bad guys and save the town.")
                event1_won = True
                break
            elif action in ("run"):
                typewriter("You chose to run away.")
                typewriter("You get away, but the bad guys take the town.")
                typewriter("You find a path and can try again.")
                if restart_story():
                    start_game()
                    return
                return
            else:
                typewriter("Invalid choice. Please type 'fight' or 'run'.")

    #----EVENT 2----#
    if not event1_won:
        return

    typewriter("A big boss is up ahead!")
    if superpower == "Wizard":
        typewriter("Your team gets ready to fight.")
    else:
        typewriter("You get ready to fight.")

    while True:
        action = input("Will you fight or ask your friend to help? Type 'fight' or 'help': ").strip().lower()
        if action in ("fight", "attack"):
            typewriter("You fight the boss and win!")
            typewriter("The boss runs away. A kind traveler joins you.")
            break
        elif action in ("ask friends for help", "friends", "help"):
            typewriter("A kind traveler helps you fight.")
            typewriter("Together, you beat the boss!")
            break
        else:
            typewriter("Please type 'fight' or 'help'.")

    #----EVENT 3----#
    typewriter("A kind traveler goes with you to an old stone hall.")
    typewriter("A big dragon blocks the way! It has " + str(BOSS_STARTING_HEALTH) + " health.")
    while True:
        action = input("Type 'attack' to hit the dragon, or 'use my power' to use your special skill: ").strip().lower()
        if action in ("attack", "fight"):
            typewriter("You run at the dragon and hit it!")
            typewriter("Your friend helps. You beat the dragon!")
            break
        elif action in ("use my power", "special power", "power", "spell"):
            if superpower == "Wizard":
                typewriter("You cast a spell at the dragon!")
            else:
                typewriter("You use your power on the dragon!")
            typewriter("Your friend helps. You beat the dragon!")
            break
        else:
            typewriter("Please type 'attack' to hit the dragon or 'use my power' to use your special skill.")

    typewriter("You look in the old hall and find a key.")
    typewriter("You go on to Event 4!")

    #----EVENT 4----#
    typewriter("The key opens a cave door.")
    typewriter("A rock monster jumps out!")
    while True:
        action = input("Type 'hit' to hit the rock monster, or 'use my power' to use your special skill: ").strip().lower()
        if action in ("hit", "attack", "fight"):
            typewriter("You hit the rock monster!")
            typewriter("Your friend helps you beat it.")
            break
        elif action in ("use my power", "power", "special power", "spell"):
            if superpower == "Wizard":
                typewriter("You use a spell to crack the rock monster.")
            else:
                typewriter("You use your power to crack the rock monster.")
            typewriter("Your friend helps you beat it.")
            break
        else:
            typewriter("Please type 'hit' to hit the rock monster or 'use my power' to use your special skill.")
    typewriter("You find a map in the cave.")
    typewriter("The map shows the way to a tall tower.")
    typewriter("You go on to Event 5!")

    #----EVENT 5----#
    typewriter("At the tower, a huge beast guards a treasure chest.")
    typewriter("You and your friend get ready for one last fight.")
    while True:
        action = input("Type 'hit' to hit the beast, or 'use my power' to use your special skill: ").strip().lower()
        if action in ("hit", "attack", "fight"):
            typewriter("You hit the beast while your friend keeps it busy.")
            typewriter("Together, you beat the beast!")
            break
        elif action in ("use my power", "power", "special power", "spell"):
            if superpower == "Wizard":
                typewriter("You use a spell to stop the beast.")
            else:
                typewriter("You use your power to stop the beast.")
            typewriter("Your friend helps you win the fight!")
            break
        else:
            typewriter("Please type 'hit' to hit the beast or 'use my power' to use your special skill.")

    typewriter("You open the chest and find gold!")
    typewriter("You win! Great job, " + playerName + "!")


start_game()
