#Final
import sys
import time
def type_text (text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 
#constants:
score=100
totalAttempts= 15

#variables
riddleSalmon = "" 
riddleRice= ""
riddleSeaweed= ""
riddleCucumber= ""
riddleAvocado= ""



#variables:
mistake = 0
hasSalmon = False
hasRice = False
hasSeaweed = False
hasCucumber = False
hasAvocado = False

#work today




type_text("Welcome to the kitchen of riddles")
print()
name = input("Enter your name to begin: ")
type_text(f"Hello, chef {name}!")
print()
type_text(" You have been chosen to cook for hungry customers using your skills!")
print()
type_text("Your ingredients are hidden in different magical words.")
print()
type_text("Solve riddles to discover what ingredients you need!")
print()
type_text("Your goal is to get 100 points by collecting all the ingredients. You will lose points for every wrong answer.")
print()
type_text("Can you make the perfect dish?")
print()


input("Press ENTER to begin!")

print()

#EventOne
type_text("A strange order has arrived...")

mistake = 0
MAX_MISTAKE=3

while mistake < MAX_MISTAKE: 

    type_text("Ingredient 1:")
    print()
    type_text("I swim through the ocean, but I'm not a whale. ")

    type_text("I have scales, but I am not a dragon.")

    type_text("I can travel upstream when it is time to lay my eggs.")

    type_text("What am I?")
    print()

    riddleSalmon = input("Enter your guess:").lower()

    print()
    if riddleSalmon == "salmon":
        type_text("Correct! You got salmon!")
        hasSalmon = True
        break
 
    else:
        mistake = mistake + 1
        type_text("Sorry, incorrect")
        print("Mistakes:" + str(mistake) + "/" + str(MAX_MISTAKE))

        if mistake == MAX_MISTAKE:
            type_text("Oops! You are out of attempts.")
            type_text("Salmon will not be added to the recipe.")

#ascii art for salmon
salmon=r"""
              /`·.¸
             /¸...¸`:·
         ¸.·´  ¸   `·.¸.·´)
        : © ):´;      ¸  {{
         `·.¸ `·  ¸.·´\  `·.¸)
             `·´
"""
print(salmon)
type_text("Moving on to the next ingredient...")
print()

mistake=0
MAX_MISTAKE=3

while mistake < MAX_MISTAKE:

    type_text("Ingredient 2:")
    print()
    type_text("I begin my life in a muddy field, and I grow in rows beside the water.")
    type_text("I am not wheat, but people grind and cook me before I become soft and fluffy.")
    type_text("What am I?")
    print()

    riddleRice = input("Enter your guess:").lower()
    print()
    if riddleRice == "rice": 
        type_text("Awesome! You got rice.")
        hasRice = True
        break

    else: 
        mistake = mistake + 1
        type_text("Sorry, incorrect")
        print("Mistakes:" + str(mistake) + "/" + str(MAX_MISTAKE))

        if mistake == MAX_MISTAKE:
            type_text("Oops! You are out of attempts.")
            type_text("Rice will not be added to the recipe.")

#ascii art for rice
rice = r"""
      .-""-.
    .' * * * `.
   / * * * * * \
  |-------------|
  |             |
   \           /
    `._______ .'
"""
print(rice)
type_text("Great! 2 ingredients down, 3 to go!")
print()

mistake=0
MAX_MISTAKE=3

while mistake < MAX_MISTAKE:
    type_text("Ingredient 3:")
    print()
    type_text("I grow beneath the waves, but I am not an animal.")
    type_text("I am usually green, brown, or almost black")
    type_text("You may find me wrapped around around food instead of growing in a garden.")
    type_text("What am I?")
    print()


    riddleSeaweed = input("Enter your guess:").lower()
    print()
    if riddleSeaweed == "seaweed": 
        type_text("WOW!You're a pro! You got seaweed!")
        hasSeaweed = True
        break

    else: 
        mistake = mistake + 1
        type_text("Sorry, incorrect")
        print("Mistakes:" + str(mistake) + "/" + str(MAX_MISTAKE))

        if mistake == MAX_MISTAKE:
            type_text("Uh-oh! You are out of attempts.")
            type_text("Seaweed will not be added to the recipe.")
print()
#ascii art for seaweed
seaweed = r"""
      __________
     /          \
    |            |
    |            |
    |            |
    |            |
    |            |
     \__________/
"""
print(seaweed)
type_text("Excellent! 2 more ingredients until you finish your dish!")
print()

mistake=0
MAX_MISTAKE=3

while mistake < MAX_MISTAKE:

    type_text("Ingredient 4:")
    print()
    type_text("I grow on a vine, but I am not a grape")
    type_text("I am long, green, and filled with tiny seeds")
    type_text("I am mosty water, and I make a satisfying crunch when you bite me")
    type_text("What am I?")
    print()


    riddleCucumber = input("Enter your guess:").lower()
    print()
    if riddleCucumber == "cucumber": 
        type_text("Yes! You got cucumber!")
        hasCucumber = True
        break

    else: 
        mistake = mistake + 1
        type_text("Sorry, incorrect")
        print("Mistakes:" + str(mistake) + "/" + str(MAX_MISTAKE))

        if mistake == MAX_MISTAKE:
            type_text("Oops! You are out of attempts.")
            type_text("Cucumber will not be added to the recipe.")
print()
#ascii art for cucumber
cucumber = r'''
          _
       .-' `-.
     .'       `.
    /           \
   |   . . . .   |
   |  .       .  |
   | .  . . .  . |
   |.           .|
   | . . . . . . |
   |.           .|
   | . . . . . . |
   |.           .|
   | . . . . . . |
    \           /
     `.       .'
       `-._.-'
'''
print(cucumber)
type_text("Almost there! Just one more ingredient to go!")
print()

mistake=0
MAX_MISTAKE=3

while mistake < MAX_MISTAKE:
    
    type_text("Ingredient 5:")
    print()
    type_text("My outside is dark and bumpy, but my inside is soft and creamy")
    type_text("I have one large seed hiding in my center.")
    type_text("I am a fruit, even though I am not usually sweet.")
    type_text("What am I?")
    print()


    riddleAvocado = input("Enter your guess:").lower()
    print()
    if riddleAvocado == "avocado": 
        type_text("Excellent! You got avocado!")
        hasAvocado = True
        break

    else: 
        mistake = mistake + 1
        type_text("Sorry, incorrect")
        print("Mistakes:" + str(mistake) + "/" + str(MAX_MISTAKE))

        if mistake == MAX_MISTAKE:
            type_text("Uh-oh! You are out of attempts.")
            type_text("Avocado will not be added to the recipe.")
print()
#ascii art for avocado
avocado = r'''
         .-.
       .'   `.
      /  .-.  \
     |  /   \  |
     | |  o  | |
     |  \   /  |
      \  '-'  /
       '.   .'
         `-`
'''
print(avocado)
type_text("Congratulations! You have completed the riddle challenge!")
print()
type_text("You made sushi!")
print()
type_text("Now, let's see how your dish turned out...")
type_text("Dish is now being prepared...")
print()

type_text("The costumer tastes your dish...")
print()

if not hasSalmon:
    score = score - 30
    type_text("Customer: NO SALMON IN SUSHI?! I am disappointed.")

if not hasRice:
    score = score-20
    type_text("Customer: There's no rice! How am I supposed to eat this?")

if not hasSeaweed:
    score= score-10
    type_text("Customer: UGH! No seaweed? This is not sushi!")

if not hasCucumber:
    score= score-20
    type_text("Customer: I was expecting cucumber for a nice crunch!")

if not hasAvocado:
    score= score-20
    type_text("Customer: I was expecting avocado for a creamy texture!")

type_text("Your final score is... " + str(score) + "/100")

if score >= 90:
    type_text("Customer:Perfect! You're a sushi master!")
elif score >= 80:
    type_text("Customer: Not bad! I would order this again!")
elif score>= 60:
    type_text("Customer: Meh. I guess this is okay, but I would not order this again.")
else:
    type_text("Customer: Sorry, but this dish is not good...")

if score >= 70:
    type_text("You have passed the challenge!")
else:
    type_text("You have failed the challenge. Better luck next time!")
#constants:
score=100
riddleSalmon= ""
totalAttempts= 15

#variables
riddleSalmon = "" 
riddleRice= ""
riddleSeaweed= ""
riddleCucumber= ""
riddleAvocado= ""

#variables:
mistake = 0
hasSalmon = False
hasRice = False
hasSeaweed = False
hasCucumber = False
hasAvocado = False

print("Welcome to the kitchen of riddles")
print()
print("You have been chosen to cook for hungry customers using your skills!")
print()
print("Your ingredients are hiddden in different magical words.")
print()
print("Solve riddles to discover what ingredients you need!")
print()
print("Your goal is to get 100 points by collecting all the ingredients. You will lose points for every wrong answer.")
print()
print("Can you make the perfect dish?")
print()

input("Press ENTER to begin!")

#EventOne
print("A strange order has arrived...")

mistake = 0
MAX_MISTAKE=3

while mistake < MAX_MISTAKE: 

    print("Ingredient 1:")
    print("I swim through the ocean, but I'm not a whale. ")
    print("I have scales, but I am not a dragon.")
    print("I can travel upstream when it is time to lay my eggs.")
    print("What am I?")


    riddleSalmon = input("Enter your guess:").lower()
        
    if riddleSalmon == "salmon":
        print("Correct! You got salmon!")
        hasSalmon = True
        break

    else:
        mistake = mistake + 1
        print("Sorry,incorrect")
        print("Mistakes:" + str(mistake) + "/" + str(MAX_MISTAKE))

        if mistake == MAX_MISTAKE:
            print("Oops! You are out of attempts.")
            print("Salmon will not be added to the recipe.")

print("Moving on to the next ingredient...")

mistake=0
MAX_MISTAKE=3

while mistake < MAX_MISTAKE:

    print("Ingredient 2:")
    print("I begin my life in a muddy field, and I grow in rows beside the water.")
    print("I am not wheat, but people grind and cook me before I become soft and fluffy.")
    print("What am I?")

    riddleRice = input("Enter your guess:").lower()

    if riddleRice == "rice": 
        print("Awesome! You got rice.")
        hasRice = True
        break

    else: 
        mistake = mistake + 1
        print("Sorry, incorrect")
        print("Mistakes:" + str(mistake) + "/" + str(MAX_MISTAKE))

        if mistake == MAX_MISTAKE:
            print("Oops! You are out of attempts.")
            print("Rice will not be added to the recipe.")

print("Great! 2 ingredients down, 3 to go!")

mistake=0
MAX_MISTAKE=3

while mistake < MAX_MISTAKE:

    print("Ingredient 3:")
    print("I grow beneath the waves, but I am not an animal.")
    print("I am usually green, brown, or almost black")
    print("You may find me wrapped around around food instead of growing in a garden.")
    print("What am I?")


    riddleSeaweed = input("Enter your guess:").lower()

    if riddleSeaweed == "seaweed": 
        print("WOW!You're a pro! You got seaweed!")
        hasSeaweed = True
        break

    else: 
        mistake = mistake + 1
        print("Sorry, incorrect")
        print("Mistakes:" + str(mistake) + "/" + str(MAX_MISTAKE))

        if mistake == MAX_MISTAKE:
            print("Uh-oh! You are out of attempts.")
            print("Seaweed will not be added to the recipe.")

print("Excellent! 2 more ingredients until you finish your dish!")

mistake=0
MAX_MISTAKE=3

while mistake < MAX_MISTAKE:

    print("Ingredient 4:")
    print("I grow on a vine, but I am not a grape")
    print("I am long, green, and filled with tiny seeds")
    print("I am mosty water, and I make a satisfying crunch when you bite me")
    print("What am I?")


    riddleCucumber = input("Enter your guess:").lower()

    if riddleCucumber == "cucumber": 
        print("Yes! You got cucumber!")
        hasCucumber = True
        break

    else: 
        mistake = mistake + 1
        print("Sorry, incorrect")
        print("Mistakes:" + str(mistake) + "/" + str(MAX_MISTAKE))

        if mistake == MAX_MISTAKE:
            print("Oops! You are out of attempts.")
            print("Cucumber will not be added to the recipe.")

print("Almost there! Just one more ingredient to go!")

mistake=0
MAX_MISTAKE=3

while mistake < MAX_MISTAKE:
    
    print("Ingredient 5:")
    print("My outside is dark and bumpy, but my inside is soft and creamy")
    print("I have one large seed hiding in my center.")
    print("I am a fruit, even though I am not usually sweet.")
    print("What am I?")


    riddleAvocado = input("Enter your guess:").lower()

    if riddleAvocado == "avocado": 
        print("Excellent! You got avocado!")
        hasAvocado = True
        break

    else: 
        mistake = mistake + 1
        print("Sorry, incorrect")
        print("Mistakes:" + str(mistake) + "/" + str(MAX_MISTAKE))

        if mistake == MAX_MISTAKE:
            print("Uh-oh! You are out of attempts.")
            print("Avocado will not be added to the recipe.")

print("Congratulations! You have completed the riddle challenge!")
print("Dish is now being prepared...")
print("The costumer tastes your dish...")

if not hasSalmon:
    score = score - 30
    print("Customer: NO SALMON IN SUSHI?! I am disappointed.")

if not hasRice:
    score = score-20
    print("Customer: There's no rice! How am I supposed to eat this?")

if not hasSeaweed:
    score= score-10
    print("Customer: UGH! No seaweed? This is not sushi!")

if not hasCucumber:
    score= score-20
    print("Customer: I was expecting cucumber for a nice crunch!")

if not hasAvocado:
    score= score-20
    print("Customer: I was expecting avocado for a creamy texture!")

print("Your final score is: " + str(score) + "/100")

if score >= 90:
    print("Customer:Perfect! You're a sushi master!")
elif score >= 80:
    print("Customer: Not bad! I would order this again!")
elif score>= 60:
    print("Customer: Meh. I guess this is okay, but I would not order this again.")
else:
    print("Customer: Sorry, but this dish is not good...")

if score >= 70:
    print("You have passed the challenge!")
else:
    print("You have failed the challenge. Better luck next time!")
