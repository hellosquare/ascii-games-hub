#final
#imports
import time

def typewriter(text, speed=0.03):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
    print()

#variables
health = 100
gameover = False

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

#EVENTONE  
while gameover == False:
    name = input("What is your name, brave knight? ")
    typewriter("Welcome, " + name + ", to the world of adventure!")

    typewriter("This is a game where characters have to choose 2 paths")
    typewriter("You are a knight that just finished the war and you are going to choose your way back")
    choiceOne = input("Which path do you choose? 1. grassland 2. foggy forest")
    if choiceOne == "1":
        typewriter("You are going in the grassland, and you see a town with good villagers")
        typewriter("The villagers will hunt you and eat you")
        health = health -10
        typewriter("You now have: " + str(health) + "health.")
        
    elif choiceOne == "2":
        typewriter("You are going in the foggy forest, and you see a cave and mountains with bats")
        typewriter("You go through it, you are safe")
        health = health + 10
        typewriter("You now have: " + str(health) + "health.")
        
    typewriter("You go into a village where you are safe there and can have a rest")
    typewriter("The next morning you continue your journey, you go into a grassland")
    
    choiceTwo = input("Which path do you choose? 1. go in the grassland 2. go around the grassland")
    
    if choiceTwo == "1":
        typewriter("You go in to the grassland and go over a hill that has a dragon sleeping on it")
        typewriter("You also see a small path")
        typewriter("You are walking and you are so close to home.") 
        typewriter("You see a small path off to the side.")
        
        choiceThree = input("Do you want to go down the path? 1. yes 2. no")
        
        if choiceThree == "1":
            typewriter("You go down the path and see a farm with a old man collecting wheats")
            typewriter("You can help him collect the wheats and get a reward")
            
            choiceFour = input("Do you want to help him? 1. yes 2. no")
            if choiceFour == "1":
                typewriter("You help him collect the wheats and he gives you a reward")
                health = health + 10
                typewriter("You now have: " + str(health) + "health.")
                
            elif choiceFour == "2":
                typewriter("You don't help him and you go back to the main path")
                typewriter("You now have: " + str(health) + "health.")

        elif choiceThree == "2":
            typewriter("You choose to keep going for the main mission to get back home")
            typewriter("You now have: " + str(health) + "health.")

        typewriter("You go by the dragon and walk a long road, then you are back to home")
        typewriter("You won, Congradulations!!!")
        health = health + 10
        typewriter("You now have: " + str(health) + "health.")
        print(dragonart)

        typewriter("You are so close to home, you walk in to your house and see your family is cooking dinner and waiting for you.")
        typewriter("You sat at the table abd have a great dinner with your family.")
        typewriter("You won the game, Congradulations!!!")
        typewriter("Thank you for playing the game, bye.")
        typewriter("The End.")
        time.sleep(5)
    
    elif choiceTwo == "2" :
        gameover = True
        typewriter("go around the grassland and the dragon will wake up and eat you")
        health = health - health
        typewriter("You now have: " + str(health) + "health.")
        print(dragonart)
        time.sleep(5)
      
        typewriter("You have been eaten by the dragon, you lost the game.")
        typewriter("Thank you for playing the game, bye.")
        typewriter("The End.")
        break
    break
