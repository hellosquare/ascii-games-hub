#Third Checkpoint - Ms. Christine
#lets add some places where you can track the players quality and coins - these need to be printed out during the game
#you are missing the choices for fruit cake
#add ASCII art
#add error checking for invalid answers

#IMPORT
import time
import sys

# =============================
# START OF GAME
# =============================
print("Welcome to your Dessert Shop!")

# String data
player_name = input("Enter your name, Little Chef")
shop_name = input("Name your dessert shop:")

print(f"\nwelcome to {shop_name}, Chef {player_name}! A customer is here.\n")

#VARIABLES FOR DESSERT
dessert_choice = ""
flavor_choice = ""
#add all your variables here

# Integer - Shop funds
coins = 100

#Float - Dessert quality
dessert_quality = 50.0

# Boolean - Special topping status
has_special_topping = False

# ============================
# Decision 1: Choose Cake Or Cookies (Main Branch)
print("Decision 1:What wil you make?\n")
print("1.Cake")
print("2.Cookies")
dessert_choice = input("Enter 1 or 2:")

if dessert_choice =="1":
    dessert = "Cake"
    dessert_quality += 10.0 
    print("Yay! A Cake! (Quality +10)\n")

    print("What flavor of cake?")
    print("1. Chocolate Cake")
    print("2. Strawberry Cake")
    print("3. Cheesecake Cake")
    print("4. Fruit Cake")
    flavor_choice = input("Enter 1, 2, 3, or 4:")
    
    if flavor_choice == "1":
        dessert = "Chocolate Cake"
        print("Chocolate Cake") 
        print("Yummy! Chocolate Cake!")
        
        add_chips = input("Do you want to add more chocolate chips? (yes/no):").lower()
        if add_chips == "yes":
            dessert_quality *= 1.5
            has_special_topping = True
            print("Chocolate chips added!(Quality *1.5)") #you need to make this more readable for the user
    
    elif flavor_choice == "2":
        dessert = "Strawberry Cake"
        print("Sweet! Strawberry Cake")
        
        strawberry_choice = input("Do you want strawberry jam or fresh strawberries?(type 'jam or fresh')").lower()
        if strawberry_choice == "jam":
            dessert_quality +=10.0
            has_special_topping = True
            print("Strawberry jam added!(Quality +10)")
            
        elif strawberry_choice =="fresh":
            dessert_quality += 15.0
            has_special_topping = True
            print("Fresh strawberries added!(Quality +15)")
            
        else:
            print("No strawberries added.")
    
    elif flavor_choice == "3":
        dessert = "Cheesecake"
        print("Creamy Cheesecake")
        
        cheesecake_choice = input("Do you want blueberry topping?(yes/no):").lower()
        if cheesecake_choice == "yes":
            dessert_quality += 12.0
            has_special_topping = True
            print("Blueberry topping added!(Quality +12)")

    else:
        print("Invalid choice. No special flavor selected.") #make the user try again (also you dont have choices for fruit cake yet)

    print("\nLet's buy ingredients for the cake! You have 100 coins to spend.")
    print("1.Buy good quality ingredients for 50 coins (qualiy +20)")
    print("2.Buy cheap ingredients for 20 coins (quality +5)")
    buy_choice=input("Enter 1 or 2:")
    
    if buy_choice == "1":
        coins -= 50
        dessert_quality += 20.0
        print("Good quality ingredients bought! Coins left:{coins}, Quality:{dessert_quality}") #fix this formatting please
        
    elif buy_choice == "2":
        coins -= 20
        dessert_quality += 5.0
        print("Cheap ingredients bought! Coins left:{coins},Quality:{dessert_quality}")


elif dessert_choice == "2":
    dessert = "Cookies"
    dessert_quality += 8.0
    print("Yay! Cookies! (Quality +8)")

   
    print("What flavor of cookies?")
    print("1.Chocolate Chip Cookies")
    print("2.Oatmeal Cookies")
    print("3.Suger Cookies")
    cookie_choice = input("Enter 1,2, or 3")

    if cookie_choice == "1":
        dessert = "Chocolate Chip Cookies"
        print("Classic Chocolate Chip Cookies")
        add_nuts = input("Do you want to add nuts? (yes/no):").lower()
        if add_nuts == "yes":
            dessert_quality *= 1.2
            has_special_topping = True
            print("Nuts added! (Quality *1.2)")

        elif cookie_choice =="2":
            dessert ="Oatmeal Cookies"
            print("healthy Oatmeal Cookies")
            add_raisins = input("Do you want to add raision? (yes/no):").lower()

            if add_raisins == "yes":
                dessert_quality == 10.0
                has_special_topping =True
                print("Raisins added! (Quality +10)")
