#final
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
gameover = False
finalguessdeny = False

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
print()
print()
print()
print("welcome to the huanted mansion...") 
print("you have enterd a mysterious house filled with secret, strage noise, and wandering goshts.")
print("Explore the rooms , collect coins and search for clues to uncover the truth.")
print("you only have 5 minuets to solve the mystery, good luck!")
print()
print()
print()
print(" IN ORDER TO WIN YOU HAVE TO FIND THE MURDERER AND HAVE AT LEAST 250 COINS AT THE END OF THE GAME")
print()
print()
print()
print("Make sure you remember these information")
print()
print()
print()
print("there are 3 supspect the witch, a ninja and a vampire")
print(" Now these are the clues the companion left you.")
print()
print("Clue 1-the murdere was wearing a all black outfit.")
print("Clue 2 - the murdere shoe size is 39.")
print("Clue 3 - the murder has black hair")
    
while True:
    print("Are you ready to make your first decision?")
    print()
    print("1. A simple blue door with a round handle. It looks clean and bright")
    print()
    print("or 2'. A dark red door with a round handle also but it looks scary and damaged ")
    doorchoice = input(" which door do you choose: type red or blue?:").strip().lower()

    if doorchoice == "blue":
        print("you slowly open the blue door. A bright light shines from inside.")
        print()
        print("you walk into a samll quite room.there is a table in the middle with a box on it")
        print()
        print("you open the box and see lots of gold coins. you count them carefully.")
        print()
        print(" THERE ARE 50 coins! you take the coins and leave the room happily")
        coins = coins + 50
        break

    elif doorchoice == "red":

        print("you slowly open the red door. It creaks loudly...")
        print()
        print(" you enter a dark and spooky room")
        print("oh theres a box under a table.")
        print()
        openingboxchoice = input(" Do you open the box type YES or NO").upper().strip()

        if openingboxchoice == "YES":
            print(" you open the box and find 20 coins!")
            coins = coins + 20
            print(" you take the 20 coins and leave the room.")
            print("You now have: " + str(coins) + "coins")
            break

        elif openingboxchoice == "NO":
            print(" you leave the box and leave the room")
            print(" SUPRISINGLY you found a book that has clues inside. You read the book and find out that the murdere has sharp pointy teeth,The witch and the ninja both wearing a black outfit and has black hair but except of the vampire. You have to choose the right suspect based on the clues you have")
            break

    else:
        print("Please type red or blue")

while True:        
    print(" Now time for the second decision")
    
    print("1. A black box")
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
    boxchoice = input(" which box do you want? type black or pink:").lower().strip()
    
    if boxchoice == "black":
        print("Oh no you encounterd a gosht. You lost 20 coins")
        coins = coins - 20
        print()
        print("You now have: " + str(coins) + "coins")
        break
    
    elif boxchoice == "pink":
        print("yayy you got a clue")
        print()
        print(" But make sure all the clues the compianion provide you won't forget")
        print()
        print("the clue is that the murderer carrys lots of weapons.")
        print()
        print(r"""/()
                / /
               / /
  /============| |------------------------------------------,
{=| / / / / / /|()}     }     }     }                        >
  \============| |------------------------------------------'
               \ \
                \ \
                 \ \
""")
        break

print("moving on...")
print()
print()

while True:
    print("woww you encounterd 50 coins. Do you want to take the risk and accept the coins")
    coinchoice = input(" YES or NO").strip().upper()
    if coinchoice == "YES":
        print(" you take the coins and leave the room.")
        print()
        coins = coins + 50
        print("You now have: " + str(coins) + "coins")
        print()
        
        print(" Sadly you encounterd a ghost down the hall.")
        print()
        print("What do you want to do?")
        print()
        print("1. loose 75 coins")
        print("2 Pay 150 to escape")
        print()
        print("You now have: " + str(coins) + "coins")
        
        escapechoice = input(" what do you choose to do? type 1 or 2").strip()
        
        if escapechoice == "1":
            coins = coins - 25
            print("You now have: " + str(coins) + "coins")
            
            if (coins < 50):
                print("Game Over!! please press restart to play again")
                gameover = True
                break

        elif escapechoice == "2":
            coins = coins - 150
            print("You now have: " + str(coins) + "coins")
            break
    
    elif coinchoice == "NO":
        print(" you get a clue.")
        print()
        print("THE NINJA SHOE SIZE IS 39 , THE WITCH SHOE SIZE IS 38 AND THE VAMPAIRE SHOE SIZE IS 40")
        break
    
    else:
        print("That's wrong. Try again!")

while True:
    guesschoice = input("Do you want to guess now? type yes or no: ").strip().lower()
    
    if guesschoice == "yes":
        print("Your choices are the ninja, the witch, or the vampire.")
        print()
        guess = input("Who do you think it is? type ninja or witch or vampire").strip().lower()
        
        if guess == "ninja":
            print("YES! You got it right!")
            break
        
        elif guess == "witch":
            print("OH NO! That's wrong!")
            print()
            print("GAME OVER!!")
            gameover = True
            break
            
        elif guess == "vampire":
            print("OH NO! That's wrong!")
            print()
            print("GAME OVER!!")
            gameover = True
            break
    
    elif guesschoice == "no":
        print("You chose not to guess.")
        finalguessdeny = True
        break
    
    else:
        print("That's wrong. Try again!")

while finalguessdeny == True:
    print("OMGG you found 2 shiney boxes. One is golden and the other is silver. You can only choose one box.")
    print()
    print()
    print("1. Golden box")
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
    boxchoice = input("Which box do you choose? type 1 or 2 ").strip()
    
    if boxchoice == "1":
        coins = coins + 500
        print("You chose the golden box!")
        print("You got 500 coins!")
        print("You now have" + str(coins) + " coins.")
        break
        
    elif boxchoice == "2":
        coins = coins - 15
        print("You chose the silver box.")
        print("You lost 15 coins.")
        print("You now have" + str(coins) + " coins.")
        
        if coins < 50:
            print("GAME OVER!!")
            gameover = True
            break
    
    else:
        print("That's wrong. Try again!")

while finalguessdeny == True and gameover == False:
    print("You have followed the clues this far...")
    print("Now, there is only one thing left to do.")
    print("It is the moment of truth.")
    print()
    print("Who is the murderer?")
    print()
    print("1. Ninja")
    print("2. Witch")
    print("3. Vampire")
    murderchoice = input("Who do you think the murderer is? type 1, 2, or 3").strip()
    
    if murderchoice == "1":
        print("You chose the Ninja.")
        print()
        print("Everyone goes silent.")
        print()
        print("The truth is finally revealed...")
        print()
        print("THE NINJA WAS THE MURDERER!")
        print()
        print(" GOOD JOB! You solved the mystery!")
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
        break

    elif murderchoice == "2":
        print("You chose the Witch.")
        print()
        print("Everyone looks at you in silence.")
        print()
        print("But you made the wrong choice.")
        print()
        print("The Witch was innocent.")
        print()
        print("The real murderer escapes...")
        print()
        print("GAME OVER!!")
        gameover = True
        break

    elif murderchoice == "3":
        print("You chose the Vampire.")
        print()
        print("The room suddenly goes silent.")
        print()
        print("NOO  you made the wrong choice.")
        print()
        print("The Vampire was innocent.")
        print()
        print("The real murderer escapes...")
        print("GAME OVER!!")
        gameover = True
        print(r'''
    .-""""""-.
   .'          '.
  /   O      O   \
 :           `    :
 |                |   sad
 :    .------.    :
  \  '        '  /
   '.          .'
jgs  '-......-'

''')
        break

    else:
        print("That's wrong. Try again!")

while gameover == True:
    print("Game Over! Please restart the game")
    break
