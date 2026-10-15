# CONSTANTS
SURVIVOR_COINS = 1000
SPY_COINS = 700
 
# PLAYER VARIABLES
playerName = ""
characterType = 0
choiceOne = 0
choiceTwo = 0
choiceThree = 0
choiceFour = 0
choiceFive = 0
deadCook = 0
firstClue = 0
firstEnding = 0
secondEnding = 0
 
print("Choose your character. (You have 1000 coins)")
print("Secret spy: 300 coins")
print("Survivor: 0 coins")
 
while True:
    try:
        characterType = int(input("Enter 1 = spy. Enter 2 = survivor: "))
 
        if characterType == 1:
            print("You are now a spy. You have 700 coins remaining.")
            break
 
        elif characterType == 2:
            print("You are now a survivor.")
            break
 
        else:
            print("Please enter 1 or 2")
 
    except ValueError:
        print("Please enter 1 or 2")
 
print()
 
playerName = input("What would you like to be called? ")
 
print("Welcome to the game, " + playerName + "!")
print()
 
print("-Story begins-")
print("It is a stormy afternoon in New England, 1954. You are getting ready for a dinner party held in a dark mansion. -6:00 pm.")
 
enter = input("please press enter to continue...")
 
print()
 
print("A butler, Wadsworth, greets you at the front door. Here you meet three other strangers: Mrs. Peacock, Mrs. White, and Colonel Mustard.")
 
enter = input("")
 
print("You sit down at the dining table and try to have a conversation with these people. 7:02 pm.")
 
enter = input("")
 
print("You notice that Mrs. White, an intimidating looking woman is staring at you.")
print("Mrs. White: Hi " + playerName + " what is your occupation? press enter to continue...")
 
enter = input("")
 
input("As you were about to answer, you were interrupted by a knock on the door. A stranger drenched in rain asks for a place to stay. Do you agree to let him in? Press enter...")
 
while True:
 
    try:
 
        choiceOne = int(input("Enter 1 = yes. Enter 2 = no: "))
 
        if choiceOne == 1:
            print("The stranger is grateful for your kindness and help. He stays at the mansion.")
            break
 
        elif choiceOne == 2:
            print("The stranger leaves disappointed.")
            break
 
        else:
            print("Please enter 1 or 2")
 
    except ValueError:
        print("Please enter 1 or 2")
 
print()
 
enter = input("")
 
print("The maid sets dinner onto the dining table. As you were enjoying your meal, you listened to the conversation of everyone around you. 7:35 pm.")
 
print()
 
print("Mrs. Peacock: Oh my, this soup's delicious isn't it?")
 
enter = input("")
 
print("Colonel Mustard: What kind of soup is it?")
 
enter = input("")
 
print("Mrs. Peacock: It is shark's fin soup, it is my favorite, however it's exceptionally rare.")
 
enter = input("")
 
print("Colonel Mustard: What a coincidence.")
 
print()
 
enter = input("")
 
print("After dinner, Wadsworth, the butler, gathers everyone into the study. He reveals the real reason you have all been gathered. 8:03 pm.")
 
if choiceOne == 1:
    print("The stranger guest has been moved to a separate room.")
 
enter = input("")
 
print("Wadsworth makes sure to lock the door behind him.")
print("Wadsworth: Everyone here is all being blackmailed by the same man. I am the one who brought everyone together.")
 
enter = input("")
 
print("Wadsworth: Colonel Mustard sells stolen military truck parts on the black market. To keep his operation a secret, he used a radio dispatch to send a group of soldiers to a battle he knew they wouldn't win, resulting in their deaths.")
print("...Mrs. Peacock, a woman who takes bribes from foreign powers to buy votes for her husband, who is the Senator...")
print("Mrs. White is the prime suspect for the murder of her husband. He was a nuclear physicist who disappeared under highly suspicious circumstances.")
print(playerName + ", you have a massive gambling debt that will cause you to lose your high profile job.")
 
enter = input("")
 
print("Wadsworth brings in another man. His name is Mr. Boddy, the blackmailer behind everyone's schemes. He and all the others are in trouble for committing serious crimes.")
print("Wadsworth: I have all the evidence recorded on a tape recorder.")
 
enter = input("")
 
print("Mr. Boddy hands out a box of weapons. He has this prepared in order to have Wadsworth be killed as he turns off the lights to escape.")
 
enter = input("")
 
print("-LIGHTS OUT-")
print("You hear a commotion around you")
 
enter = input("")
 
print("-LIGHTS ON-")
print("Mr. Boddy has been stabbed with a dagger! He failed to escape.")
 
enter = input("")
 
print("Everyone is in a panic. Colonel Mustard checks Mr. Boddy's pulse, announcing that he is dead. Everyone turns to Wadsworth, demanding the key so that they could escape.")
print("Wadsworth lets them out the study. But as he reaches into his pocket, he realizes that the key to the front door is missing. 9:46 pm.")
 
while True:
 
    if characterType == 1:
 
        try:
 
            firstClue = int(input("You are a spy. Would you like to spend 300 coins to use a clue? Enter 1 = yes. Enter 2 = no. "))
 
            if firstClue == 1:
                print("The soup in the kitchen is spilled. You have 400 coins left.")
                break
 
            elif firstClue == 2:
                break
 
            else:
                print("Please enter 1 or 2")
 
        except ValueError:
            print("Please enter 1 or 2")
 
    else:
        break
 
enter = input("")
 
print("Everyone agrees to drag Mr. Boddy's body out of the study. However, they had to check on the Cook.")
 
enter = input("")
 
print("The cook is nowhere to be found.")
 
while True:
 
    try:
 
        deadCook = int(input("Do you decide to open the pantry? Enter 1 = yes. Enter 2 = no. "))
 
        if deadCook == 1:
            print("You decide to open the pantry. The Cook's body falls directly on top of you!")
            break
 
        elif deadCook == 2:
            print("You hear a loud scream. Mrs. Peacock decided to open the pantry but the Cook's body fell directly on top of her!")
            break
 
        else:
            print("Please enter 1 or 2")
 
    except ValueError:
        print("Please enter 1 or 2")
 
enter = input("")
 
print("Everyone is in a panic. Mr. Boddy's dead body is now propped up on a sofa couch. They all agree to drag the Cook's body to the study instead.")
 
while True:
 
    if choiceOne == 1:
 
        try:
 
            choiceTwo = int(input("Would you rather stay behind to check up on the stranger instead? Enter 1 = yes. Enter 2 = no. "))
 
            if choiceTwo == 1:
                print("You decide to check up on the stranger who is staying at the library. 10:45 pm.")
                break
 
            elif choiceTwo == 2:
                print("You decide to go with the Butler, Mrs. Peacock, Mrs. White and Colonel Mustard together.")
                break
 
            else:
                print("Please enter 1 or 2")
 
        except ValueError:
            print("Please enter 1 or 2")
 
    else:
        print("You decide to go with the Butler, Mrs. Peacock, Mrs. White and Colonel Mustard together.")
        break
 
while choiceOne == 1 and choiceTwo == 1:
 
    try:
 
        print("The stranger is reading a book while waiting for the long storm to end. They are surprised to see you enter the room.")
 
        choiceThree = int(input("Would you like to make up a story in order to distract him from the chaos happening around the mansion? Enter 1 = yes. Enter 2 = no. "))
 
        if choiceThree == 1:
            break
 
        elif choiceThree == 2:
            break
 
        else:
            print("Please enter 1 or 2")
 
    except ValueError:
        print("Please enter 1 or 2")
 
if choiceThree == 1 and choiceTwo == 1 and deadCook == 1:
 
    print("You attempt to be deceptive. The incident of the dead Cook falling and landing onto you made you nervous.")
 
    enter = input("")
 
    print("As you try to tell a story, the stranger could not help but notice your strange behaviour. In the end, you failed to stop them from getting out of the library.")
 
elif choiceThree == 1 and deadCook == 2:
 
    print("You attempt to be deceptive.")
 
    enter = input("")
 
    print("You are successful and made it through in telling the lies to avoid suspicions from the stranger.")
 
elif choiceThree == 2:
 
    print("You decide to keep a distance from the stranger. The stranger thanks you for your kindness in agreeing to let them stay.")
 
if choiceOne == 1 and choiceTwo == 1:
 
    if choiceThree == 1 and deadCook == 1:
 
        print("---THE STRANGER ESCAPED THE LIBRARY---")
 
        while True:
 
            try:
 
                firstEnding = int(input("15 minutes have passed and the lights are still off ... Do you decide to get out or stay in longer? Enter 1 = stay. Enter 2 = leave. "))
 
                if firstEnding == 1:
                    print("You survive.")
                    break
 
                elif firstEnding == 2:
                    print("You died!")
                    break
 
                else:
                    print("Please enter 1 or 2")
 
            except ValueError:
                print("Please enter 1 or 2")
 
    else:
 
        print("---THE STRANGER STAYED IN THE LIBRARY---")
 
while True:
 
    try:
 
        choiceFour = int(input("Do you decide to team up with Colonel Mustard or Mrs. Peacock? 1 = Colonel Mustard. 2 = Mrs. Peacock. "))
 
        if choiceFour == 1:
            print("Colonel Mustard warns you about Mrs. Peacock and Mrs. White.")
            break
 
        elif choiceFour == 2:
            print("Mrs. Peacock warns you about the butler.")
            break
 
        else:
            print("Please enter 1 or 2")
 
    except ValueError:
        print("Please enter 1 or 2")
 
print("It has been a while since everyone decided to split up into groups.")
print("You find the dead body of Mrs. White.")
 
while True:
 
    try:
 
        choiceFive = int(input("Do you blame Mrs. Peacock for the murder? 1 = Yes. 2 = No. "))
 
        if choiceFive == 1:
            print("Everyone believes you.")
            print("The cops arrive to the crime scene and arrests Mrs. Peacock.")
            break
 
        elif choiceFive == 2:
            print("Everyone becomes suspicious of you.")
            print("The cops arrive to the crime scene.")
            break
 
        else:
            print("Please enter 1 or 2")
 
    except ValueError:
        print("Please enter 1 or 2")
 
while True:
 
    try:
 
        finalEnding = int(input("Do you want to spend 500 coins to deceive the cops? 1 = Yes. 2 = No. "))
 
        if finalEnding == 1:
            print("---GOOD ENDING---")
            break
 
        elif finalEnding == 2:
            print("---BAD ENDING---")
            print("You were unsuccessful in deceiving the cops.")
            break
 
        else:
            print("Please enter 1 or 2")
 
    except ValueError:
        print("Please enter 1 or 2")
has context menu


has context menu
