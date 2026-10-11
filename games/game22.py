import random
import time

# VARIABLES
playerhp = 100
playermaxhp = 100
Dmax = 100
Dcurrent = 0

print("===== Cooking Luck Game =====")
print(f"Your HP: {playerhp}/{playermaxhp}")

fish = str("fish")
chicken = str("chicken")
noodle = str("noodle")
sandwich = str("sandwich")
beef = str("beef")
hotpot = str("hotpot")

chance = 6-*++
+3+

.

while chance > 0 and playerhp > 0:
    print("\nAvailable food to cook:")
    print("1. Fish")
    print("2. Chicken")
    print("3. Noodle")
    print("4. Sandwich")
    print("5. Beef")
    print("6. Hotpot")

    choice = input("\nEnter the food you want to cook (name): ").lower()
    if choice.lower() == fish or choice.lower() == chicken or choice.lower() == noodle or choice.lower() == beef or choice.lower() == hotpot or choice.lower() == sandwich:
        time.sleep(0.5)
        result = random.choice(["cooked", "overcooked"])

        if result == "cooked":
            print(f"{choice} is perfectly cooked! You gain HP.")
            playerhp = min(playerhp + 15, playermaxhp)
            break
        else:
            print(f"{choice} is overcooked! You lose HP.")
            playerhp -= 20
            chance -= 1
                
            print(f"Current HP: {playerhp}, Remaining chances: {chance}")
            
        if playerhp <= 0:
            print("\n Game over. Your HP dropped to 0.")
            break
        else:
            print("\n You finished cooking! You survived.")

        print("you now enter level 2 - battle with a boss chef")
        chefName = input("enter your chef name: ")

        battlechoice = random.choice(["fish","chicken","noodle","sandwich"])
        break
    else:
        print("invalid choice")

print("===== battlechoice =====")
print(f"Your HP: {playerhp}/{playermaxhp}")

while chance > 0 and playerhp > 0:
    print("\nAvailable food to cook:")
    print("1. Fish")
    print("2. Chicken")
    print("3. Noodle")
    print("4. Sandwich")
    print("5. Beef")
    print("6. Hotpot")
    break

choice = input("\nEnter the food you want to cook (name): ").lower()
time.sleep(0.5)
result = random.choice(["cooked", "overcooked"])
        
if result == "cooked":
    print(f"{choice} is perfectly cooked! You gain HP.")
    playerhp = min(playerhp + 15, playermaxhp)
else:
    print(f"{choice} is overcooked! You lose HP.")
    playerhp -= 20
    chance -= 1
        
    print(f"Current HP: {playerhp}, Remaining chances: {chance}")
    
if playerhp <= 0:
    print("\n Game over. Your HP dropped to 0.")
else:
    print("\n You finished cooking! You survived.")
