import time

def slow(text):
    print(text)
    time.sleep(0.5)

def pause():
    input("\n[Press ENTER to continue] ")


#------CONSTANTS------

RABBIT_STARTING_HEALTH = 20
RABBIT_STARTING_DMG = 0

CRAB_STARTING_HEALTH = 100
CRAB_STARTING_DMG = 40

GOBLIN_STARTING_HEALTH = 150
GOBLIN_STARTING_DMG = 55

BUCK_STARTING_HEALTH = 120
BUCK_STARTING_DMG = 30

COBRA_STARTING_HEALTH = 220  
COBRA_STARTING_DMG = 90

GIANT_STARTING_HEALTH = 300
GIANT_STARTING_DMG = 100

WOLF_STARTING_HEALTH = 300
WOLF_STARTING_DMG = 90

ALLIGATOR_STARTING_HEALTH = 500
ALLIGATOR_STARTING_DMG = 100

DRAGON_STARTING_HEALTH = 1000
DRAGON_STARTING_DMG = 150


#------GAME LOOP------

while True:


    #------PLAYER VARIABLES------

    playername = ""
    characterType = ""
    weaponType = ""
    health = 0
    attackPower = 0


    #------GAME VARIABLES------

    spawnlocation = ""

    enemyName = ""
    enemyHealth = 0
    enemyAttackPower = 0


    #------TITLE SCREEN------

    while True:

        print()
        print("================================")
        slow("     WELCOME TO THE ADVENTURE")
        print("================================")
        print()

        print("1. Start")
        print("2. Quit")
        print()

        menuChoice = input("Choose Start or Quit (1/2): ").strip().lower()

        if menuChoice in ("2", "quit"):

            print()
            slow("Thanks for playing!")
            exit()

        elif menuChoice in ("1", "start"):

            print()
            slow("You are starting your adventure...")
            pause()
            break

        else:

            slow("Invalid choice. Please choose Start or Quit.")


    #------START ADVENTURE------

    slow("------START ADVENTURE------")
    print()
    slow("What is your name, adventurer? ")
    playername = input(">")
    slow("Hello, " + playername + "! Welcome to the Adventure!")


    #------CREATE YOUR CHARACTER------

    print()
    print("================================")
    slow("       CHOOSE YOUR CHARACTER")
    print("================================")
    print()

    print("1. Knight")
    print("2. Wizard")
    print("3. Elf")
    print()

    while True:

        characterChoice = input("Type 1, 2, or 3: ")

        if characterChoice == "1":

            characterType = "Knight"
            health = 120
            attackPower = 135
            weaponType = "Sword"

            break

        elif characterChoice == "2":

            characterType = "Wizard"
            health = 90
            attackPower = 140
            weaponType = "Wand"

            break

        elif characterChoice == "3":

            characterType = "Elf"
            health = 60
            attackPower = 145
            weaponType = "Bow"

            break

        else:

            print("Invalid choice. Please type 1, 2, or 3.")


    print()
    slow("You chose the " + characterType + "!")
    slow("Your weapon is the " + weaponType + ".")
    slow("Health: " + str(health))
    slow("Attack: " + str(attackPower))

    pause()


    #------CHOOSE SPAWN LOCATION------

    print()
    print("================================")
    slow("      CHOOSE YOUR LOCATION")
    print("================================")
    print()

    print("1. Forest - Easy")
    print("2. Swamp - Medium")
    print("3. Volcano - Hard")
    print()

    while True:

        spawnChoice = input("Type 1, 2, or 3: ")

        if spawnChoice == "1":

            spawnlocation = "Forest"

            enemyName = "Rabbit"
            enemyHealth = RABBIT_STARTING_HEALTH
            enemyAttackPower = RABBIT_STARTING_DMG

            break

        elif spawnChoice == "2":

            spawnlocation = "Swamp"

            enemyName = "Crab"
            enemyHealth = CRAB_STARTING_HEALTH
            enemyAttackPower = CRAB_STARTING_DMG

            break

        elif spawnChoice == "3":

            spawnlocation = "Volcano"

            enemyName = "Goblin"
            enemyHealth = GOBLIN_STARTING_HEALTH
            enemyAttackPower = GOBLIN_STARTING_DMG

            break

        else:

            print("Invalid choice. Please type 1, 2, or 3.")


    print()
    slow("You have entered the " + spawnlocation + "!")
    pause()


    #------FIRST ENEMY------

    print()
    slow("You hear something moving...")
    pause()

    slow("A " + enemyName + " appears!")
    slow("It has " + str(enemyHealth) + " HP.")

    pause()


    #------FIRST BATTLE------

    print()
    print("================================")
    slow("          BATTLE")
    print("================================")
    print()

    while health > 0 and enemyHealth > 0:

        print()
        print("Your HP: " + str(health))
        print(enemyName + " HP: " + str(enemyHealth))

        pause()

        slow("You attack the " + enemyName + " with your " + weaponType + "!")
        enemyHealth = enemyHealth - attackPower

        if enemyHealth <= 0:

            enemyHealth = 0

            print()
            slow("You defeated the " + enemyName + "!")
            pause()
            break

        print()
        slow(enemyName + " attacks you!")

        health = health - enemyAttackPower

        if health <= 0:

            health = 0

            print()
            slow("You have been defeated!")
            pause()
            break

        slow("Your HP is now " + str(health) + ".")
        pause()


    #------CHECK FIRST BATTLE------

    if health > 0:

        print()
        print("================================")
        slow("     FIRST BATTLE COMPLETE")
        print("================================")
        print()

        slow("You survived your first battle!")
        pause()


        #------TREASURE CHEST------

        slow("You continue deeper into the " + spawnlocation + "...")
        pause()

        slow("You discover something shining in the distance.")
        pause()

        slow("It's a treasure chest!")
        pause()

        slow("You open the chest...")
        pause()

        slow("Inside is a mysterious bracelet!")
        slow("The bracelet gives you +100 attack and +100 HP!")

        attackPower = attackPower + 100
        health = health + 100

        print()
        slow("Your attack is now: " + str(attackPower))
        slow("Your HP is now: " + str(health))

        pause()


        #------SECOND ENEMY------

        if spawnlocation == "Forest":

            enemyName = "Buck"
            enemyHealth = BUCK_STARTING_HEALTH
            enemyAttackPower = BUCK_STARTING_DMG

        elif spawnlocation == "Swamp":

            enemyName = "Cobra"
            enemyHealth = COBRA_STARTING_HEALTH
            enemyAttackPower = COBRA_STARTING_DMG

        elif spawnlocation == "Volcano":

            enemyName = "Giant"
            enemyHealth = GIANT_STARTING_HEALTH
            enemyAttackPower = GIANT_STARTING_DMG


        print()
        slow("You suddenly hear a loud noise...")
        pause()

        slow("A " + enemyName + " appears!")
        slow("It has " + str(enemyHealth) + " HP.")

        pause()


        #------SECOND BATTLE------

        print()
        print("================================")
        slow("         SECOND BATTLE")
        print("================================")
        print()

        while health > 0 and enemyHealth > 0:

            print()
            print("Your HP: " + str(health))
            print(enemyName + " HP: " + str(enemyHealth))

            pause()

            slow("You attack the " + enemyName + "!")
            enemyHealth = enemyHealth - attackPower

            if enemyHealth <= 0:

                enemyHealth = 0

                print()
                slow("You defeated the " + enemyName + "!")
                pause()
                break

            print()
            slow(enemyName + " attacks you!")

            health = health - enemyAttackPower

            if health <= 0:

                health = 0

                print()
                slow("You have been defeated!")
                pause()
                break

            slow("Your HP is now " + str(health) + ".")
            pause()


    #------CHECK SECOND BATTLE------

    if health > 0:

        print()
        print("================================")
        slow("     SECOND BATTLE COMPLETE")
        print("================================")
        print()

        slow("You defeated the " + enemyName + "!")
        pause()


        #------ENEMY REWARD------

        if enemyName == "Buck":

            slow("The Buck drops a strange horn.")
            pause()

            slow("You received the Buck Horn!")
            slow("The Buck Horn gives you +50 attack!")

            attackPower = attackPower + 50

        elif enemyName == "Cobra":

            slow("The Cobra drops a mysterious object.")
            pause()

            slow("You received a Poison Enchantment!")
            slow("The Poison Enchantment gives you +150 attack!")

            attackPower = attackPower + 150

        elif enemyName == "Giant":

            slow("The Giant drops a giant piece of armor.")
            pause()

            slow("You received Giant Armor!")
            slow("The Giant Armor gives you +200 HP!")

            health = health + 200


        print()
        slow("Your attack is now: " + str(attackPower))
        slow("Your HP is now: " + str(health))

        pause()


        #------FINAL STAT UPGRADE------

        slow("You feel a powerful energy surrounding you.")
        pause()

        slow("Your final upgrade gives you +100 attack and +100 HP!")

        attackPower = attackPower + 100
        health = health + 100

        print()
        slow("Your attack is now: " + str(attackPower))
        slow("Your HP is now: " + str(health))

        pause()


        #------FINAL ENEMY------

        if spawnlocation == "Forest":

            enemyName = "Wolf"
            enemyHealth = WOLF_STARTING_HEALTH
            enemyAttackPower = WOLF_STARTING_DMG

        elif spawnlocation == "Swamp":

            enemyName = "Alligator"
            enemyHealth = ALLIGATOR_STARTING_HEALTH
            enemyAttackPower = ALLIGATOR_STARTING_DMG

        elif spawnlocation == "Volcano":

            enemyName = "Dragon"
            enemyHealth = DRAGON_STARTING_HEALTH
            enemyAttackPower = DRAGON_STARTING_DMG


        #------FINAL BOSS------

        print()
        print("================================")
        slow("        FINAL BATTLE")
        print("================================")
        print()

        slow("You reach the end of your journey...")
        pause()

        slow("The ground begins to shake.")
        pause()

        slow("A massive " + enemyName + " appears!")
        slow("It has " + str(enemyHealth) + " HP!")

        pause()

        slow("This is your final battle.")
        slow("Defeat the " + enemyName + " to complete your adventure!")

        pause()


        #------FINAL BATTLE------

        while health > 0 and enemyHealth > 0:

            print()
            print("Your HP: " + str(health))
            print(enemyName + " HP: " + str(enemyHealth))

            pause()

            slow("You attack the " + enemyName + "!")
            enemyHealth = enemyHealth - attackPower

            if enemyHealth <= 0:

                enemyHealth = 0

                print()
                slow("You defeated the " + enemyName + "!")
                pause()
                break

            print()
            slow(enemyName + " attacks you!")

            health = health - enemyAttackPower

            if health <= 0:

                health = 0

                print()
                slow("The " + enemyName + " defeated you!")
                pause()
                break

            slow("Your HP is now " + str(health) + ".")
            pause()


        #------FINAL RESULT------

        if health > 0:

            print()
            print("================================")
            slow("           YOU WIN!")
            print("================================")
            print()

            slow("Congratulations, " + playername + "!")
            pause()

            slow("You defeated the " + enemyName + "!")
            pause()

            slow("You have completed your adventure!")
            pause()

            print()
            print("Character: " + characterType)
            print("Weapon: " + weaponType)
            print("Final HP: " + str(health))
            print("Final Attack: " + str(attackPower))
            print()

            slow("You are a true adventurer!")
            pause()


        else:

            print()
            print("================================")
            slow("          GAME OVER")
            print("================================")
            print()

            slow("You were defeated by the " + enemyName + ".")
            pause()

            slow("Better luck next time, " + playername + "!")


    else:

        print()
        print("================================")
        slow("          GAME OVER")
        print("================================")
        print()

        slow("Your adventure has ended.")
        pause()

        slow("Better luck next time, " + playername + "!")


    #------PLAY AGAIN------

    print()
    while True:

        playAgain = input("Would you like to play again? (yes/no): ").strip().lower()

        if playAgain in ("yes"):

            slow("Restarting your adventure...")
            break   

        elif playAgain in ("no"):

            slow("Thanks for playing the Adventure Game!")
            exit()

        else:

            slow("Invalid choice. Please type yes or no.")
