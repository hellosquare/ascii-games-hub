#final

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

#PIZZA CHOICES
doughchoice = ""
saucechoice = ""
toppingschoice =""
cheesechoice =""

#TACO CHOICES
tortillachoice =""
beefchoice =""
lettucechoice =""
salsachoice =""





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

    
    print("now you can choose the type of seaweed") 
    print("1= seaweed sheets / 2= expired seaweed sheets")
    secondchoice = input("Type 1 or 2:  "). strip(). lower()
    
    if secondchoice == "1":
        print("you have chosen seaweed sheets that are delicious and fresh ")
        print("congrates continue picking the ingredients for your dish")
    if  ricechoice == "1":
        print ("you have chosen rice that is delicious and fresh")
        print("congrates please continue picking the ingredients for your dish ")

    elif ricechoice == "2":
        print("you have chosen expired rice that is molddy and smelly")
        trials = trials -1
        print("you have "+ str(trials) + "tries left to get the correct ingredients for your dish ")

    print("time to choose the next ingredient:")
    elif secondchoice == "2":
        print("you have chosen expired seaweed sheets that are moldy and smelly")
        trials = trials -1
        print("you have " + str(trials) + " tries left to get the correct ingredients for your dish")
        
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


print("welcome back the cooking game") 
playername=input("Enter your name: ")
print("Welcome, chef" + playername + " let's begin!")
print("The goal of the game is to finish a dish with the correct ingredients.")
print("You will have 3 tries to get the correct number of ingredients")
print("You will have " + str(trials) + "tries to get the correct number of ingredients") #how is the game keeping track of the choices

#EVENTONE
print("Please choose the dish you want to make")
print("I am making 1. pizza or 2. tacos today ?")
choiceEventOne = input("Type 1 or 2:  "). strip(). lower()

#PIZZACHOICES
if choiceEventOne == "1" : 
    print("you are going to make pizza today - pizza - today") 
    print("now you can choose the type of pizza dough") 
    print("1= fresh dough / 2= stale dough that is expired.")
    doughchoice = input("Type 1 or 2:  "). strip(). lower()

    if choiceEventOne == "1" : 
    print("you are going to make pizza today- pizza - today") 
    print("now you can choose the type of pizza dough") 
    print("1= fresh dough / 2= stale dough that is expired.")
    doughchoice = input("Type 1 or 2:  "). strip(). lower()

    
    print("now you can choose the type of pizza sauce") 
    print("1= tomato sauce that are fresh  / 2= expired tomato sauce")
    secondchoice = input("Type 1 or 2:  "). strip(). lower()
    
    if secondchoice == "1":
        print("you have chosen tomato sauce that are fresh ")
        print("congrates continue picking the ingredients for your dish")

        
    if  doughchoice == "1":
        print ("you have chosen fresh dough")
        print("congrates please continue picking the ingredients for your dish ")

    elif doughchoice == "2":
        print("you have chosen stale dough that is expired")
        trials = trials -1
        print("you have "+ str(trials) + "tries left to get the correct ingredients for your dish ")

         
                
            print("time to choose the next ingredient - it is pizza sauce ")
            print("now you can choose the type of pizza sauce") 
            print("1= delicious fresh pizza sauce / 2= expired pizza sauce that is moldy and smelly")
            
            thirdchoice = input("Type 1 or 2:  "). strip(). lower()
                
            if thirdchoice == "1= deloicious fresh pizza sauce":
                print("you have chosen delicious fresh pizza sauce that is fresh and tasty")
                print("congrates continue picking the ingredients for your dish please continue to the next step ")
                elif thirdchoice == "2= expired pizza sauce":
                        print("you have chosen expired pizza sauce that is moldy and smelly")
                        print("you lost beacause you picked the wrong choice for pizza sauce ")
                
                        
                    print("time to choose the next ingredient - it is pizza topping ")
                    print("now you can choose the type of topping") 
                    print("1= fresh pepperoni / 2= expired pepperoni that are moldy and smelly")
                    toppingchoice = input("Type 1 or 2:  "). strip(). lower()

                if toppingchoice == "1":
                        print("you have chosen fresh pepperoni that is delicious")
                        print("congrats continue picking the ingredients for your dish")
                        
                         #what happens here after - does the player get awarded or punished for choosing good or bad - make sure you count up points here
                    elif toppingchoice == ("2"):
                        print("you have chosen way too much pepperoni that is too much!!!!")
                        print("you lost you had literally failed the dish !!")

          fourthchoice == input("type 1 or 2: "). strip(). lower()

if fourthchoice == "2=deloicious fresh Mozzarella cheese":
    print("you have chosen delicious Mozzarella cheese on the top of your pizza")
print("congrats you have finish your dish ！！its absolutely delicious")
elif fourthchoice == "2= mozzarella cheese that are improper cold storage before use":
                        print("you have chosen improper cold storage for your cheese")
                        print("you lost beacause you picked the wrong choice for your pizza ")

#TACOCHOICES
if choiceEventOne == "1" : 
    print("you are going to make mexicofood - tacos - today") 
    print("now you can choose the type of tortilla") 
    print("1= tortilla / 2= overdue tortilla that are hard a and dry a long time ago.")
    tortillachoice = input("Type 1 or 2:  "). strip(). lower()

    
    print("now you can choose the type of beef") 
    print("1= beef / 2= overcooked beef")
    secondchoice = input("Type 1 or 2:  "). strip(). lower()
    
    if secondchoice == "1":
        print("you have chosen the beef cooked at the exact temperature ")
        print("congrates continue picking the ingredients for your dish")
    if  beefchoice == "1":
        print ("you have chosen rice that is delicious and fresh")
        print("congrates please continue picking the ingredients for your dish ")

    elif beefchoice == "2":
        print("you have chosen a beef that is overcooked")
        trials = trials -1
        print("you have "+ str(trials) + "tries left to get the correct ingredients for your dish ")

    print("time to choose the next ingredient:")
    elif secondchoice == "2":
        print("you have chosen expired lettuce that are moldy and smelly")
        trials = trials -1
        print("you have " + str(trials) + " tries left to get the correct ingredients for your dish")
        
    print("time to choose the next ingredient - it is salsa")
    print("now you can choose the type of salsa you like ") 
    print("1= tasty spicy salsa / 2= expired salsa that are absolutely disgusting")
    
    thirdchoice = input("Type 1 or 2:  "). strip(). lower()
        
    if thirdchoice == "1= salsa":
        print("you have chosen fresh salsa that is fresh and tasty")
        print("congrats you have finally finished your dish. It is absolutely delicious!! ")

    elif thirdchoice == "2= expired salsa":
        print("you have chosen expired salsa that is absolutely disgusting")
        print("you have lost the whole entire game because you have picked the wrong ingredients for your dish.")





                        
                
                          




