#final
#variables
coins = 0

print("Welcome to the game")
print()
print()
print("This is a role playing game where you will be given a choice to make decisions that will affect the outcome of the story")
print("you have to choose between two options at each decision point.") 
print()
print()
print("you have to earn 100 coins to win this game!")
print()
print()
print("Let's begin!")


print("You are a sailor, you are deciding to go on a trade ship or a pirate ship, which one do you choose?")
print(r"""    __|__ |___| |\
    |o__| |___| | \
    |___| |___| |o \
   _|___| |___| |__o\
  /...\_____|___|____\_/
  \   o * o * * o o  /
~~~~~~~~~~~~~~~~~~~~~~~~~~
 """)
print("if you choose trade ship, you earn 50 coins")
print("if you choose pirate ship, you earn 10 coins")
choiceOne = input("type your choice in complete words: 1. trade ship 2. pirate ship: ")

if choiceOne == "1":
    print("you are on a trade ship")
    coins = coins + 50
    print("coins:" + str(coins)) 
    
    print("you are given the choice to go trade in a close place or a far away place, which one do you choose?")
    print(r"""          |
        \ _ /
      -= (_) =-
        /   \         _\/_
          |           //o\  _\/_
   _____ _ __ __ ____ _ | __/o\\ _
 =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
  =- _=-=- -_=-=_,-"          |
=- =- -=.--"
    
    """)
    print("if you choose to trade in close places, you earn 30 coins")
    print("if you choose to trade in far places , you earn 49 coins")
    choiceTwo = input("type your choice in complete words: 1. close places 2. far away places") 
    
    if choiceTwo == "1":
        print("you have chosen to trade in close places")
        coins = coins + 30
        print("coins:" + str(coins)) 
        print()
        print()
        print("Since you chose the close place, you find a treasure chest!")
        print(r"""
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|   
        
        """)
        print("you earn an additional 20 coins!")
        coins = coins + 20 
        print("coins:" + str(coins)) 
        print()
        print()
        print("YOU WIN!")
    
    elif choiceTwo == "2":
        print ("you have chosen to trade in far away places, you earn 49 coins")
        coins = coins + 49
        print("coins:" + str(coins)) 
        print("Since you chose the far away place, your ship got attacked by pirates!")
        print("""                       |    |    |                 
             )_)  )_)  )_)              
            )___))___))___)\            
           )____)____)_____)\\
         _____|____|____|____\\\__
         \-----------------/
 
       """)
        print("you died, you lost all your coins")
        coins = coins - coins
        print("coins:" + str(coins)) 
        print("YOU LOST!")
        print("restart the game")

elif choiceOne == "2":
    print ("you have chosen the pirate ship, you earn 10 coins")
    coins = coins + 10
    print("coins:" + str(coins))
    
choiceThree = input("You have to choose from two options, you can either 1. attack a trade ship or 2. attack a navy ship, which one do you choose?")
if choiceThree == "attack trade ship":
    print("you have chosen to attack a trade ship, you earn 30 coins.")
    coins = coins + 30
    print("coins:" + str(coins))
    
elif choiceThree == "attack navy ship":
    print("you have chosen to attack a navy ship, but it did not work.")
    print("""               |__
                                |\/
                                 ---
                                 / | [
                            !      | |||
                         _/|     _/|-++'
                        +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____               /\
                ____`-' ||___-{]_| _[}-  |     |_[___\==--          \/   _
 __..._____--==/___]_|__|_____________________________[___\==--___,-----' .7
|                                                                   BB-61/
 \_______________________________________________________________________|
              
    """)
        
        
    print("you got killed by the navy, you lost all your coins")
    coins = coins - coins
    print("coins:" + str(coins))
    print("YOU LOST!")
    print("restart the game")


print("You have survived the attack from the trade ship, but your captain is not happy with your performance")
print("He has given you a choice to either 1. stay on the boat, but you will not get any coins.")
print("Or, you can 2. leave the ship.")
choiceFour = input("Which one do you choose? ")
if choiceFour == "stay on the boat":
    print("Because you guys had attacked a trade ship, the navy has found your ship and you have been captured by the navy") 
    print("Your coins stay the same.")
    coins = coins + 0
    print("coins:" + str(coins))

elif choiceFour == "leave the ship":
    print("you have chosen to leave the ship.")
    print("you swam to the nerest island and you have found a treasure chest")
    (r"""
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|   
        
        """)
    print("inside the treasure chest you have found 60 coins")
    coins = coins + 60
    print("coins:" + str(coins))
    print("YOU WIN!")
    
print("Your captain has slipped away before the navy has found your ship.")
print("He told you where he was going to hide before he left") 
print("you are given two choices from the navy that captured you")
print("you can either 1. tell them where your captain is hiding") 
print("or you can stay 2. silent and not tell them anything")
choiceFive = input("which one do you choose?")
if choiceFive == "tell them":
    print("you have chosen to tell the navy where your captain is hiding")
    print("the navy has captured your captain and you have been rewarded 60 coins")
    coins = coins + 60
    print("coins:" + str(coins))
    print("YOU WIN!")

elif choiceFive == "stay silent":
    print("you have chosen to stay silent and not tell the navy where your captain is hiding")
    print("the navy has put you in jail and you have lost all your coins")
    coins = coins - coins
    print("coins:" + str(coins))
    print("YOU LOST!")
    print("restart the game")
