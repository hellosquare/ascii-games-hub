import random
import sys
import time

def slow(text):
    print(text)
    time.sleep(1.2)

health = 1000
attack = 100
coins = random.randint(100, 150)
potions = random.randint(1, 40)
sword = False

def check_death():
    global health
    if health <= 0:
        slow("You've run out of health, better luck next time!")
        sys.exit()

name = input("Welcome traveler, you are now in a magical land. Your objective is to defeat the demon king, what is your name : ")
print("Alright ", name, " your journey begins now, you have ", health, " health, ", attack, " attack power, and ", coins, " coins, as well as ",potions, " potions to heal yourself.")

if name.lower() == "adrian":
    health += 10000
    attack += 10000
    coins += 10000
    slow("You have been given a special boost for being the creator of this game! You now have " + str(health) + " health, " + str(attack) + " attack power, and " + str(coins) + " coins.")

# ---- Monster 1 ----
slow(r"""
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠟⣧⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣴⣞⡛⠋⠉⠉⠉⠙⠛⠓⠶⣤⣀⠀⠀⠀⣼⠃⠼⣧⣀⣠⣤⣤⣤⣤⣄⣀⣠⡟⠀⢹⡇⠀⣤⣶⠛⠛⠉⠉⠉⠉⠉⠉⠙⠛⠲⢦⣄⡀⠀⠀⠀⠀⠀
⠉⠉⠉⠙⠳⣄⠀⠀⠀⠀⠀⠀⢈⣽⠗⠀⢀⣿⡀⠷⠛⠉⠁⠀⠀⠀⠀⠈⠿⠋⠀⠀⣸⠇⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⣦⡀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣼⠁⠀⢠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠟⢷⡀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣬⣻⣦⠀
⠀⠀⠀⠀⣰⡏⠀⠀⠀⠀⠀⠀⣿⠀⣰⢟⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡄⠀⣾⡀⠀⠀⠀⠀⠀⠀⠀⢸⠋⠀⠀⠀⠀⠀⠀⠙⠃
⠀⠀⠀⡴⠿⠖⠒⠶⣦⡀⠀⠀⠹⣧⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣼⠃⠁⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⣷⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⢠⣤⠾⠋⠁⠀⠀⠀⣠⡶⠒⠓⠶⢦⣄⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣤⠴⠶⣾⠀⠀⠀⠀⠀⢀⢻⠁⠀⠀⠈⠛⠁⠀⠀⠀⠀⠀⠀⠿⠳⢶⣦⣤⣀⠀⣿⠀⠀⠀⠀⠀⠈⠙⠷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠁⠀⠀⢹⡗⠀⠀⠀⠀⠛⠉⠉⠉⠙⠛⠶⣦⠄⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠉⠳⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢦⣤⣀⡀⠀⠀⠀⠀⠀⠀⣀⠀⠀⡶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣟⢻⡟⠛⠛⠛⠹⣦⢰⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀k
      
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠾⠃⠀⠀⠀⠀⠹⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      """)
choice1 = input("You encounter a monster, do you want to fight it or run away? (fight/run) : ")
if choice1.lower() == "fight":
    slow("You have chosen to fight the monster!")
    slow("The monster has 500 health and 50 attack power.")
    monster_health = 500
    while monster_health > 0:
        choice2 = input("Do you want to attack, use a potion, or flee? (attack/potion/flee) : ")
        if choice2.lower() == "attack":
            slow("You attack the monster!")
            monster_health -= attack
            if monster_health <= 0:
                slow("You have defeated the monster!")
                coins += random.randint(10, 50)
                slow("You have gained some coins! You now have " + str(coins) + " coins.")
                break
            slow("The monster now has " + str(monster_health) + " health left.")
            slow("The monster attacks you back!")
            health -= 50
            slow("You now have " + str(health) + " health left.")
            check_death()
        elif choice2.lower() == "potion":
            if potions > 0:
                health += 100
                potions -= 1
                slow("You used a potion and gained 100 health! You now have " + str(health) + " health left.")
            else:
                slow("You don't have any potions left!")
        elif choice2.lower() == "flee":
            slow("You have fled from the monster!")
            break
        else:
            slow("Invalid choice, please choose again.")
else:
    slow("You have chosen to run away from the monster.")

# ---- Strong monster ----
choice_strong = input("You encounter a strong monster, do you want to fight it or run away? (fight/run) : ")
if choice_strong.lower() == "fight":
    slow("You have chosen to fight the strong monster!")
    slow("The strong monster has 1000 health and 100 attack power.")
    strong_health = 1000
    while strong_health > 0:
        choice3 = input("Do you want to attack, use a potion, or flee? (attack/potion/flee) : ")
        if choice3.lower() == "attack":
            slow("You attack the strong monster!")
            strong_health -= attack
            if strong_health <= 0:
                slow("You have defeated the strong monster!")
                coins += random.randint(50, 100)
                slow("You have gained some coins! You now have " + str(coins) + " coins.")
                break
            slow("The strong monster now has " + str(strong_health) + " health left.")
            slow("The strong monster attacks you back!")
            health -= 100
            slow("You now have " + str(health) + " health left.")
            check_death()
        elif choice3.lower() == "potion":
            if potions > 0:
                health += 100
                potions -= 1
                slow("You used a potion and gained 100 health! You now have " + str(health) + " health left.")
            else:
                slow("You don't have any potions left!")
        elif choice3.lower() == "flee":
            slow("You have fled from the strong monster!")
            break
        else:
            slow("Invalid choice, please choose again.")
else:
    slow("You have chosen to run away from the strong monster.")

# ---- Toll bridge ----
toll = random.randint(101, 125)
slow("You encounter a toll bridge, you need to pay " + str(toll) + " coins to cross it.")
if coins >= toll:
    coins -= toll
    slow("You have paid the toll and crossed the bridge. You now have " + str(coins) + " coins left.")
else:
    slow("You don't have enough coins to pay the toll. You cannot cross the bridge.")
    sys.exit()

# ---- Shop ----
slow(r""" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣀⣀⣀⣀⣀⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣀⣀⣀⣀⣀⣀⡀⠀⠀
⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡤⡤⡤⡤⡤⡤⡤⡤⡤⡤⡄⠀⠀
⠀⠀⣿⣿⣿⣿⣿⢻ 
⠀⠈⠻⠿⠿⠋⣀⠈⠻⠿⠟⢁⡀⠙⠿⠿⠋⢀⡈⠻⠿⠟⠁⣀⠙⠿⠿⠟⠁⠀
⠀⢸⣷⣦⣶⣿⣿⣿⣶⣤⣶⣿⣿⣷⣦⣴⣾⣿⣿⣶⣤⣶⣿⣿⣿⣶⣴⣾⡇⠀
⠀⢸⣿⡏⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⡉⢹⣿⠉⣉⣉⣉⣉⣉⢹⣿⡇⠀
⠀⢸⣿⡇⣿⠉⢉⣩⣭⣽⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⠀⣿⣿⣿⣿⣿⢸⣿⡇⠀
⠀⢸⣿⡇⣿⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⠀⠿⠿⠿⠿⠿⢸⣿⡇⠀
⠀⢸⣿⡇⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⠀⠶⠶⠶⠶⠶⢸⣿⡇⠀
⠀⢸⣿⡇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⣿⠀⣶⣶⣶⣶⣶⢸⣿⡇⠀
⠀⢸⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⠀⣿⣿⣿⣿⣿⢸⣿⡇⠀
⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠉⠉⠉⠉⠉⠈⠉⠁⠀
      """)
shop_choice = input("You encounter a shop, do you want to buy a potion for 50 coins or a sword for 200 coins? (potion/sword/none) : ")
if shop_choice.lower() == "potion":
    if coins >= 50:
        coins -= 50
        potions += 1
        slow("You have bought a potion! You now have " + str(potions) + " potions and " + str(coins) + " coins left.")
    else:
        slow("You don't have enough coins to buy a potion.")
elif shop_choice.lower() == "sword":
    if coins >= 200:
        coins -= 200
        attack += 1000
        sword = True
        slow("You have bought a sword! Your attack power is now " + str(attack) + " and you have " + str(coins) + " coins left.")
    else:
        slow("You don't have enough coins to buy a sword.")
else:
    slow("You have chosen not to buy anything from the shop.")

# ---- Demon king (no fleeing — you must fight) ----
demon_choice = input("You encounter the demon king. There is no escape — you must fight! (fight) : ")
if demon_choice.lower() == "fight":
    slow("You have chosen to fight the demon king!")
    slow("The demon king has 2000 health and 200 attack power.")
    demon_health = 2000
    while demon_health > 0:
        choice4 = input("Do you want to attack or use a potion? (attack/potion) : ")
        if choice4.lower() == "attack":
            slow("You attack the demon king!")
            demon_health -= attack
            if demon_health <= 0:
                slow("You have defeated the demon king! Congratulations, you have completed your journey!")
                break
            slow("The demon king now has " + str(demon_health) + " health left.")
            slow("The demon king attacks you back!")
            health -= 200
            slow("You now have " + str(health) + " health left.")
            check_death()
        elif choice4.lower() == "potion":
            if potions > 0:
                health += 100
                potions -= 1
                slow("You used a potion and gained 100 health! You now have " + str(health) + " health left.")
            else:
                slow("You don't have any potions left!")
        else:
            slow("Invalid choice, please choose again.")
else:
    slow("You cannot run from the demon king! He strikes you down where you stand.")
    sys.exit()
