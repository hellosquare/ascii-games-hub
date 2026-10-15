import time
# connect to github
# -------- CONSTANTS ----------
PLAYER_STARTING_COINS = 200
GHOSTS_DAMAGE = 20
BLUE_DOOR = +50
RED_DOOR = +30
pink_BOX = -25
balck_BOX = -20

# ---------- PLAYER VARIABLE -------
PlayerName = " "
characterType = "detective"

# --------- game variable -------
coins = 200
clue = 3

# -------- game states ------
foundMurderer = False
metCompanion = False

while True:
    print("""
================================
       THE MURDER MYSTERY
================================
          MOMENT OF TRUTH
================================
""")

    print(r"""    .
                               !!!!!!!
                       .       [[[|]]]    .
                     !!!!!!!!|--_--|!!!!!
                       [[[[[[[[\_(X)_/]]]]]
               .-.     /-_--__-/_--_-\-_--\
               |=|    /-_---__/__-__-_\__-_\
           . . |=| ._/-__-__\===========/-__\_
           !!!!!!!!!\========[ /]]|[[\ ]=====/
          /-_--_-_-_[[[[[[[[[||==  == ||]]]]]]
         /-_--_--_--_|=  === ||=/^|^\ ||== =|
        /-_-/^|^\-_--| /^|^\=|| | | | ||^\= |
       /_-_-| | |-_--|=| | | ||=|_|_|=||"|==|
      /-__--|_|_|_-_-| |_|_|=||______=||_| =|
     /_-__--_-__-___-|_=__=_.`---------'._=_|__
    /-----------------------\===========/-----/
   ^^^\^^^^^^^^^^^^^^^^^^^^^^[[|]]|[[|]]=====/
       |.' ..==::'"'::==.. '.[ /~~~~~\ ]]]]]]]
       | .'=[[[|]]|[[|]]]=`._||==  =  || =\ ]
       ||== =|/ _____ \|== = ||=/^|^\=||^\ ||
       || == `||-----||' = ==|| | | |=|| |=||
       ||= == ||:^s^:|| = == ||=| | | || |=||
       || = = ||:___:||= == =|| |_|_| ||_|=||
       _||_ = =||o---.|| = ==_||_= == =||==_||_
      \__/= = ||:   :||= == \__/[][][][][]\__/
      [||]= ==||:___:|| = = [||]\\//\\//\\[||]
      }  {---'"'-----'"'- --}  { //\\//\\//}  {
    __[==]__________________[==]\\//\\//\\[==]_
   |`|~~~~|================|~~~~|~~~~~~~~|~~~~||
jgs|^| ^  |================|^   | ^ ^^ ^ |  ^ ||
  \|//\\/^|/==============\|/^\\\^/^.\^///\\//|///
  \\///\\\//===============\\//\\///\\\\////\\\/////
""")

    PlayerName = input("what is your name?: ")

    print(" welcome detective ", PlayerName, '--')
    print(r"""___
     .:---:.         _
    // #   \\_...--'' \
   || #     |_         |
    \\     // ```--.._/
jgs  ':===:'
       ```
""")

    print("you start with" + str(coins) + "coins")

    print(" welcome to the huanted mansion... you have enterd a mysterious house filled with secret, strage noise, and wandering goshts. Explore the rooms , collect coins and search for clues to uncover the truth. you only have 5 minuets to solve the mystery, good luck!")
    time.sleep(2) 
    print(" IN ORDER TO WIN YOU HAVE TO FIND THE MURDERE AND HAVE AT LEAST 250 COINS AT THE END OF THE GAME")
    time.sleep(1) 
    print("Make sure you remeber these information")
    time.sleep(1) 
    print("there are 3 supspect the witch, a ninja and a vampire")
    time.sleep(1) 
    print("Now these are the clues the companion left you.")
    time.sleep(1)
    print("Clue 1 - The murderer was wearing dark clothing.")
    time.sleep(1)
    print("Clue 2 - The murderer's shoe size was between 38 and 40.")
    time.sleep(1)
    print("Clue 3 - The murderer had black hair.")
    time.sleep(1) 
    print(   )
    
    while True:
        print("Are you ready to make your first decision?")
        print("1. A simple blue door with a round handle. It looks clean and bright.")
        time.sleep(1)
        print("2. A dark red door with a round handle. It looks scary and damaged.")
        time.sleep(1)

        doorchoice = input("Which door do you choose? BLUE or RED: ").upper().strip()

        if doorchoice == "BLUE":
            coins += 50
            print("You found 50 coins!")
            print("Your coins:", coins)
            break

        elif doorchoice == "RED":
            boxchoice = input("You found a box! Open it? YES or NO: ").upper().strip()

            if boxchoice == "YES":
                coins += 20
                print("You found 20 coins!")
                print("Your coins:", coins)
            else:
                print("You decided not to open the box.")
                print("You found a clue in a book!")

            break

        else:
            print("Invalid choice. Please choose BLUE or RED.")
    
    print(" Now time for the second decision")
    time.sleep(1) 
    print("1. A black box")
    time.sleep(1)
    print("2. A pink box")
    print(r"""    _   _
     ((\o/))
.-----//^\\-----.
|    /`| |`\    |
|      | |      |
|      | |      |
|      | |      |
'------===------'
""")
    boxchoice = input("Which box do you want? black or pink: ").strip().lower()
    
    if boxchoice == "black":
        time.sleep(1)
        print("Oh no! You encountered a ghost. You lost 20 coins.")
        coins -= 20
        print("You now have:", coins, "coins")
        time.sleep(1)
        
    elif boxchoice == "pink":
        time.sleep(1)
        print("Yay! You got a clue!")
        print("Make sure you remember all the clues the companion provides.")
        print("Clue 4 - Someone was seen running away from the room, but nobody saw their face.")
        
        print("moving on ")
        print(" woww you encounterd 50 coins. Do you want to take the risk and accept the coins")
        coinchoice = input("YES or NO").upper().strip()
        time.sleep(1) 
        
        if coinchoice == "YES":
            print(" you take the coins and leave the room.")
            coins = coins + 50
            print("You now have: " + str(coins) + "coins")
            time.sleep(1) 
            print(" Sadly you encounterd a ghost down the hall. What do you want to do?")
            time.sleep(1) 
            print("1. loose 75 coins")
            time.sleep(1) 
            print("2 Pay 150 to escape")
            print("You now have: " + str(coins) + "coins")
            escapechoice = input(" what do you choose to do?")
            
            if escapechoice == "1":
                coins = coins - 75
                print("You now have: " + str(coins) + "coins")
                if (coins < 50):
                    print("Game Over!!")
            elif escapechoice == "2":
                coins = coins - 150
                print("You now have: " + str(coins) + "coins")
        
        elif coinchoice == "NO":
            print("You found another clue!")
            time.sleep(1)
            print("Clue 5 - The Witch had a black spot on her clothes.")
            time.sleep(1)
            print("The Vampire had a blood stain on his shirt.")
            time.sleep(1)
            print("Someone else had a ripped T-shirt, but nobody knows who it belongs to.")
            time.sleep(1)
            
            guesschoice = input("Do you want to guess the murderer? YES or NO: ").strip().lower()
            
            if guesschoice == "yes":
                print("Your choices are the ninja, the witch, or the vampire.")
                time.sleep(1)
                guess = input("Who do you think it is? ").strip().lower()
                
                if guess == "ninja":
                    print("YES! You got it right!")
                    time.sleep(1)
                    print(r"""*****************
               ******               ******
           ****                           ****
        ****                                 ***
      ***                                       ***
     **           ***               ***           **
   **           *******           *******          ***
  **            *******           *******            **
 **             *******           *******             **
 **               ***               ***               **
**                                                     **
**       *                                     *       **
**      **                                     **      **
 **   ****                                     ****   **
 **      **                                   **      **
  **       ***                             ***       **
   ***       ****                       ****       ***
     **         ******             ******         **
      ***            ***************            ***
        ****                                 ****
          ****                           ****
              ******               ******
                   *****************
""")
                elif guess == "witch" or guess == "vampire":
                    print("OH NO! That's wrong!")
                    print(r"""
    .-""""""-.
   .'          '.
  /   O      O   \
 :           `    :
 |                |   sad
 :    .------.    :
  \  '        '  /
   '.          .'
 jgs  '-......-'
 """)
                    print("GAME OVER!!")
                    break

                else:
                    print("That is not one of the suspects.")

            elif guesschoice == "no":
                print("You chose not to guess.")
                time.sleep(1)

            else:
                print("Please enter YES or NO.")
                print("OMGG you found 2 shiney boxes. One is golden and the other is silver. You can only choose one box.")
                time.sleep(1) 
                print("1. Golden box")
                time.sleep(1) 
                print("2. Silver box")
                print(r"""    _   _
     ((\o/))
.-----//^\\-----.
|    /`| |`\    |
|      | |      |
|      | |      |
|      | |      |
'------===------'
""")

                boxchoice = input("Which box do you choose? ")

                if boxchoice == "1":
                    coins = coins + 500
                    print("You chose the golden box!")
                    print("You got 500 coins!")
                    print("You now have", coins, "coins.")

                elif boxchoice == "2":
                    coins = coins - 15
                    print("You chose the silver box.")
                    print("You lost 15 coins.")
                    print("You now have", coins, "coins.")

                    if coins < 50:
                        print("GAME OVER!!")

                else:
                    print("That's wrong. Try again!")

print("This is your last clue before you guess the murderer...")
time.sleep(2)
print("Final Clue - The Ninja had a ripped shirt.")
time.sleep(2)

print("You have followed the clues this far...")
time.sleep(2) 
print("Now, there is only one thing left to do.")
time.sleep(1) 
print("It is the moment of truth.")
time.sleep(1) 
print("Who is the murderer?")
time.sleep(1) 
print("1. Ninja")
time.sleep(1) 
print("2. Witch")
time.sleep(1) 
print("3. Vampire")

murderchoice = input("Who do you think the murderer is? ")
if murderchoice == "1":
    print("You chose the Ninja.")
    time.sleep(1) 
    print(r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢀⣶⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⢀⡴⡂⢠⣾⡇⠀⣠⣴⣿⠁⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣻⣤⣟⣿⣷⣿⣿⣷⣾⣿⢿⣧⣤⣶⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣷⢿⣷⣯⣿⣷⠿⡝⢗⣷⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⣟⡎⣻⢚⣷⣝⣿⣿⡯⣏⣿⣿⣟⣿⢟⣟⣳⡖⡲⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⢆⡿⢛⠻⣿⢋⡾⢯⣏⢒⡳⠻⣷⣙⣻⣦⡯⡠⠼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣵⣈⣟⠻⠞⢷⣡⢛⣓⣜⢻⣿⢥⣷⡷⡟⣝⣿⣦⣾⡞⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⢿⡳⡮⣧⣯⠻⣾⣽⢿⣞⣳⢷⣶⣶⣯⢳⣷⢿⣳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⣧⣾⠿⣗⢰⠽⣽⣲⣭⣻⡿⣯⢿⣷⣝⣏⣿⣧⣞⠉⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢠⣷⡿⡿⣼⡎⣽⣷⢗⣏⣿⣿⡽⢿⣿⣟⠧⣭⡿⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⣱⣭⡅⣽⢢⣬⢝⣛⡟⣾⣧⣳⠲⣿⠾⢊⡪⣤⢛⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠺⠣⢮⠯⠴⢺⠿⠓⡟⠸⡘⠛⢓⡷⣢⢺⢺⠕⠀⠐⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢏⠼⢤⣶⢳⢕⣷⡾⣖⣸⣛⣳⣎⣻⣦⣬⣇⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠷⠟⠙⠛⠈⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠓⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠖⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠲⠶⢤⣤⣄⣀⣀⣀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⣀⢀⠤⡤⠔⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠜⠓⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠟⣉⠭⠤⠤⠤⠤⠍⣉⠛⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⡈⠀⠀⠀⠀⠀⠀⡀⡾⠀⠀⠀⣰⠟⣶⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢄⠀⠀⠀⠀⠀⠀⠀⠀⠄⣢⠋⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⡴⠃⣴⡿⢋⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⠀⢻⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠲⢶⠀⡖⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⢀⡾⢁⣼⡿⣡⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡃⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣠⠟⢠⣾⠟⣰⡿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠋⣠⣿⢏⣼⡟⠀⢻⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⣴⡿⢣⣾⠏⠀⠀⠈⢧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⢁⣼⡟⣡⣿⠃⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀
⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⢠⣾⠟⣴⡿⠁⠀⠀⠀⠀⣀⣀⣽⡀⠀⠀⠀
⠀⠀⠠⣯⣀⣀⣀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⣠⣿⢋⣼⣿⣥⡴⠶⠒⠉⢿⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠙⠿⣿⣿⠛⠓⠒⠦⣤⣀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣶⣶⣶⣶⣶⣤⣤⡼⠁⣰⡿⢣⣾⣿⡟⠁⠀⠀⠀⠀⠘⣏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢈⡟⠀⠀⠀⠀⠈⢻⣿⡇⠀⢀⣀⣤⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢀⣼⡟⣱⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⣀⣼⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⣴⠏⣴⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⢀⣾⢋⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀
⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⣠⡿⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀
⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⣴⡟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀
⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣠⣾⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀
⠀⠀⠀⡎⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡿⠟⠛⡿⠋⠉⡿⠋⠉⠀⡼⠉⠀⠀⠋⠁⠀⠰⠋⠀⠀⡿⠁⠀⢸⠁⠈⢹⠋⠉⢻⠟⠛⣿⣇⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀
⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⢸⣿⠏⠀⠞⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠘⠀⠀⡿⢹⡀⠀⠀⠀⠀⠀⢸⡆⠀⠀
⠀⠀⢸⠀⠀⠀⠀⠀⠀⢀⡟⢻⢀⣀⣀⣀⣀⣤⣤⣤⣴⣤⣤⣤⣤⣤⣤⣶⠶⣦⣶⣶⣶⣶⣦⣤⣤⣤⣤⠤⣶⣶⡶⢤⣤⣤⣶⣾⡃⠀⢧⠀⠀⠀⠀⠀⠈⡇⠀⠀
⠀⠀⡿⠀⠀⠀⠀⠀⠀⣸⣱⠟⢻⠟⠛⠙⠟⠉⠉⠛⠁⠀⠘⠋⠀⢀⡾⠃⢀⣾⣿⣿⠟⠉⠃⠀⠀⠸⠀⠀⠀⠑⠀⠀⠀⠇⠀⠈⣿⠀⠸⡆⠀⠀⠀⠀⠀⣿⠀⠀
⠀⢰⡇⠀⠀⠀⠀⠀⢀⠏⣟⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣠⠟⠀⣠⣿⣿⣿⣏⣀⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⢀⠟⠀⠀⢻⣀⣤⣴⣶⣿⣿⣿⡄
⠀⣸⣅⣀⣀⣀⣀⣀⣼⠀⠛⢶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⣼⠟⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢀⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⢀⣾⢫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠸⠿⠿⠿⠿⠿⠿⠿⠿⠀⠼⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠀⠠⠿⠱⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠆⠀⠻⠿⠿⠿⠿⠿⠿⠿⠇
    """)
    print("Everyone goes silent.")
    time.sleep(1) 
    print("The truth is finally revealed...")
    time.sleep(1) 
    print("THE NINJA WAS THE MURDERER!")
    time.sleep(1) 
    print(" GOOD JOB! You solved the mystery!")
    time.sleep(1) 
    print(r"""       *****************
               ******               ******
           ****                           ****
        ****                                 ***
      ***                                       ***
     **           ***               ***           **
   **           *******           *******          ***
  **            *******           *******            **
 **             *******           *******             **
 **               ***               ***               **
**                                                     **
**       *                                     *       **
**      **                                     **      **
 **   ****                                     ****   **
 **      **                                   **      **
  **       ***                             ***       **
   ***       ****                       ****       ***
     **         ******             ******         **
      ***            ***************            ***
        ****                                 ****
          ****                           ****
              ******               ******
                   *****************
""")

elif murderchoice == "2":
    print("You chose the Witch.")
    time.sleep(1) 
    print(r"""                     .,:::::::,. 
                  ,::;;;;;;;;;;::, 
                ,::;;;;;;;;;;;;;;:: 
               ::;;;;;;;;;;;;;;;;:::. 
              ::;;;;;;;;;;;;;;:::::,;;. 
            ,::;;;;;;;;;;;;;::::,;;;;;;::, 
           ::;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;::, 
         ,::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;::, 
        ,::;;;;;;;;;;;;;;;;;;;;;::,vvvvvvvvv,;;;::, 
     ,:,;;;;;;;;;;;;;;;;;;;;::,vvnnnnnnnnnnnnvv,;;::. 
   ,::,;;;;;;;;;;;;;;;;;::,vv;;;;vvnnv,vnnnvv;;;vv,:: 
 ,:::,;;;;;;;;;;;;;;;;::,vvvv''';;;vvnv,vv,v;;vvvvv,' 
;::::,;;;;;;;;;;;;;;::##'vvv,a@@@@a;;vv,v,v;a@@@avv, 
;::::,;;;;;;;;;;;;::'###'vv,a@@@@@@@,vvnnv,@@@@@@;v; 
;::::;;;;;;;;;;;;::'###'vvvv,@@@' `@,vvnnvv' `@@,;' 
;;;;;;;;;;;;;;;::'####'vvn;;vvvvvv;;nnnnnnnnmv;;vv, 
;;;;;;;;;;;;;::'######'vvnnnn;;;;nnvmnnnnnnnnnm,%vv, 
;;;;;;;;;;;::',######'vvnnnnnnnnnv;mnnnnnnnnnnnnm,v' 
;;;;;;;;;;'::,####%##'vvnnnnnnnn;nv;mnnnnnnnnnnnn, 
;;;;;;;;'::::,###%###'vvnnnnnn;nnnnvvv;mnnnnnnnnm 
;;;;;;;':::::,###%###'vvnnnn;v nnnnnnvvv;mmmmmmm' 
;;;;;;;':::::,##%####'vvnn;vvnn `nnnnnnnvvvvvv 
;;;;;;;;;;;:::,######'vvn;vvnnnn.,,,,.   'vv'# 
;;;;,:::;;;;;;,#####'v;vvn;vnnnn;;;;;;; ,v'### 
;;;;;,::::;;;;,#####'v%%;vvnnnnnnnnnnnnvv,##%# 
;;;;;;,::::;;;,#####'vvv%%%%%;vvvnnnnnnnvv;### 
;;;;;;;,::::;;,#####'vvvvvv%%%;vvvvvvvvvv'###% 
;;;;;;;,::::;;,##%###'vvvvvvvv%%%%%%%';;;####% 
;;;;;;;,::::;;;##%###'vvvvvvvvvvvv';;;;,;###%#              .,,,;' 
;;;;;;;;,::::;;##%###'vvvvvvvv;;;;;,::;,:#####           //;;;;;' 
;;;;;;;;,::::;;###%##'vvvvv';;;;,:::;;,::#####          //'''' 
;;;;;;;;,::::;;#######;;;;;;,::::;;;::,:,#####    ,sSSSSssSSSSs, 
;;;;;;;;;,::::;###;###;;,:::::;;;;;;;,::,####'   SSSSSSSSSSSSS@SS.v, 
;;;;;;;;;;,::::##;;###;;;;;;;;;;;;;,::::,####   v;SSSSSSSSSSSS@@S;vv 
;;;;;;;;;;;,:::##::###;;;;;;;;:,::::::::,####  vv;SSSSSSSSSSSS@@S;vv 
;;;;;;;;;;;;;,::#:;###;;;;;;;;;;;;;;;:::,####  vv;SSSSSSSSSSSS@S;vnv 
;;;;;;;;;;;;;;;,::::##::::::::::;;;;;:::,####  vnv;SSSSSSSSSSS;vnvv' 
;;;;;;;;;;;;;;;;;,:::##;;;;;;;;;;;;;::::,###'  `vnv;SSSSSSS;vnnnvv' 
;;;;;;;;;;;;;;;;::::,::#;;;;;;;;::::::::,###   ,vvnnnnnnnnnnvvv' 
;;;;;;;;;;;;;;;;;;;;;;;;;;::::::::::::::,#',vvnnnnnnnnnnvvvv' 
;;;;;;;;;;;;;;;;;;;;:::::::::::::,;;;;;,vvvnnnnnnnnnvvv' 
;;;;;;;;;;;;;;;:::::::::::,;;;;;;;;;;;,vvnnnnnnnnnvv' 
;;;;;;;;:::::::::::::,;;;;;;;;;;;;;;;,vvnnnnnnnnvv' 
;;::::::::::::,;;;;;;;;;;;;;;;;;;;;;,vvnnnnnnnvv' 
;;::::::,;;;;;;;;;;;;;;;;;;;;;;;;;,vvnnnnnnnvv' 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,vvnnnnnnvv' 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,vvnnnnnvv' 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,vvnnnnvv' 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,vvnvv::: 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,vvv:::::: 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;,:::::::::' 
;;;;;;;;;;;;;;;;;;;;;;;;;;;,:::::::::: 
;;;;;;;;;;;;;;;;;;;;;;;;;;,::::::::::' 
;;;;;;;;;;;;;;;;;;;;;;;;;;,:::::::::' 
;;;;;;;;;;;;;;;;;;;;;;;;;;,::::::::' 
;;;;;;;;;;;;;;;;;;;;;;;;;;;,::::::'
    """)
    print("Everyone looks at you in silence.")
    time.sleep(1) 
    print("But you made the wrong choice.")
    time.sleep(1) 
    print("The Witch was innocent.")
    time.sleep(1) 
    print("The real murderer escapes...")
    time.sleep(1) 
    print("GAME OVER!!")

elif murderchoice == "3":
    print("You chose the Vampire.")
    time.sleep(1) 
    print(r"""              __.......__
            .-:::::::::::::-.
          .:::''':::::::''':::.
        .:::'     `:::'     `:::. 
   .'\  ::'   ^^^  `:'  ^^^   '::  /`.
  :   \ ::   _.__       __._   :: /   ;
 :     \`: .' ___\     /___ `. :'/     ; 
:       /\   (_|_)\   /(_|_)   /\       ;
:      / .\   __.' ) ( `.__   /. \      ;
:      \ (        {   }        ) /      ; 
 :      `-(     .  ^"^  .     )-'      ;
  `.       \  .'<`-._.-'>'.  /       .'
    `.      \    \;`.';/    /      .'
 jgs  `._    `-._       _.-'    _.'
       .'`-.__ .'`-._.-'`. __.-'`.
     .'       `.         .'       `.
   .'           `-.   .-'           `.
""")
    print("The room suddenly goes silent.")
    time.sleep(1) 
    print("NOO  you made the wrong choice.")
    time.sleep(1) 
    print("The Vampire was innocent.")
    time.sleep(1) 
    print("The real murderer escapes...")
    time.sleep(1) 
    import sys
    print("GAME OVER!!")
    sys.exit() 
    print(r"""
    .-""""""-.
   .'          '.
  /   O      O   \
 :           `    :
 |                |   sad
 :    .------.    :
  \  '        '  /
   '.          .'
jgs  '-......-'
""")

else:
    print("That's wrong. Try again!")
