#final
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
shopchoice = ""

while True:
    gameover = False
    coins = 0
    playername = ""
    islandchoice = ""
    mermaidchoice = ""
    idolchoice = ""
    crewmatechoice = ""
    shopchoice = ""

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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        playername = input("What is your name?: ").strip()
        if not playername:
            playername = "Captain"
        print("Ahoy, pirate", playername, "!")
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
    islandchoice = input("Which one will you sail to, 1 or 2?: ").strip().lower()
    if islandchoice == "1":
        coins += 150
        print("You arrive at Crystal Coves Island. The sunlight glimmers beautifully on the beach.")
        print(r"""       
        \ _ /
      -= (_) =-
        /   \         _\/_
          |           //o\  _\/_
   _____ _ __ __ ____ _ | __/o\\ _
  =-=-_-__=_-= _=_=-=_,-|"'""|-,_
   =- _=-=- -_=-=_,-"        |
  =- =- -=.--")""")
        print("You found 150 coins under the sand!")
        print("You hear a faint singing voice coming from the lagoon. You see a mermaid sitting on a rock, combing her hair. She beckons you to come closer.")
        mermaidchoice = input("Do you approach the mermaid? (yes or no): ").strip().lower()
        if mermaidchoice == "yes":
            print("The mermaid is actually a siren and she lures you into the water, where you are never seen again. Game Over!")
            gameover = True
        elif mermaidchoice == "no":
            print("You decide to stay away from the mermaid and continue your journey.")
        else:
            print("Invalid choice. You step back and continue your journey.")

    elif islandchoice == "2":
        coins += 200
        print("You arrive at Rainforest Island. The humid air is filled with the sounds of exotic birds.")
        print(r"""           _    .  ,   .           .
    *  / \_ *  / \_      _  *        *   /\'__        *
      /    \  /    \,   ((        .    _/  /  \  *'.
  .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
    /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
  /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \
 /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
/        `.  / /       `.~-^=-=~=-=.-'      '-._ `._ """)
        print("You found 200 coins in a treasure box!")
        print("You find an artifact in a cave. It is a intricately carved golden idol with mysterious engravings. Do you take the idol? (yes or no)")
        idolchoice = input().strip().lower()
        if idolchoice == "yes":
            print("You take the golden idol and it is cursed! You fall into a deep slumber. Game Over!")
            gameover = True
        elif idolchoice == "no":
            print("You decide to leave the golden idol and continue your journey.")
        else:
            print("Invalid choice. You leave the cave and continue your journey.")
    else:
        print("That island does not exist. You drift around aimlessly and lose time.")
        gameover = True

    if gameover:
        play_again = input("Would you like to play again? (yes or no): ").strip().lower()
        if play_again != "yes":
            break
        continue

    print("On voyage across the seas, you and your crewmate get into a heated argument over who has to scrub the deck.")
    print(r""" 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠤⠒⢒⣉⣉⠉⠁⠀⠉⢉⣉⠁⠒⠂⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⣋⠠⠔⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠢⠤⣉⠒⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⣉⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠢⣌⠑⢄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⢁⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠱⣄⠙⢦⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⣄⠳⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡎⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠘⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⢸⡄
⠀⠀⠀⠀⠀⠀⠀⠀⢰⢃⠁⠀⠀⠀⣴⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣶⡀⠀⠀⠀⠈⣧
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⣾⠏⠀⠈⢹⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣟⠉⠁⠀⢻⡄⠀⠀⠃⣽
⠀⠀⠀⠀⢀⣠⠞⠃⢄⣀⣾⡏⠀⠀⠀⢼⣿⣿⣿⣿⡶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣠⣼⣾⣿⣿⣿⣿⠀⠀⠀⠀⣧⠀⠀⠠⣽
⠀⠀⠀⠀⢀⡞⠇⠀⠀⠀⠀⠈⠉⠙⠢⢄⡀⠀⠙⠻⠿⠛⠁⠀⠉⠳⣤⡀⠀⠀⠀⠀⠀⣠⣶⠋⠁⠀⠙⠻⠿⠟⠁⠀⠀⠀⠀⡟⡆⠀⡁⣾
⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⣀⠀⠀⠀⠀⠨⠑⣒⠢⡄⠀⠀⠀⠀⠀⢠⡽⠃⠀⠀⠀⠀⠠⣹⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣳⠁⠀⢡⣿
⠀⠀⣰⠣⠌⠀⠀⠀⠀⠀⠈⠑⠢⢄⡀⠀⠀⣸⠁⡞⠀⠀⠀⢀⣤⠟⠁⠀⠀⠀⠀⠀⠀⠀⢝⢦⡀⠀⠀⠀⠀⠀⠀⠀⣀⡾⡱⠁⠀⡐⢢⡟
⢠⠋⢷⠀⠀⠀⠀⠀⢄⡀⠀⠀⠀⠈⠉⢩⠁⢸⠧⠴⠦⠖⠋⢁⣠⣴⣶⣶⣿⣿⣶⣶⣦⣄⠁⠩⣓⠤⠤⠴⠤⠶⡛⠍⠈⠀⠀⠀⠼⣹⠃
⣼⢸⠈⠀⠀⠀⠀⠀⠀⠈⠑⠢⢄⡀⠀⣘⣦⠟⠀⠈⠁⠀⣰⣿⡿⠟⠋⠉⠉⠉⠩⠉⡛⠿⣿⣦⡀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠠⣉⢾⡇⠀
⢸⡁⠊⠀⠀⠐⠒⠒⠤⢄⡀⠀⠀⢀⠗⠀⠀⠀⠀⠀⠀⣸⡿⠋⠀⠀⠀⠀⠀⢀⠖⣩⠍⠉⠒⠋⠃⠀⠉⠁⠘⠒⢦⠀⠀⢄⠣⣼⠏⠀⠀
⠘⣦⠁⠀⠀⠀⠀⠀⠀⠀⠀⣭⣖⢢⠀⡀⠀⠀⠀⠀⣸⡟⡔⠀⠀⠀⠀⠀⠀⢸⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⣱⢨⣌⣿⠃⠀⠀⠀
⠀⠀⠈⠳⢄⣀⣀⣘⡱⠖⠒⠛⠁⠙⢧⣇⠔⡠⢀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠘⢀⠌⠙⠒⠚⠋⠉⠀⠁⠀⠀⠀⠀⢢⢱⠞⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠾⣄⠣⣌⠠⠁⠀⡀⠀⠀⠀⠀⠀⠀⠈⠚⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⢸⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠦⣧⡑⠦⡄⠡⢌⠐⢠⠂⡐⢀⢂⠌⠉⠉⠉⠁⠈⠀⠀⠀⠀⠀⠀⡘⢠⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠫⠷⣌⣞⣤⣓⣌⣖⣸⣮⣤⠀⠠⠤⠤⠤⢀⡀⠀⠀⠠⢐⢠⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⡀⠀⠀⠀⠀⠀⠀⠀⡁⢂⣽⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡒⠄⠀⠀⠀⠠⣄⠿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠢⠴⠴⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    print("1) Meet in the middle and compromise on a solution")
    print("2) Settle the argument with a sword duel")
    print("3) Throw your crewmate overboard")
    crewmatechoice = input("What do you do? (1, 2, or 3): ").strip().lower()
    if crewmatechoice == "1":
        print("You and your crewmate compromise and agree to take turns scrubbing the deck. You've made peace!")
    elif crewmatechoice == "2":
        print("You draw your sword, but your crewmate is a skilled fighter and knocks it out of your hand. You lose the duel! Game Over!")
        gameover = True
    elif crewmatechoice == "3":
        coins = 0
        print("Your crewmate sinks into the dark depths of the ocean, but all the coins you collected were with them!")
    else:
        print("Invalid option. Your crewmate storms off in frustration.")
        gameover = True

    if gameover:
        play_again = input("Would you like to play again? (yes or no): ").strip().lower()
        if play_again != "yes":
            break
        continue

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
    /___|||___\
         ww
         MM
        _MM_
       (&<>&)
        ~~~~""")
    print("pearl: 50 coins")
    print(r""" 
      _._
    .'--.'.    
    |  .' |   
     `--`'   """)
    print("scroll: 25 coins")
    print(r"""
    (\ 
    '\' 
     '\'     __________  
     / '|   ()_________)
     \ '/    \ ~~~~~~~~ \
       \       \ ~~~~~~   \
       ==).      \__________\
      (__)       ()__________)
    """)
    print("You have", coins, "coins.")
    shopchoice = input("What would you like to buy? (hat, sword, pearl, scroll, or nothing): ").strip().lower()
    if shopchoice == "hat":
        if coins >= HATCOST:
            coins -= HATCOST
            print("You bought a hat! You have", coins, "coins left.")
        else:
            print("You don't have enough coins to buy a hat.")
    elif shopchoice == "sword":
        if coins >= SWORDCOST:
            coins -= SWORDCOST
            print("You bought a sword! You have", coins, "coins left.")
        else:
            print("You don't have enough coins to buy a sword.")
    elif shopchoice == "pearl":
        if coins >= PEARLCOST:
            coins -= PEARLCOST
            print("You bought a pearl! You have", coins, "coins left.")
        else:
            print("You don't have enough coins to buy a pearl.")
    elif shopchoice == "scroll":
        if coins >= SCROLLCOST:
            coins -= SCROLLCOST
            print("You bought a scroll! You have", coins, "coins left.")
        else:
            print("You don't have enough coins to buy a scroll.")
    elif shopchoice == "nothing":
        print("You chose not to buy anything. You have", coins, "coins left.")
    else:
        print("Invalid choice. The merchant shrugs and keeps the goods. ")

    print("Pirate", playername + ", your journey has come to an end. Thank you for playing Pirate Adventure!")
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠤⠒⠒⠒⠒⠒⠒⠒⠒⡲⠶⠶⠶⠦⠴⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠊⠁⠀⠀⠀⠀⣠⣤⠞⠉⠀⠀⣨⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠊⢁⠤⠒⠒⠐⢢⠀⠀⠀⡤⠚⠁⠀⠀⠀⠀⣀⠤⢤⡀⠀⠀⠀⠀⠀⠀⢠⣞⠁⠀⠀⠀⠀⢀⣼⡋⠀⠀⢀⡠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⡇⠒⠁⠀⠀⢀⡠⠎⣀⣶⠋⠀⠀⠀⠀⠀⣠⠊⠁⡠⠚⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣀⣀⣀⣀⣸⡥⠔⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴
⠀⠀⠀⠀⠀⠀⠀⠈⠒⠒⠒⠊⠁⢀⣴⡟⠃⠀⠀⠀⢀⣠⠞⣀⠴⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠖⠛⠛⠷⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠛⢻
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⣾⣟⠂⠀⠀⢀⣰⣿⡗⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠏⠁⠀⢀⡶⠤⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⡟⠃⠀⠀
⢀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⡁⠀⠀⣠⣴⣿⣿⠓⡧⠀⢀⣠⡤⣶⡆⠀⠀⠀⠀⠀⠀⠀⢰⡟⡗⣀⠔⠊⠁⠀⠀⢀⡼⢀⣠⢴⣦⣠⣴⣲⠀⢀⣠⡤⠔⣦⣴⡏⠂⠀⠀⠀⠀
⣿⠷⠀⠀⠀⠀⠀⢀⡴⠟⠋⠀⠀⠀⣺⣿⡟⠋⣼⡿⣃⣼⠿⡟⢉⡸⠆⠀⠀⠀⠀⠀⠀⠀⠸⡀⠺⠃⠀⠀⠀⢀⡠⠚⠀⢋⣴⣿⠋⣱⣿⣟⣴⣿⣛⣤⡶⣏⣳⠆⠀⠀⠀⠀⠀
⠈⠑⠒⠒⠒⠒⠉⠁⠀⠀⠀⠀⠀⠐⠛⠁⠀⠀⠛⠋⠁⠹⠖⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠀⠒⠒⠈⠁⠀⠀⠐⠻⠃⠀⠀⠙⠛⠁⠘⠞⠋⠘⠷⠋⠀⠀⠀⠀⠀⠀⠀
    """)

    play_again = input("Play again? (yes or no): ").strip().lower()
    if play_again != "yes":
        break

    # reset variables for a fresh game
    coins = 0
    playername = ""
    islandchoice = ""
    mermaidchoice = ""
    idolchoice = ""
    crewmatechoice = ""
    shopchoice = ""

    print("\nStarting a new adventure...\n")
