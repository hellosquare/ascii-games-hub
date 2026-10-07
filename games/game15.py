#ThirdCheckpoint - Ms. Christine
#check that enemy health doesn't go in the negatives
#add error checking

#-----CONSTANT-----#
EnemyStartingHealth = 50
BossStartingHealth = 200
FriendStartingHealth = 75

#-----PLAYER VARIABLE-----#
playerName = ""
playerSuperpower = ""
health = 100
playerBackground = ""
playerAttack = 50
health = 100

import sys
import time

def typewriter(text, speed=0.04):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
    print()

typewriter("Welcome to the game!")
playerName = input("Please enter your name: ")
playerSuperpower = input("Please choose your superpower, Fire ball or Spider web? Please type in 1 or 2: ")


if playerSuperpower == "1":
    playerSuperpower = "Fire ball"
    print(r'''
  ⠀⠀⠀⠀⠀⠀⢱⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣧⠀⠀⠀
⠀⠀⠀⠀⡀⢠⣿⡟⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⣳⣼⣿⡏⢸⣿⣿⣿⢀⠀
⠀⠀⠀⣰⣿⣿⡿⠁⢸⣿⣿⡟⣼⡆
⢰⢀⣾⣿⣿⠟⠀⠀⣾⢿⣿⣿⣿⣿
⢸⣿⣿⣿⡏⠀⠢⡄⠃⠸⣿⣿⣿⡿
⢳⣿⣿⣿⠀⠀⠀⠈⢆⠀⢹⣿⡿⡁
⠀⠹⣿⣿⡄⠀⠀⠀⠀⠳⣠⣿⡞⠁
⠀⠀⠈⠛⢿⣄⠀⠀⠀⣠⠟⡋⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠂⡀
''')
    typewriter("You have chosen Fire ball as your superpower!")
    typewriter("Your name is " + playerName + " and your superpower is " + playerSuperpower + ".")
    typewriter("Your starting health is " + str(health) + ".")
    typewriter("Once the health reaches 0, you will lose the game.")
    typewriter("==============================================")
    typewriter("                START GAME                    ")
    typewriter("==============================================")
    
elif playerSuperpower == "2":
    playerSuperpower = "Spider web"
    print(r'''
     \_______/
 `.,-'\_____/`-.,'
  /`..'\ _ /`.,'\
 /  /`.,' `.,'\  \
/__/__/     \__\__\__
\  \  \     /  /  /
 \  \,'`._,'`./  /
  \,'`./___\,'`./
 ,'`-./_____\,-'`.
     /       \
    ''')
    typewriter("You have chosen Spider web as your superpower!")
    typewriter("==============================================")
    typewriter("                START GAME                    ")
    typewriter("==============================================")
    typewriter("Your name is " + playerName + " and your superpower is " + playerSuperpower + ".")
    typewriter("Your starting health is " + str(health) + ".")
    typewriter("Once the health reaches 0, you will lose the game.")
else:
    print("Invalid choice. Please restart the game and choose either 1 or 2.")

#-----COMBAT-----#
def fight_enemy(enemy_name, enemy_health, victory_message, friend_name=""):
    global health

    print("\nA " + enemy_name + " is blocking your path!")
    print("The enemy has " + str(enemy_health) + " health.")

    while enemy_health > 0 and health > 0:
        typewriter("\nChoose your move:")
        typewriter("1. Power attack - reliable damage")
        typewriter("2. Use the surroundings - clever damage and dodge")
        typewriter("3. Superpower combo - your most creative move")
        typewriter("4. Heal - restore up to 30 health")
        typewriter("5. Run away")
        action = input("Enter 1, 2, 3, 4, or 5: ")

        enemy_can_attack = True
        if action == "1":
            enemy_health -= playerAttack
            typewriter("Your power attack hits! Enemy health: " + str(max(0, enemy_health)))
        elif action == "2":
            enemy_health -= 35
            enemy_can_attack = False
            typewriter("You trick the enemy into crashing into the environment!")
            typewriter("Enemy health: " + str(max(0, enemy_health)))
        elif action == "3":
            if playerSuperpower == "Fire ball":
                enemy_health -= 75
                typewriter("You bounce a Fire ball off the scenery for a huge combo!") #this makes your enemy health negative 
            else:
                enemy_health -= 40
                enemy_can_attack = False
                typewriter("You wrap the enemy in a Spider web trap and pin it down!")
            typewriter("Enemy health: " + str(max(0, enemy_health)))
        elif action == "4":
            previous_health = health
            health = min(100, health + 30)
            typewriter("You heal for " + str(health - previous_health) + " health. Your health is now " + str(health) + ".")
        elif action == "5":
            typewriter("You escape before the enemy can attack.")
            typewriter("YOU LOST!")
            return False
        
        if enemy_health <= 0:
            typewriter(victory_message)
            return True

        if friend_name:
            enemy_health -= 25
            typewriter(friend_name + " distracts the enemy and helps you land a hit!")
            typewriter("The enemy's health is now " + str(max(0, enemy_health)) + ".")
            if enemy_health <= 0:
                typewriter(victory_message)
                return True

        if enemy_can_attack:
            health -= 20
            typewriter("The enemy attacks! Your health is now " + str(max(0, health)) + ".")
        else:
            typewriter("You avoid the enemy's counterattack!")

    typewriter("You collapsed before defeating the enemy.")
    typewriter("YOU LOST!")
    return False


#-----EVENT 1-----#
if playerSuperpower in ("Fire ball", "Spider web"):
    print(r'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⢠⢤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠔⠒⠒⠲⠎⠀⠀⢹⡃⢀⣀⠀⠑⠃⠀⠈⢀⠔⠒⢢⠀⠀⠀⡖⠉⠉⠉⠒⢤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠚⠙⠒⠒⠒⠤⡎⠀⠀⠀⠀⢀⣠⣴⣦⠀⠈⠘⣦⠑⠢⡀⠀⢰⠁⠀⠀⠀⠑⠰⠋⠁⠀⠀⠀⠀⠀⠈⢦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⢰⠃⠀⣀⣀⡠⣞⣉⡀⡜⡟⣷⢟⠟⡀⣀⡸⠀⡎⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀
⢰⠂⠀⠀⠀⠀⠀⠀⠀⣗⠀⠀⢀⣀⣀⣀⣀⣀⣓⡞⢽⡚⣑⣛⡇⢸⣷⠓⢻⣟⡿⠻⣝⢢⠀⢇⣀⡀⠀⠀⠀⢈⠗⠒⢶⣶⣶⡾⠋⠉⠀⠀⠀⠀⠀
⠈⠉⠀⠀⠀⠀⠀⢀⠀⠈⠒⠊⠻⣷⣿⣚⡽⠃⠉⠀⠀⠙⠿⣌⠳⣼⡇⠀⣸⣟⡑⢄⠘⢸⢀⣾⠾⠥⣀⠤⠖⠁⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢀⠀⠀
⠀⠀⠀⢰⢆⠀⢀⠏⡇⠀⡀⠀⠀⠀⣿⠉⠀⠀⠀⠀⠀⠀⠀⠈⢧⣸⡇⢐⡟⠀⠙⢎⢣⣿⣾⡷⠊⠉⠙⠢⠀⠀⠀⠀⠀⢸⡇⢀⠀⠀⠀⠀⠈⠣⡀
⠀⠀⠀⠘⡌⢣⣸⠀⣧⢺⢃⡤⢶⠆⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣟⠋⢀⠔⣒⣚⡋⠉⣡⠔⠋⠉⢰⡤⣇⠀⠀⠀⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠸
⠀⠀⠀⠀⠑⢄⢹⡆⠁⠛⣁⠔⠁⠀⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣿⢠⡷⠋⠁⠀⠈⣿⡇⠀⠀⠀⠈⡇⠉⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠑⣦⡔⠋⠁⠀⠀⠀⣿⠀⠀⢠⡀⢰⣼⡇⠀⡀⠀⠀⣿⠀⠁⠀⠀⠀⠀⣿⣷⠀⠀⠀⠀⡇⠀⠀⢴⣤⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⡀⠀⢨⣧⡿⠋⠀⠘⠛⠀⠀⣿⠀⠀⢀⠀⠀⠀⣿⣿⠀⠀⠀⠀⢲⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⢸⡧⡄⠀⠹⣇⡆⠀⠀⠀⠀⠀⣿⠀⢰⣏⠀⣿⣸⣿⣿⠀⠀⠀⠀⣼⠀⠀⠰⠗⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⢸⡇⣷⣛⣦⣿⢀⠈⠑⠀⢠⡆⣿⠐⢠⣟⠁⢸⠸⣿⣿⢱⣤⢀⠀⣼⠀⠀⢀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⢀⠀⠀⠀⢸⡇⠘⠫⣟⡇⠊⣣⠘⠛⣾⡆⢿⠀⠙⣿⢀⣘⡃⣿⣿⡏⠉⠒⠂⡿⠀⠰⣾⡄⠀⢸⡟⣽⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣿⡇⠀⠘⣾⠀⠀⢸⡇⢸⣇⡙⠣⠀⣹⣇⠀⠈⠧⢀⣀⣀⡏⣸⣿⣇⢹⣿⡇⢴⣴⣄⣀⡀⢰⣿⡇⠀⢸⣇⢿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠓⠁⠈⠻⢷⠾⠦⠤⠬⣅⣹⣿⣖⣶⣲⣈⡥⠤⠶⡖⠛⠒⠛⠁⠉⠛⠮⠐⢛⡓⠒⢛⠚⠒⠒⠒⠛⣚⣫⡼⠿⠿⣯⠛⠤⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⡉⠉⠁⠀⠀⠘⠓⠀⠀⠀⠀⠀⣀⣞⡿⡉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')
    typewriter("\nThe forest is unusually quiet, and a trail of footprints leads you deeper between the trees.")
    typewriter("A wild enemy jumps from the bushes and guards the only path forward!")
    if fight_enemy("forest beast", EnemyStartingHealth, "You defeated the forest beast with style!"):
        typewriter("Behind the beast, you discover a torn map with two mysterious paths marked on it.")

#-----EVENT 2-----#
if health > 0 and playerSuperpower == "Fire ball":
    print(r'''
 [][][] /""\ [][][]
  |::| /____\ |::|
  |[]|_|::::|_|[]|
  |::::::__::::::|
  |:::::/||\:::::|
  |:#:::||||::#::|
  ''')
    typewriter("The map leads you to a castle surrounded by smoke and broken banners.")
    typewriter("A message on the gate says, 'The princess is trapped in the highest tower.'")
    typewriter("At the castle gate, an armored guard blocks your rescue mission.")
    if fight_enemy("castle guard", EnemyStartingHealth, "You defeated the guard and can enter the castle!"):
        typewriter("You race up the tower and find the princess locked behind an iron door.")
        typewriter("With one powerful Fire ball, you melt the lock and free her!")
        typewriter("The princess thanks you for your bravery, and the kingdom celebrates your heroic rescue!")
    elif health > 0:
        typewriter("You leave the castle behind, but the princess is still waiting in the tower.")
elif health > 0 and playerSuperpower == "Spider web":
    print(r'''
┈┈┈┈▅┈┈┈┈┈▅ ┈┈
┈┈┈▕┈┈┈╱╲▕▀┈┈┈
┈┈┈╱╲┈┈▏▕╱╲┈┈┈
┈┈┈▏▕╱╲▏▎▏▕╱╲┈▃
┈╱╲▏▎▅▂▅▂▏▎▏▎▏▏
▂▏▎▏▕╭┳┳╮▏┊▏▕╱╲
▏▏┊▏▎┃┊┊┃▏▎▏▎▏▕
▇▆▅▃▂┻┻┻┻▂▃▅▆▇▉⛫⛫
    ''')
    typewriter("The map leads you to an abandoned mansion covered in vines and secret symbols.")
    typewriter("A legend says that a lost treasure is hidden beneath the mansion's oldest room.")
    typewriter("Inside, a treasure guardian blocks the staircase to the underground vault.")
    if fight_enemy("treasure guardian", EnemyStartingHealth, "You defeated the guardian and can search for treasure!"):
        event2_complete = True
        typewriter  ("The guardian drops a silver key, but warns you that a giant beast protects the vault.")
    elif health > 0:
        typewriter("You escape the mansion, but its treasure remains hidden beneath the floor.")

#-----EVENT 3-----#
if health > 0 and event2_complete:
    if playerSuperpower == "Fire ball":
        typewriter("You use the key to enter the castle tower, but a giant stone beast blocks the stairs.")
        typewriter("Your friend Maya arrives with a shield and promises to help you reach the princess.")
        event3_complete = fight_enemy(
            "giant stone beast", 125,
            "With Maya's help, you defeat the giant beast and reach the top of the tower!",
            "Maya"
        )
    else:
        typewriter("You use the key to open the staircase, but a giant vault beast guards the tunnel below.")
        typewriter("Your friend Leo arrives with a lantern and promises to help you find the treasure.")
        event3_complete = fight_enemy(
            "giant vault beast", 125,
            "With Leo's help, you defeat the giant beast and reach the hidden vault!",
            "Leo"
        )

#-----EVENT 4-----#
if health > 0 and event3_complete:
    if playerSuperpower == "Fire ball":
        
        typewriter("At the top of the tower, the final boss appears: the Shadow King!")
        typewriter("He has captured the princess and plans to cover the kingdom in darkness.")
        if fight_enemy("Shadow King", BossStartingHealth, "You defeated the Shadow King!"):
            typewriter("You unlock the final cell with your Fire ball and rescue the princess!")
            typewriter("The kingdom is safe, and you become its legendary hero!")
            typewriter("YOU WIN!")
    else:
        typewriter("At the center of the vault, the final boss appears: the Treasure Dragon!")
        typewriter("It guards the legendary treasure and shakes the mansion with a mighty roar.")
        if fight_enemy("Treasure Dragon", BossStartingHealth, "You defeated the Treasure Dragon!"):
            typewriter("You open the final chest and discover gold, jewels, and an ancient crown!")
            typewriter("You found the legendary treasure and became the richest adventurer alive!")
            typewriter("YOU WIN!")
