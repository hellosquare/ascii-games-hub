import time
import sys

def typewriter(text, speed=0.01):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
    print()

health = 100
gameover = False

dragonart = r'''
                 \|/|
                |  @___oo
      /\  /\  / (__,,,,|
     ) /^\) ^\/ _)
     )   ^\/   _)
     )   _ /  / _)
 /\ )/\/ ||  | )_)
<  >      |(,,) )__)
 ||      /    \)___)\
 | \___(      )___) )___
  \_____(_______;;; __;;;
'''

while not gameover:

    name = input("What is your name, brave knight? ")
    typewriter("Welcome, " + name + ", to the world of adventure!")

    typewriter("This is a game where characters have to choose 2 paths.")
    typewriter("You are a knight that just finished the war and you are going to choose your way back.")

    choiceOne = input("Which path do you choose? 1. grassland  2. foggy forest: ")

    if choiceOne == "1":
        typewriter("You are going in the grassland, and you see a town with good villagers.")
        typewriter("The villagers will hunt you and eat you.")
        health -= 10
        typewriter("You now have: " + str(health) + " health.")

    elif choiceOne == "2":
        typewriter("You are going in the foggy forest, and you see a cave and mountains with bats.")
        typewriter("You go through it, you are safe.")
        health += 10
        typewriter("You now have: " + str(health) + " health.")

    typewriter("You go into a village where you are safe and can rest.")
    typewriter("The next morning you continue your journey and enter a grassland.")

    choiceTwo = input(
        "Which path do you choose? 1. go in the grassland  2. go around the grassland: "
    )

    if choiceTwo == "1":

        typewriter("You go into the grassland and over a hill with a sleeping dragon.")
        typewriter("You also see a small path.")
        typewriter("You are walking and are very close to home.")

        choiceThree = input("Do you want to go down the path? 1. yes  2. no: ")

        if choiceThree == "1":

            typewriter("You go down the path and see a farm with an old man collecting wheat.")
            typewriter("You can help him collect the wheat and get a reward.")

            choiceFour = input("Do you want to help him? 1. yes  2. no: ")

            if choiceFour == "1":
                typewriter("You help him collect the wheat and he gives you a reward.")
                health += 10
                typewriter("You now have: " + str(health) + "health.")
