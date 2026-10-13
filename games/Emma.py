#final
HP = 0
atk = 0

physicaldefence = 0
magicresistance = 0
weapon_atk = 0  # extra attack from weapon


#GAMESTART
print("Let's start the game now!")
playerName = input("Please enter your name: ")

#CHOICEONE
characterType = input("Please type which character you want to be: 1. magician 2. knight 3. fairy")
if characterType == "magician":
    print("you chose magician")
    HP = 85
    atk = 12
    physicaldefence = 15
    magicresistance = 15
    print("HP = 85")
    print("atk = 12")
    print("physicaldefence = 15")
    print("magicresistance = 15")

elif characterType == "knight":
    print("you choose knight")
    HP = 110
    atk = 12
    physicaldefence = 25
    magicresistance = 5
    print("HP = 110")
    print("atk = 12")
    print(" physicaldefence = 25")
    print(" magicresistance = 5")

elif characterType == "fairy":
    print("you choose fairy")
    HP = 60
    atk = 22
    physicaldefence = 5
    magicresistance = 25
    print("HP = 60")
    print("atk = 22")
    print("physicaldefence = 5")
    print("magicresistance = 25")
else:
    print("Invalid choice! You get default stats.")
    HP = 70
    atk = 10
    physicaldefence = 10
    magicresistance = 10

print("")
print("")
print("now you can choose a enemy to fight with")
print("1. Goblin")
print("2. Dark Wizard")
print("3. Stone Golem")
first = input(" please enter the number")

if first == "1":
    print("start fight with Goblin")
    enemyHP = 70
    enemyAtk = 10
    weapon_gain = 4
    weapon_name = "Rusty Dagger"
elif first == "2":
    print("start fight with Dark Wizard")
    enemyHP = 65
    enemyAtk = 16
    weapon_gain = 7
    weapon_name = "Magic Staff"
elif first == "3":
    print("start fight with Stone Golem")
    enemyHP = 120
    enemyAtk = 8
    weapon_gain = 10
    weapon_name = "Rock Cleaver"
else:
    print("Wrong input, fighting Goblin by default")
    enemyHP = 70
    enemyAtk = 10
    weapon_gain = 4
    weapon_name = "Rusty Dagger"


while HP > 0 and enemyHP > 0:
    total_atk = atk + weapon_atk
    damage = total_atk
    enemyHP -= damage
    print(f"\n{playerName} attack! Deal {damage} damage. Enemy HP: {enemyHP}")
    if enemyHP <= 0:
        break

    dmg_taken = max(0, enemyAtk - physicaldefence//2)
    HP -= dmg_taken
    print(f"Enemy attack! You take {dmg_taken} damage. Your HP: {HP}")

#battle result
if HP > 0:
    print(f"\nCongratulation {playerName}! You win the battle!")
    weapon_atk += weapon_gain
    print(f"You got weapon: {weapon_name}! Attack +{weapon_gain}")
    print(f"Your total attack now: {atk + weapon_atk}")
else:
    print(f"\n{playerName} died... Game Over.")
