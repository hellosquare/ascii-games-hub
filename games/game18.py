# -------- CONSTANTS----------
from ast import While


PLAYER_STARTING_COINS=200
GHOSTS_DAMAGE=20
BLUE_DOOR= 50
RED_DOOR= 30
pink_BOX= 25
black_BOX= 20

#----------PLAYER VARIABLE-------
PlayerName= " "
characterType = "detective"


#---------game variable-------
coins= 200
clue= 3

#--------game states------
foundMurderer = False
metCompanion = False 


print("================================")
print("       THE MURDER MYSTERY")
print("================================")
print("          MOMENT OF TRUTH")
print("================================")
print(r'''
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
    }  {---'"'-----'"'- --}  {//\\//\\//}  {
__[==]__________________[==]\\//\\//\\[==]_
|`|~~~~|================|~~~~|~~~~~~~~|~~~~||
jgs|^| ^  |================|^   | ^ ^^ ^ |  ^ ||
\|//\\/^|/==============\|/^\\\^/^.\^///\\//|///
\\///\\\//===============\\//\\///\\\\////\\\///// 
''')
PlayerName = input("what is your name?: ")

print (" welcome detective ", PlayerName, '--') 

print(r"""
    :---:.         _
// #   \\_...--'' \
|| #     |_         |
\\     // ```--.._/
    ':===:'
    ```""")

print(                       )
print(                       )
print("you start with" + str(coins) +"coins")

print(" welcome to the huanted mansion... you have enterd a mysterious house filled with secret, strage noise, and wandering goshts. Explore the rooms , collect coins and search for clues to uncover the truth. you only have 5 minuets to solve the mystery, good luck!")

print(" IN ORDER TO WIN YOU HAVE TO FIND THE MURDERE AND HAVE AT LEAST 250 COINS AT THE END OF THE GAME")

print("Make sure you remeber these information")

print("there are 3 supspects:") 
print("the witch")
print("a ninja") 
print("and a vampire")

print(" Now these are the clues the companion left you:") 
print("Clue 1-the murdere was wearing a all black outfit.") 
print("Clue 2-the murdere shoe size is 39.") 
print("Clue 3-the murder has black hair")
    

print("Are you ready to make your first desciosn?")
print("1. A simple blue door with a round handle. It looks clean and bright")
print("or 2'. A dark red door with a round handle also but it looks scary and damaged ")
print(                       )
print(                       )

while True:
    
    doorchoice = input(" which door do you choose red or blue?: ").strip().lower()

    if doorchoice == "blue":
        print("you slowly open the blue door. A bright light shines from inside.")
        print("you walk into a samll quite room.there is a table in the middle with a box on it")
        print("you open the box and see lots of gold coins. you count them carefully.")
        print(" THERE ARE 50 coins! you take the coins and leave the room happily")
        coins = coins + 50

    elif doorchoice == "red":
        print("you slowly open the red door. It creaks loudly...")
        print(" you enter a dark and spooky room")
        print("oh theres a box under a table.")

        while True:
            openingboxchoice = input(" Do you open the box YES or NO ").upper().strip()
            
            if openingboxchoice == "YES":
                print(" you open the box and find 20 coins!")
                coins = coins + 20
                print(" you take the 20 coins and leave the room.")
                print("You now have: " + str(coins) + "coins")
                break
            
            elif openingboxchoice == "NO":
                print(" you leave the box and leave the room")
                print(" SUPRISINGLY you found a book that has clues inside.") 
                print("You read the book and find out that the murderer has sharp pointy teeth")
                print("The witch and the ninja both wearing a black outfit and has black hair but except of the vampire.") 
                print("You have to choose the right suspect based on the clues you have")
                break
            
            else:
                print("Please type YES or NO")
                continue

    else:
        print("Please type red or blue")
        continue
    
    print(" Now time for the second decision")
    print("You see some boxes:")
    print("1 - A black box")
    print("2 - A pink box")
    
    print(r"""" _   _
     ((\o/))
.-----//^\\-----.
|    /`| |`\    |
|      | |      |
|      | |      |
|      | |      |
'------===------'
""")
    
    boxchoice = input(" which box do you want").strip().lower()
    if boxchoice=="black":
        print("Oh no you encounterd a gosht. You lost 20 coins")
        coins= coins - 20
        print("You now have: " + str(coins) + "coins")
        
    elif boxchoice =="pink":
        print ("yayy you got a clue")
        print(" But make sure all the clues the compianion provide you won't forget")
        print("the clue is that the murder carrys lots of weapons.")
        
        print(r''')
                / /
               / /
  /============| |------------------------------------------,
{=| / / / / / /|()}     }     }     }                        >
  \============| |------------------------------------------'
               \ \
                \ \
                 \ \ ''')
        
    print(                       )
    print(                       )
    print("moving on....... ")
    
    print(" woww you encounterd 50 coins. Do you want to take the risk and accept the coins")
    
    coinchoice=input(" YES or NO").upper().strip()
    
    if coinchoice == "YES":
        print(" you take the coins and leave the room.")
        coins= coins + 50
        print("You now have: " + str(coins) + "coins")

        print(" Sadly you encounterd a ghost down the hall. What do you want to do?")
        print("1.loose 75 coins")
        print("2 Pay 150 to escape")
        print("You now have: " + str(coins) + "coins")

        escapechoice=input(" what do you choose to do?")
        
        if escapechoice == "1":
            coins= coins - 25
            print("You now have: " + str(coins) + "coins")
            if(coins < 50):
               print("Game Over!!")

        elif escapechoice == "2":
            coins= coins - 150
            print("You now have: " + str(coins) + "coins")

    elif coinchoice == "NO": 
        print(" you get a clue.")
        print("THE NINJA SHOE SIZE IS 39 , THE WITCH SHOE SIZE IS 38 AND THE VAMPAIRE SHOE SIZE IS 40")


    print("Now let's move on to the next option.")
    guesschoice = input("Do you want to guess? YES or NO: ").upper().strip()
    
    if guesschoice == "YES":
        print("Your choices are the ninja, the witch, or the vampire.")
        guess = input("Who do you think it is? ").strip().lower()
        
        print(                       )
        print(                       )
        
        if guess == "ninja":
            print(r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⣀⣠⣤⣶⣶⣶⠶⠾⠿⠿⠷⣷⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀            ⠀⠀ ⢀⣤⣶⠄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀
            ⠀⠀⣠⡾⢫⣿⠀⠀⠀⠀⠀⠀⢀⣴⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣾⠿⠿⠛⠛⠛⠛⠿⢷⣦⡀
⠀           ⣰⡿⠁⢸⣿⠀⠀⠀⠀⠀⣠⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡄⠀⠀⠀⠀⠀⠀⣀⣤⣾⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷
           ⢠⣿⠁⠀⢸⣿⠀⠀⠀⠀⣼⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣆⠀⢀⣠⣴⣾⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿
           ⢸⡇⠀⠀⢸⣿⠀⠀⠀⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠛⢻⣿⣿⠛⢉⣠⣤⣴⣶⣶⣶⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⣠⣾⠟
          ⣿⡇⠀⠀⢸⣿⠀⠀⠀⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡏⠀⡴⠋⠘⣿⡿⠛⠋⠉⠁⠀⠀⠀⠀⠈⠉⠛⠿⣿⣦⣄⢀⣴⡿⠃⠀
          ⢿⡇⠀⡄⠀⣿⡀⠀⢸⣿⠻⣿⣿⣦⣤⢤⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣶⣶⣿⡇⠞⠁⠀⢉⣿⡟⠛⠻⠿⢿⣶⣦⣄⠀⠀⠀⠀⠀⠈⠙⠻⠿⠛⠁⠀⠀
          ⢸⣇⠀⢱⠀⣿⡇⠀⠸⣿⠀⣿⡿⣿⣿⣧⠀⠀⢀⣈⣽⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⣿⣷⣶⣿⣿⡿⠿⣧⠀⠀⠀⠀⠀⠙⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠈⣿⡄⠈⣆⢹⣧⣀⡄⣿⡇⣿⢱⠘⣏⠉⠀⠀⠘⠛⠛⠛⠛⣻⡿⢿⠋⠉⠉⠙⠻⢿⣦⡀⠀⠀⠀⣠⠞⠁⢠⣿⠃⠀⢹⣧⠀⠀⠀⠀⠀⠀⠙⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠘⣿⣤⣼⠿⠟⢻⣇⢻⣷⠹⡎⢧⣸⠀⠀⠀⠀⠀⠀⠀⣸⡟⠁⢸⠀⠀⠀⠀⠀⠀⢙⣿⣆⡠⠞⠁⠀⣠⣿⠏⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⣴⡾⠛⠉⠀⠀⣠⣾⣿⣼⣿⡏⠛⠢⣭⣄⡀⠀⠀⠀⠀⢠⡟⠀⠀⠈⣆⠀⠀⠀⠀⣀⡾⠞⠉⠀⠀⣀⣴⡿⠋⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠸⣯⠀⣀⣴⠿⡏⠁⠙⠛⠛⠿⢷⣶⣤⣄⣉⠉⠒⠒⠲⠤⠤⠤⠤⠤⠼⠷⠖⠒⠉⠁⠀⠀⢀⣤⣾⠿⠋⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
             ⠀⠻⠟⠙⣿⣄⠹⣄⠀⣦⡀⠀⠀⠈⠉⠛⠿⢿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⢠⣿⠇⠀⠀⠀⣀⣀⣤⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀               ⢰⣾⠛⣠⣼⠿⢻⣿⣷⣤⡀⠀⠀⠀⠀⠀⠉⠙⠻⠿⣷⣦⣤⣶⣶⡾⢿⣿⡛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣤⣴⣾⠿⠟⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀               ⠙⠿⠻⣧⠀⠀⠻⣦⠙⢿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠦⠄⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀               ⠀⢹⣧⠀⠀⢹⣷⠀⠈⠙⢿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀               ⠀⠻⣧⡾⠟⠁⠀⠀⣠⣿⡟⠙⠛⠿⣷⣦⣄⡀⠀⠀⠀⠀⠀⣠⡄⠙⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⣰⣿⠋⠀⠀⠀⠀⠀⠈⠉⠉⠛⠒⠀⠀⣴⡏⠀⠀⠀⠈⠻⣷⣄⣠⣴⡶⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⢿⣦⣄⠀⠀⠀⠈⠛⠿⡁⣠⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⢰⣿⠃⠑⠦⢤⣀⣀⡀⠀⠀⠀⠀⠀⣀⣀⣘⣿⡀⠙⠿⣷⣄⠀⠀⠀⣠⠛⢿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⢀⣿⠏⠙⠦⢄⣀⣀⠀⠈⠉⠉⠉⠉⠉⣀⣀⡠⢿⣷⠀⡀⠈⠛⠿⠶⠿⠶⠶⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⣼⡿⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠻⣿⡝⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⢸⣿⢃⣤⣤⣀⡀⠀⣠⣾⣶⣶⣦⣤⣤⣤⣤⣤⣤⠀⠀⢙⣿⣦⡹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⣾⡿⠒⠒⠒⠤⢬⣽⡿⠋⠀⠈⠉⠉⠉⠛⢿⣦⣴⠒⣋⡥⠔⠻⣷⣵⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀         ⠀⢀⣴⣿⡇⠀⠀⠀⢠⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣀⠀⠀⠀⢈⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀          ⠀⠀⢿⣥⣿⣷⣶⣶⣶⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣻⠿⠿⠿⠛⠛⠀
""")
        print("YES! You got it right!")
        print("good job!)")
        break
        
    elif guess == "witch":
        print(r"""
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
;;;;;;;;;;;;;;;;;;;;;;;;;;;,::::::'""")
        print(                       )
        print(                       )
        print("OH NO! That's wrong!")
        print("GAME OVER!!")

        break
    
    elif guess == "vampire":
        print(r""""       __.......__
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
   .'           `-.   .-'           `.""")
        print(                       )
        print(                       )
        print("OH NO! That's wrong!")
        print("GAME OVER!!")
        break
    
    elif guesschoice == "NO":
        print("You chose not to guess.")
        break

    else: 
        print("invalid answer - GAME OVER")

