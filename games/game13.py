#THIRD Checkpoint Teacher Check - Ms. Christine
#please add a counter to give a winning condition
#please add ASCII art
#please add error checking


#VARIABLES
playername = ""
choiceEventOne = ""

#SUSHI CHOICES
ricechoice = ""
secondchoice = ""
thirdchoice = ""
vinegarchoice = ""

#ITALIAN CHOICES
noodleschoice = ""
waterchoice = ""
saucechoice = ""
fourthchoice = ""

trials = 4


print("welcome to the cooking game") 
playername=input("Enter your name: ")
print("Welcome, chef" + playername + " let's begin!")
print("The goal of the game is to finish a dish with the correct ingredients.")
print("You will have 3 tries to get the correct number of ingredients")
print("You will have " + str(trials) + "tries to get the correct number of ingredients") #how is the game keeping track of the choices

#EVENTONE
print("Please choose the dish you want to make")
print("I am making 1. japanese food or 2. italian food today ?")
choiceEventOne = input("Type 1 or 2:  "). strip(). lower()

#SUSHICHOICES
if choiceEventOne == "1" : 
    print("you are going to make japanese food - sushi - today") 
    print("now you can choose the type of rice") 
    print("1= rice / 2= overdue rice that are expired a long time ago.")
    ricechoice = input("Type 1 or 2:  "). strip(). lower()

    if ricechoice == "1":
        print("you have chosen normal rice that is delicious and fresh")
        print("continue picking the ingredients for your dish")
        
    elif ricechoice== "2":
        print("you have chosen overdue rice that is expired a long time ago")
        print("you lost because you picked the overdue rice , it became mushy and sour !")

    print("time to choose the next ingredient:")
    print("now you can choose the type of seaweed") 
    print("1= seaweed sheets / 2= expired seaweed sheets")
    secondchoice = input("Type 1 or 2:  "). strip(). lower()
    
    if secondchoice == "1":
        print("you have chosen seaweed sheets that are delicious and fresh ")
        print("congrates continue picking the ingredients for your dish")
    
    elif secondchoice == "2":
        print("you have chosen expired seaweed sheets that are moldy and smelly")
        print("you lost beacause you picked the expired seaweed sheets , that are disgusting !")
        
    print("time to choose the next ingredient - it is salmon")
    print("now you can choose the type of salmon") 
    print("1= delicious fresh salmon / 2= expired salmon that is moldy and smelly")
    
    thirdchoice = input("Type 1 or 2:  "). strip(). lower()
        
    if thirdchoice == "1= deloicious fresh salmon":
        print("you have chosen delicious fresh salmon that is fresh and tasty")
        print("congrates continue picking the ingredients for your dish please continue to the next step ")

    elif thirdchoice == "2= expired salmon":
        print("you have chosen expired salmon that is moldy and smelly")
        print("you lost beacause you picked the wrong choice for salmon ")

        
    print("time to choose the next ingredient - it is sushi vinegar")
    print("now you can choose the type of vinegar") 
    print("1= Sushi vinegar that has the right amount of amount / 2= etooo much vinegar, that is very sour and salty")
    vinegarchoice = input("Type 1 or 2:  "). strip(). lower()
          
    if vinegarchoice == "1":
        print("you have chosen sushi vinegar that has the perfect amount")
        print("congrats you have finish your dish , its absolutely delicious and you have won !!")
        
         #what happens here after - does the player get awarded or punished for choosing good or bad - make sure you count up points here
    elif vinegarchoice == ("2"):
        print("you have chosen way too much vinegar that is very salty")
        print("you lost you had literally failed the dish !!")

#ITALIANFOODCHOICES
elif choiceEventOne == "2":
    print("you are going to make italian food today")
    print("now choose the type of pasta/noddles")
    print("noodles / 2= expired noodles that are moldy and smelly")
    noodleschoice = input("Type 1 or 2:  "). strip(). lower()

    if noodleschoice =="1":
        print("you have chosen noodles that are delicious")
        print("good job")
        
    elif noodleschoice== "2":
        print("you have chosen over heated noodles that are too raw and soft")
        print("you lost")
        
    print("time to choose the next ingredient:")
    print("now you can choose the type of water for the noodles") 
    print("1= boiled hot water for the noodles  / 2= over boiled hot water")
    waterchoice = input("Type 1 or 2:  "). strip(). lower()
    
    if waterchoice == "1":
        print("you have chosen boiled hot water that has the right amount of heat ")
        print("congrates continue picking the ingredients for your dish ")
    
    elif waterchoice == ("2"):
        print("you have chosen over boiled hot water that is way too hot ")
        print("you lost beacause you piked the wrong choice for the hot water ")
        
    print("time to choose the next ingredient:")
    print("now you can choose the type of sauce for the pasta") 
    print("1= tomato sauce that are fresh  / 2= expired tomato sauce")
    saucechoice = input("Type 1 or 2:  "). strip(). lower()
    
    if saucechoice == "1":
        print("you have chosen tomato sauce that are fresh ")
    
    elif saucechoice == "2":
        print("you have chosen expired tomato sauce that is moldy ")
        
        print("time to choose the next ingredient:")
        print("now you can choose the type of sauce for the pasta") 
        print("1= tomato sauce that are fresh  / 2= expired tomato sauce")

    print("time to choose the next ingredient:")
    print("now you can choose the type of cheese for the pasta") 
    print("1= cheese that is delicious  / 2= expired cheese")
    fourthchoice = input("Type 1 or 2:  "). strip(). lower()

    if fourthchoice == "1":
        print("you have chosen cheese that is delicious ")
        print("congrates you have finally finish your dish")
        
    elif fourthchoice == "2":
        print("you have chosen expired cheese that is expired ")
        print("you had totally failed your dish ")
