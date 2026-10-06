#CONSTANTS
HATCOST = 10
SWORDCOST = 30
PEARLCOST = 50
SCROLLCOST = 25

#VARIABLES
coins = 0
playername = ""
islandchoice = ""
mermaidchoice = ""
idolchoice = ""
crewmatechoice = ""
shopcoice = ""


while True:

#BOOLEANS
    gameover = False
    while not gameover:
        print("--PIRATE ADVENTURE-")
        print(r"""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⠀⠀⢀⣠⣤⣶⣶⣶⣶⣶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡔⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣫⣯⣷⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣷⡙⢿⣿⣿⣿⣿⣿⣿⡿⢋⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⠿⠿⠿⢟⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡏⠉⠙⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⡿⡍⠳⣄⡀⢀⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⢿⡄⠸⡿⢄⠛⣘⢠⣼⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡞⣼⡻⡄⠳⡤⠽⠾⠿⠿⠿⢛⣻⣿⣿⣿⣷⡀⠀⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣄⠙⢶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⢉⣁⣀⣀⣀⣀⣀⣉⡉⠙⠛⠻⢿⣿⣿⣿⣿⣿⣯⣻⣍⡲⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⢀⡀⣶⣤⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣁⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣈⠛⢿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⡿⠟⠛⠛⠁⠀⠀
⣰⣿⣿⣿⣿⣿⣿⣿⣝⢿⣿⣿⣿⣿⣿⣿⣟⣡⣶⠿⢛⣛⣉⣭⣭⣤⣤⡴⠶⠶⠶⠶⢲⣴⣤⠭⠭⡭⣟⠻⠦⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⣀⣠⣶⣿⣆⠀⠀
⠹⣿⣿⣿⣿⣿⣿⣙⠻⣿⣮⣛⠿⣿⣿⣿⣫⣵⡶⠟⣛⣋⣭⣭⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣮⣽⣿⣿⣿⠿⠟⠛⠉⢀⣴⣿⣿⣿⣿⣿⣿⣶⡀
⠀⠈⠙⠋⠁⠀⠈⠉⠛⠳⣭⣛⢷⣦⣸⣿⣯⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⡟⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⠿⠿⢿⣹⣿⣧⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⡏⣀⣴⣾⣿⣿⠿⠛⠉⠀⠀⠀⠈⠛⠛⠉⠀
⠀⠀⠀⠀⢀⣴⠿⠛⠋⠁⠀⠀⠀⢀⣯⢿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⠣⣟⡻⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⣀⣴⣾⣿⠈⡿⣿⠃⠀⠀⠀⠈⠉⠛⠻⠿⣿⣿⣿⣿⣿⠿⠛⠉⠉⠀⠈⠉⠛⣿⣽⡟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣤⣶⣾⣿⣿⣿⣿⣿⣀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣹⡟⣻⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⢹⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣰⣿⢣⡇⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠟⠋⠙⠛⠻⣿⣿⣿⣿⣿⠏⠀⠈⢿⣿⣿⣿⣦⣄⣀⣀⣀⣠⣴⣿⣏⡞⢻⣸⣿⣷⣄⠀⠀⣀⣤⠴⣾⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⠃⠀⠀⠀⠈⢿⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣶⠾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣏⠀⠀⠀⠀⠀⣀⣼⣿⡛⢿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠟⣡⣾⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⢠⣶⣿⣿⣯⣿⡇⠀⢹⣿⣿⣿⣿⣷⣤⣤⣦⣶⣿⣿⣿⣿⣿⡇⠀⣿⣿⢸⣿⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣠⣴⣾⣿⣟⣿⠟⠁⣿⡇⠀⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⡇⢀⣿⣿⠙⢮⣛⠿⣷⣦⣄⣀⣀⣀⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣶⣶⣾⣿⣿⡿⣛⣽⠞⠋⠀⠀⠀⣿⣷⠀⣍⠇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠉⡄⣸⣿⡿⠀⠀⠈⠙⠮⣟⠿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣹⣿⣿⣿⢵⡿⠋⠀⠀⠀⠀⠀⠀⢿⣿⣦⣿⡷⣄⠙⠿⣿⢹⣿⣿⢼⡿⠋⣡⣶⣳⣿⣿⣿⠃⠀⠀⠀⠀⠀⠈⠿⠬⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣷⣻⢿⣶⣬⣈⣉⣉⣤⣴⣿⣻⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⡇⣿⣇⣿⢹⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        playername = input("What is your name?: ")
        print("Ahoy, pirate ", playername, "!")
        print("You are sailing through the dark seas with your trusted crewmate, on the quest for coins. Two islands lie ahead in your path.")
        print(r"""          
              |    |    |                 
             )_)  )_)  )_)              
            )___))___))___)\            
           )____)____)_____)\\
         _____|____|____|____\\\__
---------\                   /---------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^
""")
        break

    print("1) Crystal Coves Island, with shimmering lagoons, pink reefs, and soft sand beaches covered in pearly seashells")
    print("2) Rainforest Island, with towering mountains, lush trees, and misty waterfalls.")
    islandchoice = input("Which one will you sail to, 1 or 2?: ")
    if islandchoice == "1":
        coins = coins + 150
        print("You arrive at Crystal Coves Island. The sunglight glimmers beautifully on the beach.")
        print(r"""       |
        \ _ /
      -= (_) =-
        /   \         _\/_
          |           //o\  _\/_
   _____ _ __ __ ____ _ | __/o\\ _
 =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
  =- _=-=- -_=-=_,-"          |
=- =- -=.--")""")
        print("You found 150 coins under the sand!")
        print("You hear a faint singing voice coming from the lagoon. You see a mermaid sitting on a rock, combing her hair. She beckons you to come closer.")
        print("Do you approach the mermaid? (yes or no)")
        mermaidchoice = input()
        if mermaidchoice == "yes":
            print(" The mermaid is actually a siren and she lures you into the water, where you are never seen again. Game Over!")
            break
        elif mermaidchoice == "no":
            print("You decide to stay away from the mermaid and continue your journey.")
            
    elif islandchoice == "2":
        coins = coins + 200
        print("You arrive at Rainforest Island. The humid air is filled with the sounds of exotic birds.")
        print(r"""           _    .  ,   .           .
    *  / \_ *  / \_      _  *        *   /\'__        *
      /    \  /    \,   ((        .    _/  /  \  *'.
 .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
    /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \
 /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
/        `.  / /       `.~-^=-=~=^=.-'      '-._ `._ """)
        print("You found 200 coins in a treasure box!")
        print("You arrive at Rainforest Island. The humid air is filled with the sounds of exotic birds. You found 200 coins in a treasure box!")
        print("You find an artifact in a cave. It is a intricately carved golden idol with mysterious engravings. Do you take the idol? (yes or no)")
        idolchoice = input()
        if idolchoice == "yes":
            print("You take the golden idol and it is cursed! You fall into a deep slumber. Game Over!")
            break
        elif idolchoice == "no":
            print("You decide to leave the golden idol and continue your journey.") 
    print("On voyage across the seas, you and your crewmate get into a heated argument over who has to scrub the deck.")
    print(r""" 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠤⠒⢒⣉⣉⠉⠁⠀⠉⢉⣉⠁⠒⠂⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⣋⠠⠔⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠢⠤⣉⠒⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⣉⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠢⣌⠑⢄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⣡⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠱⣄⠙⢦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⢁⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⣄⠳⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠘⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡎⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠘⣆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⢸⡄
⠀⠀⠀⠀⠀⠀⠀⢰⢃⠁⠀⠀⠀⣴⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣶⡀⠀⠀⠀⠈⣧
⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⣾⠏⠀⠈⢹⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣟⠉⠁⠀⢻⡄⠀⠀⠃⣽
⠀⠀⠀⠀⠀⢀⣠⠞⠃⢄⣀⣾⡏⠀⠀⠀⢼⣿⣿⣿⣿⡶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣠⣼⣾⣿⣿⣿⣿⠀⠀⠀⠀⣧⠀⠀⠠⣽
⠀⠀⠀⢀⡞⠇⠀⠀⠀⠀⠈⠉⠙⠢⢄⡀⠀⠙⠻⠿⠛⠁⠀⠉⠳⣤⡀⠀⠀⠀⠀⠀⣠⣶⠋⠁⠀⠙⠻⠿⠟⠁⠀⠀⠀⠀⡟⡆⠀⡁⣾
⠀⠀⢠⠞⠁⠀⠀⠀⠀⣀⠀⠀⠀⠀⠨⠑⣒⠢⡄⠀⠀⠀⠀⠀⢠⡽⠃⠀⠀⠀⠀⠠⣹⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣳⠁⠀⢡⣿
⠀⣰⠣⠌⠀⠀⠀⠀⠀⠈⠑⠢⢄⡀⠀⠀⣸⠁⡞⠀⠀⠀⢀⣤⠟⠁⠀⠀⠀⠀⠀⠀⠀⢝⢦⡀⠀⠀⠀⠀⠀⠀⠀⣀⡾⡱⠁⠀⡐⢢⡟
⢠⠋⢷⠀⠀⠀⠀⠀⢄⡀⠀⠀⠀⠈⠉⢩⠁⢸⠧⠴⠦⠖⠋⢁⣠⣴⣶⣶⣿⣿⣶⣶⣦⣄⠁⠩⣓⠤⠤⠴⠤⠶⡛⠍⠈⠀⠀⠀⠼⣹⠃
⣼⢸⠈⠀⠀⠀⠀⠀⠀⠈⠑⠢⢄⡀⠀⣘⣦⠟⠀⠈⠁⠀⣰⣿⡿⠟⠋⠉⠉⠉⠩⠉⡛⠿⣿⣦⡀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠠⣉⢾⡇⠀
⢸⡁⠊⠀⠀⠐⠒⠒⠤⢄⡀⠀⠀⢀⠗⠀⠀⠀⠀⠀⠀⣸⡿⠋⠀⠀⠀⠀⠀⢀⠖⣩⠍⠉⠒⠋⠃⠀⠉⠁⠘⠒⢦⠀⠀⢄⠣⣼⠏⠀⠀
⠘⣦⠁⠀⠀⠀⠀⠀⠀⠀⠀⣭⣖⢢⠀⡀⠀⠀⠀⠀⣸⡟⡔⠀⠀⠀⠀⠀⠀⢸⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⣱⢨⣌⣿⠃⠀⠀⠀
⠀⠈⠳⢄⣀⣀⣘⡱⠖⠒⠛⠁⠙⢧⣇⠔⡠⢀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠘⢀⠌⠙⠒⠚⠋⠉⠀⠁⠀⠀⠀⠀⢢⢱⠞⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠾⣄⠣⣌⠠⠁⠀⡀⠀⠀⠀⠀⠀⠀⠈⠚⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⢸⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠦⣧⡑⠦⡄⠡⢌⠐⢠⠂⡐⢀⢂⠌⠉⠉⠉⠁⠈⠀⠀⠀⠀⠀⠀⡘⢠⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠫⠷⣌⣞⣤⣓⣌⣖⣸⣮⣤⠀⠠⠤⠤⠤⢀⡀⠀⠀⠠⢐⢠⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⡀⠀⠀⠀⠀⠀⠀⠀⡁⢂⣽⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡒⠄⠀⠀⠀⠠⣄⠿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠢⠴⠴⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    print("1) Meet in the middle and compromise on a solution")
    print("2) Settle the argument with a sword duel")
    print("3) Throw your crewmate overboard")
    crewmatechoice = input("What do you do? (1, 2, or 3): ")
    if crewmatechoice == "1":
        print("You and your crewmate compromise and agree to take turns scrubbing the deck. You've made peace!")
    elif crewmatechoice == "2":
        print("You draw your sword, but your crewmate is a skilled fighter and knocks it out of your hand. You lose the duel! Game Over!")
        break
    elif crewmatechoice == "3":
        coins = 0
        print("Your crewmate sinks into the dark depths of the ocean, but all the coins you collected were with them!")
    print("Welcome to the pirate shop, " + playername + "! The merchant has a variety of items for sale.")
    print("hat: 10 coins")
    print(r"""      _____
    
               (/;
              (/;
       .--..-(/;
       |    (/;
     __|====/=|__
    (____________) """)
    print("sword: 30 coins")
    print(r"""      
        // \
        || |
        || |
        || |
        || |
        || |
        || |
     __ || | __
    /___||_|___\
         ww
         MM
        _MM_
       (&<>&)
        ~~~~""")
    print("pearl: 50 coins")
    print(r""" 
      _._
    .'--.`.    
    |  .' |   
     `--`'   """)
    print("scroll: 25 coins")
    print(r"""
    (\ 
    \'\ 
     \'\     __________  
     / '|   ()_________)
     \ '/    \ ~~~~~~~~ \
       \       \ ~~~~~~   \
       ==).      \__________\
      (__)       ()__________)
    """)
    print("You have ", coins, " coins. ")
    shopchoice = input("What would you like to buy? (hat, sword, pearl, scroll, or nothing): ")
    if shopchoice == "hat":
        if coins >= HATCOST:
            coins -= HATCOST
            print("You bought a hat! You have ", coins, " coins left.")
        else:
            print("You don't have enough coins to buy a hat.")
    elif shopchoice == "sword":
        if coins >= SWORDCOST:
            coins -= SWORDCOST
            print("You bought a sword! You have ", coins, " coins left.")
        else:
            print("You don't have enough coins to buy a sword.")
    elif shopchoice == "pearl":
        if coins >= PEARLCOST:
            coins -= PEARLCOST
            print("You bought a pearl! You have ", coins, " coins left.")
        else:
            print("You don't have enough coins to buy a pearl.")
    elif shopchoice == "scroll":
        if coins >= SCROLLCOST:
            coins -= SCROLLCOST
            print("You bought a scroll! You have ", coins, " coins left.")
        else:
            print("You don't have enough coins to buy a scroll.")
    elif shopchoice == "nothing":
        print("You chose not to buy anything. You have ", coins, " coins left.")
    print("Pirate " + playername + ", your journey has come to an end. Thank you for playing Pirate Adventure!")
    print(r"""
    ⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⡀⠙⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠸⠿⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡠⠄⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿
⣿⣿⣽⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⠇⠁⠀⠀⠀⠘⣿⣿⣿⣿⢿⣿⡿⢋⣾⣿⣿⣿⣿⣿
⣿⣽⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣷⣶⣶⢰⣶⣶⣽⣿⣿⣿⢸⡟⠁⣼⣿⣿⣿⣿⣿⣿
⣿⡿⣽⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⠛⠛⠛⠛⠛⠘⠛⠉⠉⣩⣿⣿⢈⠂⢠⣿⣿⣿⣿⣿⣿⣿
⣿⣮⣽⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣁⡥⠅⠀⢀⠈⠀⢠⡾⡿⣷⠀⠀⠀⣰⣿⡿⣡⠏⠀⣼⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣟⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣸⠋⠀⠀⠀⡎⠀⠀⠐⣶⡱⠜⠀⠀⢠⣿⡟⡰⠁⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣾⣷⣿⣿⣿⣿⣿⣿⣿⣿⡇⠃⠀⠀⠀⠐⡇⠀⠚⠢⢅⡊⠤⠴⠀⢸⡿⠀⠁⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿
⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⡓⠀⢀⣤⣀⠀⣇⠀⠋⠁⠀⠈⠑⠖⠀⠸⠃⡀⣐⠂⠠⠬⠐⠒⣚⣻⣿⣿⣿⣿
⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠉⠛⠀⣼⣦⢀⣴⣶⣶⠶⠄⠀⠀⠿⠃⠀⠀⠀⠄⠀⣸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠈⠿⠿⠿⠷⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠒⠒⠂⠀⠀⢠⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠿⠿⠿⠿⠿⠿⠿⢿
⡿⣽⢿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣂⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠐⠒⠲⠶⠶⢶⣶⣶⣾⣶⣿⣿⣿
⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""")
    print(r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠤⠤⠄⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠤⠒⠒⠒⠒⠒⠒⠒⠒⡲⠶⠶⠶⠦⠴⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠊⠁⠀⠀⠀⠀⣠⣤⠞⠉⠀⠀⣨⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠊⢁⠤⠒⠒⠐⢢⠀⠀⠀⡤⠚⠁⠀⠀⠀⠀⣀⠤⢤⡀⠀⠀⠀⠀⠀⠀⢠⣞⠁⠀⠀⠀⠀⢀⣼⡋⠀⠀⢀⡠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⡇⠒⠁⠀⠀⢀⡠⠎⣀⣶⠋⠀⠀⠀⠀⠀⣠⠊⠁⡠⠚⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣀⣀⣀⣀⣸⡥⠔⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴
⠀⠀⠀⠀⠀⠀⠈⠒⠒⠒⠊⠁⢀⣴⡟⠃⠀⠀⠀⢀⣠⠞⣀⠴⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠖⠛⠛⠷⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠛⢻
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⣾⣟⠂⠀⠀⢀⣰⣿⡗⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠏⠁⠀⢀⡶⠤⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⡟⠃⠀⠀
⢀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⡁⠀⠀⣠⣴⣿⣿⠓⡧⠀⢀⣠⡤⣶⡆⠀⠀⠀⠀⠀⠀⠀⢰⡟⡗⣀⠔⠊⠁⠀⠀⢀⡼⢀⣠⢴⣦⣠⣴⣲⠀⢀⣠⡤⠔⣦⣴⡏⠂⠀⠀⠀⠀
⣿⠷⠀⠀⠀⠀⠀⢀⡴⠟⠋⠀⠀⠀⣺⣿⡟⠋⣼⡿⣃⣼⠿⡟⢉⡸⠆⠀⠀⠀⠀⠀⠀⠀⠸⡀⠺⠃⠀⠀⠀⢀⡠⠚⠀⢋⣴⣿⠋⣱⣿⣟⣴⣿⣛⣤⡶⣏⣳⠆⠀⠀⠀⠀⠀
⠈⠑⠒⠒⠒⠒⠉⠁⠀⠀⠀⠀⠀⠐⠛⠁⠀⠀⠛⠋⠁⠹⠖⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠀⠒⠒⠈⠁⠀⠀⠐⠻⠃⠀⠀⠙⠛⠁⠘⠞⠋⠘⠷⠋⠀⠀⠀⠀⠀⠀⠀
    """)
    break 
