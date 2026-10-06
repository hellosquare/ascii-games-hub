#Third Checkpoint - Ms. Christine
#you should add time.sleep(5) for every portion since you have a lot of text

#imports
import time

#variables
health = 100

#ART
dragonart = r'''
                 \||/
                |  @___oo
      /\  /\   / (__,,,,|
     ) /^\) ^\/ _)
     )   /^\/   _)
     )   _ /  / _)
 /\  )/\/ ||  | )_)
<  >      |(,,) )__)
 ||      /    \)___)\
 | \____(      )___) )___
  \______(_______;;; __;;;
'''

#here you should add an introduction where the character gets to type their name and gets called by that name
name = input("What is your name, brave knight? ")
print("Welcome, " + name + ", to the world of adventure!")

#EVENTONE  
print("This is a game where characters have to choose 2 paths")
print("You are a knight that just finished the war and you are going to choose your way back")
choiceOne = input("Which path do you choose? 1. grassland 2. foggy forest")

if choiceOne == "1":
    print("You are going in the grassland, and you see a town with good villagers")
    print("The villagers will hunt you and eat you")
    health = health -10
    print("You now have: " + str(health) + "health.")
    
elif choiceOne == "2":
    print("You are going in the foggy forest, and you see a cave and mountains with bats")
    print("You go through it, you are safe")
    health = health + 10
    print("You now have: " + str(health) + "health.")

#EVENTTWO   
print("You go into a village where you are safe there and can have a rest")
print("The next morning you continue your journey, you go into a grassland")
choiceTwo = input("Which path do you choose? 1. go in the grassland 2. go around the grassland")
    
if choiceTwo == "1":
    print("You go in to the grassland and go over a hill that has a dragon sleeping on it")
    print("You go by the dragon and walk a long road, then you are back to home")
    print("You won, Congradulations!!!")
    health = health + 10
    print("You now have: " + str(health) + "health.")
    print(dragonart)
    time.sleep(5)
    

elif choiceTwo == "2" :
    print("go around the grassland and the dragon will wake up and eat you")
    health = health - health
    print("You now have: " + str(health) + "health.")
    print(dragonart)
    time.sleep(5)
      


#SECRETMISSION
while True:
    print("You are walking and you are so close to home.") 
    print("You see a small path off to the side.")
    choiceThree = input("Do you want to go down the path? 1. yes 2. no")
    if choiceThree == "1":
        print("You go down the path and see a farm with a old man collecting wheats")
        print("You can help him collect the wheats and get a reward")
        choiceFour = input("Do you want to help him? 1. yes 2. no")
        if choiceFour == "1":
            print("You help him collect the wheats and he gives you a reward")
            health = health + 10
            print("You now have: " + str(health) + "health.")
            break
        elif choiceFour == "2":
            print("You don't help him and you go back to the main path")
            print("You now have: " + str(health) + "health.")
            break

    elif choiceThree == "2":
        print("You choose to keep going for the main mission to get back home")
        print("You now have: " + str(health) + "health.")
        break

print("You are so close to home, you see your family waiting for you.")
print("You have a delicious dinner with your family. The End.")
