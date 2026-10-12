#final
#IMPORTS------------------
import sys

#CONSTANTS----------------

#VARIABLES----------------
playerChoice = ""
sub_choice_1 = ""
sub_choice_2 = ""
sub_choice_3 = ""
sub_choice_4 = ""
sub_choice_5 = ""
sub_choice_6 = ""
sub_choice_7 = ""
sub_choice_8 = ""

#ART------------
manArt = r'''
                 O_  _O
                 |a` `a|
                 |  u  |
                 \  =  /
                 |\___/|
        ___ ____/:     :\____ ___
      .'   `.-===-\   /-===-.`   '.
     /      .-"""""-.-"""""-.      \
    /'             =:=             '\
  .'  ' .:    o   -=:=-   o    :. '  `.
  (.'   /'. '-.....-'-.....-' .'\   '.)
  /' ._/   ".     --:--     ."   \_. '\
 |  .'|      ".  ---:---  ."      |'.  |
 |  : |       |  ---:---  |       | :  |
  \ : |       |_____._____|       | : /
  /   (       |----|------|       )   \
 /... .|      |    |      |      |. ...\
|::::/'' jgs /     |       \     ''\::::|
'""""       /'    .L_      `\       """"'
           /'-.,__/` `\__..-'\
          ;      /     \      ;
          :     /       \     |
          |    /         \.   |
          |`../           |  ,/
          ( _ )           |  _)
          |   |           |   |
          |___|           \___|
          :===|            |==|
           \  /            |__|
           /\/\           /"""`8.__
           |oo|           \__.//___/
           |==|
           \__/
'''
sharkart = r"""
           __)\_  
     (\_.-'    a`-.
jgs  (/~~````(/~^^`
"""
bearart = r"""
                                          A
             ___                         / \
          .="   "=._.---.               /   \              ____________
        ."         c ' Y'`p            /     \            /)  -
       /     \     `\  w_/            :~~~~~~~:          / )-   .   -
 jgs   |      )  /     /              |       |         <  )      -- 
 ______|     /__-\ \_=.\              |       |          \ )  -      -
(XXXXX/'`------)))`=-'"`'"___________/__/__\___\___ _ _ _ \)___________
"""
tigerart = r"""
                        __,,,,_
       _ __..-;''`--/'/ /.',-`-.
   (`/' ` |  \ \ \\ / / / / .-'/`,_
  /'`\ \   |  \ | \| // // / -.,/_,'-,
 /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')
/  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\'
`-`  f/ ;      / __/ \__ `/ |__/ |
     `-'      |  -| =|\_  \  |-' |
           __/   /_..-' `  ),'  //
       fL ((__.-'((___..-'' \__.'
"""                                 
barkart = r"""
      ////\\\\
      |      |
     @  O  O  @
      |  ~   |         \__
       \ -- /          |\ |
     ___|  |___        | \|
    /          \      /|__|
   /            \    / /
  /  /| .  . |\  \  / /
 /  / |      | \  \/ /
<  <  |      |  \   /
 \  \ |  .   |   \_/
  \  \|______|
    \_|______|
      |      |
      |  |   |
      |  |   |
      |__|___|
      |  |  |
      (  (  |
      |  |  |
      |  |  |
     _|  |  |
 cccC_Cccc___)
"""
treeart = r"""
         v
        >X<
         A
        d$b
      .d\$$b.
    .d$i$$\$$b.
       d$$@b
      d\$$$ib
    .d$$$\$$$b
  .d$$@$$$$\$$ib.
      d$$i$$b
     d\$$$$@$b
  .d$@$$\$$$$$@b.
.d$$$$i$$$\$$$$$$b.
        ###
        ###
        ### mh
"""
metalart = r"""
       __/\__ 
      \    /   
__/\__/    \__/\__
\                /
/_              _\
  \            /
__/            \__ 
\                /
/_  __      __  _\
  \/  \    /  \/
      /_  _\
        \/
"""

while True:
    PlayerHP = 100
    print("\n" + "=" * 50)
    print("Start your game") #make this a bit more exciting, also, add an option where you ask for the players name
    print(f"Current HP: {PlayerHP}")
    print("You have come to an island. To win, you need to make the right choices.")
    print("Wrong choices will cost health points. If HP reaches 0, you lose.")
    
    # First choice: Ocean or Forest
    playerChoice = input("Where do you want to go? 1. Ocean 2. Forest: ").strip() #make sure you are specific that the player has to type the number and not the word

    if playerChoice == "1":
        print("\n>>> You have chosen to go to the ocean.")
        print("You see a shark! You can choose to fight or run.")
        print()
        print(sharkart)
        
        sub_choice_1 = input("1. Fight 2. Run: ").strip()
        
        if sub_choice_1 == "1":
            print("You chose to fight the shark.")
            PlayerHP -= 100
            print(f"You lost 100 HP. Current HP: {PlayerHP}")
            if PlayerHP <= 0:
                print("Game Over! The shark ate you.")
                print()
                print(sharkart)
                continue  # Restart the game loop instead of breaking
            else:
                print("Miraculously, you survived but are heavily injured.")
                print("You crawl back to shore...")
                # Since logic was incomplete here, we restart the loop or end. 
                # Let's assume you survive but the game resets for simplicity in this linear structure
                print("You decide to try again from the start.")
                continue

        elif sub_choice_1 == "2":
            print("You chose to run away from the shark.")
            print("You are safe for now.")
            print(manArt)
            sub_choice_2 = input("Next, where to go? 1. Cave 2. Forest: ").strip()
            
            if sub_choice_2 == "1":
                print("\n>>> You entered the cave.")
                print("You see a bear! Choose wisely.")
                print()
                print(bearart)                
                sub_choice_3 = input("1. Fight 2. Run: ").strip()
                
                if sub_choice_3 == "1":
                    print("You fought the bear.")
                    PlayerHP -= 100
                    print(f"You lost 100 HP. Current HP: {PlayerHP}")
                    if PlayerHP <= 0:
                        print("Game Over! The bear defeated you.")
                        print(bearart)
                        continue  # Restart the game loop instead of breaking
                    else:
                        print("You barely survived the bear encounter.")
                        print("You found a secret exit and escaped the island! YOU WIN!")
                        break
                        
                elif sub_choice_3 == "2":
                    print("You ran away from the bear.")
                    print("You made the right choice! You found a hidden treasure chest.")
                    print("YOU WIN!")
                    print()
                    print(bearart)
                    break
                else:
                    print("Invalid choice. You got lost in the cave. Game Over.") #instead of a break can we continue in a loop so that we can restart the game again - you can do the same loop that you had before
                    continue

            elif sub_choice_2 == "2":
                print("\n>>> You went to the forest.")
                print()
                print(treeart)
                sub_choice_4 = input("Collect resources: 1. Wood 2. Metal: ").strip()
                
                if sub_choice_4 == "1":
                    print("You collected wood and built a sturdy shelter.")
                    print("You survived the night. YOU WIN!")
                    break
                elif sub_choice_4 == "2":
                    print("You tried to collect metal but triggered a trap.")
                    PlayerHP -= 100
                    print(f"You lost 100 HP. Current HP: {PlayerHP}")
                    if PlayerHP <= 0:
                        print("Game Over! The trap killed you.")
                        print()
                        print(metalart)
                        continue
                    else:
                        print("You survived the trap but are weak.")
                        print("You decide to rest and survive. YOU WIN!")
                        break
                else:
                    print("Invalid choice. You starved in the forest. Game Over.")
                    continue
            else:
                print("Invalid choice. You fell off a cliff. Game Over.")
                continue

    elif playerChoice == "2":
        print("\n>>> You have chosen to go to the forest.")
        print("You see a bear! What will you do?")
        print()
        print(bearart)
        
        sub_choice_5 = input("1. Fight 2. Run: ").strip()
        
        if sub_choice_5 == "1":
            print("You chose to fight the bear.")
            PlayerHP -= 100
            print(f"You lost 100 HP. Current HP: {PlayerHP}")
            if PlayerHP <= 0:
                print("Game Over! The bear was too strong.")
                print()
                print(bearart)
                continue
            else:
                print("You defeated the bear! But you are exhausted.")
                print("You rest and recover. YOU WIN!")
                print(bearart)
                continue #this is too short - i would suggest changing this to continue to make this loop back to the beginning so the player can make more choices
                
        elif sub_choice_5 == "2":
            print("You ran away from the bear.")
            print("You made the right choice.")
            print(bearart)

            sub_choice_6 = input("Next destination: 1. 67Park 2. Mr.Barks office: ").strip()
            
            if sub_choice_6 == "1":
                print("\n>>> You arrived at 67Park.")
                print("Oh no! A Tiger appears!")
                print()
                print(tigerart)
            
                
                sub_choice_7 = input("1. Fight 2. Run: ").strip()
                
                if sub_choice_7 == "1":
                    print("You fought the Tiger.")
                    PlayerHP -= 100
                    print(f"You lost 100 HP. Current HP: {PlayerHP}")
                    if PlayerHP <= 0:
                        print("Game Over! The Tiger won.")
                        print()
                        print(tigerart)
                        continue
                    else:
                        print("You survived the tiger attack! Incredible!")
                        print("YOU WIN!")
                        print()
                        print(tigerart)
                        break
                        
                elif sub_choice_7 == "2":
                    print("You ran away from the Tiger.")
                    print("The Tiger seems friendly now. 'Meet YOUR NEW FRIEND, Tiger'")
                    print()
                    print(tigerart)
                    
                    sub_choice_8 = input("Tiger says: I love you. Be my friend? 1. Yes 2. No: ").strip()
                    
                    if sub_choice_8 == "1":
                        print("You became friends with the Tiger.")
                        print("The Tiger helps you escape the island. YOU WIN!")
                        print()
                        print(tigerart)
                        break
                    elif sub_choice_8 == "2":
                        print("You rejected the Tiger.")
                        print("The Tiger got angry and chased you away. Game Over.")
                        print()
                        print(tigerart)
                        continue
                    else:
                        print("Invalid choice. The Tiger left you. Game Over.")
                        print()
                        print(tigerart)
                        continue

            elif sub_choice_6 == "2":
                print("\n>>> You went to Mr.Barks office.")
                print("Mr. Bark gives you a map and a boat key.")
                print("You sail away safely. YOU WIN!")
                print()
                print(barkart)
                break
            else:
                print("Invalid choice. You got lost. Game Over.")
                continue
        else:
            print("Invalid choice. The bear caught you. Game Over.")
            print()
            print(bearart)
            continue
    else:
        print("Invalid choice. You can't find the way out. Game Over.")
        continue

    # Ask to replay
    replay = input("\nDo you want to play again? (y/n): ").lower()
    if replay != 'y':
        print("Thanks for playing!")
        break
