#SecondCheckpoint - look for comments below from Ms. Christine
#Hi Kevin, please organize your code so that...

#imports go under here -----

#constants go under here -----

#variables go under here -----


print("Final test")

import time #any imports from the library - these should go at the very top before your constants and variables

def slow(text):
    print(text)
    time.sleep(0.9)

def game_over(reason):
    print("\n--- GAME OVER ---")
    slow(reason)
    exit()


print("The flipped world")
name = input("Your name: ")

slow(f"\n*Once upon a time {name} and Noelle is playing in the mountain but then both of them them accidently fall into a dark hole by accident.")
slow("* They land in the FLIPPED WORLD, where unliving things comes to life.")
print(r"""           -^- 
       _/\/_  \/\_
      (____ ))____)
       / -     - \
      / ( ^)-(^ ) \
     / ____v-v____ \
     \(-    _-  __)/
      -\-  -__---/-
       /  / V \   \
      /__/\   /    \
     =      V       =
   _=_              _=_
     -=---______---=-
        _| | | |_
       (___- -___)
""")
slow("\n* You saw a prince in the shadow and then he starts speaking.")
slow("* 'The 3 heros just like the prophecy said'")
slow("* 'The ROARING KNIGHT created this world.'")
slow("* 'If you don't stop him he will release the TITAN(a very scary monster) and then it's the end of the world.'")
slow("* Noelle has ice magic that will be useful in your journey. ")


mercy_count = 0 #you should have your constants at the top, after the imports

#EVENT ONE
slow("\n* A poker looking enemy appears!")
print(r"""
        .----------------.
       |  A          ♠   |
       |                 |
       |      _____      |
       |     /     \     |
       |    |  O O  |    |
       |    |   ^   |    |
       |     \ \_/ /     |
       |      \___/      |
       |        |        |
       |      __|__      |
       |     /  |  \     |
       |    /   |   \    |
       |       / \       |
       |   ♠          A  |
        '----------------'
""")

slow("* 'If you want to stop the knight you need to go pass me first!'")
print("1.Fight  2.Mercy") #you should specify if the player should type 1 or 2 or the words fight or mercy 
choice = input("> ")

if choice == "1":
    slow("* Noelle freezes it with her magic like you tell her to do...")
elif choice == "2":
    slow("* You spare it. Noelle is relieved.")
    mercy_count += 1
else:
    game_over("* You froze. The enemy got you.") #what if the user input another choice - an invalid choice? what will you do to make sure the game doesn't just end for them?

#EVENT TWO
slow("\n* Another enemy blocks the path!")
print(r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠿⠸⢇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⠀⠘⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣀⠶⢶⣾⠷⣶⣶⣆⣀⣀⣉⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠒⢺⣭⡍⠀⠀⠹⢢⣭⣭⡽⢯⡽⠿⠙⢻⡗⠲⣤⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⣦⠀⠀⠀⠀⠀⠘⠛⠛⠃⠀⠀⠀⢘⣛⣛⡦⠤⠤⠤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⣀⠶⠞⠉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠛⠀⠀⠀⡼⢻⡇⠀⠀⢀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⠁⢸⡇⠀⢀⡸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣶⠉⠀⠀⣶⠉⢰⡎⠁⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⠛⠀⢀⡸⠇⠀⡸⠇⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⡏⠁⠀⢸⡇⠀⠀⣇⠀⠀⣶⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣤⣤⣤⣴⡏⠁⠀⣀⡏⠀⠀⣿⠁⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣾⣉⣀⣀⣀⣀⣀⣀⣀⠿⠀⠀⣶⠉⠀⠀⠸⠶⠶⠶⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⢰⣯⣤⣤⣤⣤⣤⣤⣤⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀ """)
print("1.Fight  2.Mercy")  #you should specify if the player should type 1 or 2 or the words fight or mercy 
choice = input("> ")

if choice == "1":
    slow("* Noelle cast ICE SHOCK. It shatters. She looks away.")
elif choice == "2":
    slow("* You spare it. It bows and disappears.")
    mercy_count += 1
else:
    game_over("* You froze. The enemy got you.")

ring = False #you should have your variables/boolean values at the top, after the imports - even if they appear later on in your game

#EVENT THREE
if mercy_count == 0:
    slow("\n* A Dealer appears and offered you the ThornRing.")
    slow("* But you don't have enough money to buy it...")
    slow("* Noelle stares at it. She looks... tempted.")
    print("1.PROCEED  2. Leave")  #you should specify if the player should type 1 or 2 or the words proceed or leave 
    choice = input("> ")

    if choice == "1":
        slow("\n* 'Wait... are you sure about this?'")
        slow("* 'But we don't have enough money to buy it...'")
        slow("* 'This isn't right.'")
        print("1. PROCEED  2. Leave") 
        choice2 = input("> ")

        if choice2 == "1":
            slow("\n* 'PROCEED.'")
            slow("* 'I hope you know what you're doing.'")
            slow("* She cast SNOW GRAVE. She looks away")
            slow("* The Dealer is frozen You Got The ThornRing...")
            ring = True
        elif choice2 == "2":
            slow("\n* 'LEAVE.'")
            slow("* Noelle sighs in relief.")
            slow("* You leave the Dealer and continue your journey.")
        else:
            slow("\n* You stood there too long. The Dealer left")
    elif choice == "2":
        slow("\n* You leave, Noelle believes its all just a nightmare")
    else:
        slow("\n* The Dealer never appears.")
        if mercy_count == 2:
            slow("* Noelle smiles. 'Maybe we can do this without hurting anyone.'")


slow("\n* You reach the castle. The ROARING KNIGHT is waiting for you.")
slow("* 'So you have come to stop me?'")
slow("* 'funny, I was just about to release the TITAN.'")
slow("* 'Hahahaha.'")
print(r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣸⣄⠀⠀⠠⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣦⡏⠈⢀⣴⣄⣁⣽⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⡧⣤⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⢷⣶⣦⣤⣤⣝⣯⣝⢫⣾⣷⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣮⣿⡿⢿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⠿⠋⠉⠀⠀⢼⣍⣭⣟⠋⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣴⠶⣿⡇⠀⠀⠀⠀⠀⣰⣿⢿⣿⡓⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢻⣶⣿⠰⠆⠀⠀⠀⣴⣿⠃⢸⣿⠀⠀⠠⣼⢿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⡇⠀⢸⡟⠀⠀⠀⠀⠈⠯⣾⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣀⣼⡇⠀⠀⠀⠀⠀⠀⠘⢿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣦⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣛⠿⣿⣦⣀
""")




if mercy_count == 2:
    slow("* You and Noelle stand together.")
    slow("1.Talk  2.Fight")
    choice = input("> ")
    if choice == "1":
        slow("* 'We don't want to fight you.'")
        slow("* 'We just want to stop you from releasing the TITAN.'")
        slow("* 'Please, we can do this without hurting anyone.'")
        slow("* The ROARING KNIGHT looks at you and then he smiles.")
        slow("* Together, you seal the Flipped World.'")
        ending = "GOOD"
    elif choice == "2":
        slow("* 'I see. You want to fight me.'")
        slow("* 'I accept your challenge.'")
        slow("* You fight against the ROARING KNIGHT but it's too powerful.")
        slow("* The ROARING KNIGHT releases the TITAN.")
        ending = "TITAN"
    else:
        game_over("* You hesitated. The ROARING KNIGHT slice you in half.")

elif ring:
    slow("* The ROARING KNIGHT looks at Noelle's fingers and stops.")
    slow("* 'That ring... I see you have the ThornRing.'")
    slow("* ...")
    slow("* 1.Proceed  2.PROCEED")
    choice = input("> ")
    if choice == "1" or choice == "2":
        slow("* Noelle cast SNOW GRAVE. The ground is shaking.")
        slow("* You and Noelle leave the Flipped World")
        ending = "NOELLE_PUSH"

elif mercy_count == 1: 
    slow("* The ROARING KNIGHT laughs. 'You killed one, spared one.")
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠄⢄⠀⣤⡠⢄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣴⣶⣶⣶⣶⠤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠈⠉⠉⠀⠉⠙⠛⠛⠛⠛⠛⠛⠹⠿⠿⠿⠷⠿⠾⠿⠶⠿⠿⠿⠿⠿⠟⠎⠝⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    slow("* He slice you in half.")
    slow("* The ROARING KNIGHT releases the TITAN.'")
    ending = "DREAM"
else:
    slow("* The ROARING KNIGHT laughs. 'You killed all of them!.'")
    slow("* 'You are just like me!.'")
    slow("* 'The ROARING KNIGHT releases the TITAN.'")
    ending = "DREAM"

print("\n"+"="*30)

if ending == "GOOD":
    slow("* You and Noelle return to the real world.")
    slow("* 'We did it!'")
    slow("* 'We stopped the ROARING KNIGHT and saved the Flipped World.'")
    slow("* 'I guess we can go back to our normal lives now.'")
    slow("* 'But I will never forget this adventure.'")
    slow("* 'Me neither.'")
    slow("\n* THE END")

elif ending == "TITAN":
    slow("* The TITAN releases from the Flipped World.")
    slow("* 'We failed...'")
    slow("* 'The world is doomed.'")
    print(r"""⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⡀⠀⠀⠀⠀⠀⠀⣠⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⣀⣀⡠⠄
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⠿⣿⣿⣿⣿⣟⠘⠛⠻⠿⣿⣿⣿⣿⣤⣤⣿⠿⠟⠃⠀⠀
    ⠤⢤⣀⣀⣀⣀⣀⣤⣾⡿⠻⣿⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠘⠿⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠉⠉⠛⠻⣿⣿⣤⡀⠛⣿⣿⣿⠿⠟⠃⠀⠀⠀⠀⣀⣴⣾⡿⠂⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣦⣤⣤⣀⣤⣤⣶⣶⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⠉⠉⠛⠟⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⠶⠒⠁⠌⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⢀⣴⣿⣿⣿⣿⣿⣷⣶⣤⣤⣶⣾⠟⠛⠉⠀⠀  ⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠛⢻⣿⣿⡿⠿⣿⣿⡏⠉⠻⢿⣿⣷⠀⠀⠀⠀⠀⠄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢰⣿⡛⠁⠀⠀⠻⣿⣿⣶⣿⣿⠁⠀⢀⣴⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⣤⣀⣀⣀⡉⠉⠉⣀⣠⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢀⣤⠞⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⣴⡿⠛⠉⠉⠙⠿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⠁⠀⠀⠀
    ⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠜⠁⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣦⣶⣶⣶⣾⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡿⠟⠉⠉⠠⣿⣍⣽⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠒⠒⠿⢿⣿⡟⠁⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⡿⠋⣻⣿⣿⣿⣷⣶⣤⣤⣠⡀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣶⣤⣀⠀⡀⠀⠀⠈⣛⣉⣩⣶⣾⠟⠋⠁⠀⠀⡇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀ ⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⡿⠿⠿⣿⡿⠿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀⠀⠀⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    slow("\n* THE END")

elif ending == "NOELLE_PUSH":
    slow("* The ROARING KNIGHT is defeated.")
    slow("* You see the light home again.")
    slow("* But then...")
    slow("* Noelle pushes you down in the hole.")
    slow(f"* 'Sorry {name}. I can't let you go back to the real world.'")
    slow("* 'She cast SNOW GRAVE to you and you are frozen...'")
    slow("\n* THE END")

elif ending == "DREAM":
    slow("* The TITAN is released from the Flipped World.")
    print(r"""⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⡀⠀⠀⠀⠀⠀⠀⣠⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⣀⣀⡠⠄
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⠿⣿⣿⣿⣿⣟⠘⠛⠻⠿⣿⣿⣿⣿⣤⣤⣿⠿⠟⠃⠀⠀
⠤⢤⣀⣀⣀⣀⣀⣤⣾⡿⠻⣿⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠘⠿⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠉⠛⠻⣿⣿⣤⡀⠛⣿⣿⣿⠿⠟⠃⠀⠀⠀⠀⣀⣴⣾⡿⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣦⣤⣤⣀⣤⣤⣶⣶⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⠉⠉⠛⠟⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⠶⠒⠁⠌⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⢀⣴⣿⣿⣿⣿⣿⣷⣶⣤⣤⣶⣾⠟⠛⠉⠀⠀  ⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠛⢻⣿⣿⡿⠿⣿⣿⡏⠉⠻⢿⣿⣷⠀⠀⠀⠀⠀⠄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⡛⠁⠀⠀⠻⣿⣿⣶⣿⣿⠁⠀⢀⣴⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⣤⣀⣀⣀⡉⠉⠉⣀⣠⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢀⣤⠞⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⡿⠛⠉⠉⠙⠿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⠁⠀⠀⠀
⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠜⠁⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣦⣶⣶⣶⣾⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡿⠟⠉⠉⠠⣿⣍⣽⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠒⠒⠿⢿⣿⡟⠁⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⡿⠋⣻⣿⣿⣿⣷⣶⣤⣤⣠⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣶⣤⣀⠀⡀⠀⠀⠈⣛⣉⣩⣶⣾⠟⠋⠁⠀⠀⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀ ⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⡿⠿⠿⣿⡿⠿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀⠀⠀⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    slow("* 'We failed...'")
    slow("* You wake up in your bed. It was all a dream...")
    slow("\n* THE END")

print("="*30)
