#Second Checkpoint Teacher Check - Ms. Christine 
#thanks for reorganizing the code and having the constants, and variables, and libraries right at the top for easy visuals. Also appreciate how you've added the ASCII art already

import time

# Player Variables
player = {
    "level": 0,
    "EXP": 0,
    "reqEXP": 100,
    "HP": 100,
    "maxHP": 100,
    "damage": 20,
    "shield": 0,
    "money": 100,
    "game1": 0,
    "game2": 0,
    "quest": 0,
    "inventory": [],
    "status": []
}

# Constants
stash = 10
prot = 0.5

# Clarifying the items
items = {
  "Health Potion": {
    "usable": True,
    "heal": 50,
    "price": 25
  },
  "Stick": {
    "usable": False,
    "price": 10
  }
}

# Clarifying the traders
traders = {
    "Bob": {
        "actions": ["trade", "mission"],
        "products": ["Health Potion", "Stick"]
    }
}

# For multiple different stats of enemies easier
class Enemy:
  def __init__(self, name, level, maxHP, damage, exp, drop):
    self.name = name
    self.level = level
    self.MHP = maxHP
    self.HP = maxHP
    self.DMG = damage
    self.exp = exp
    self.drop = drop

# Stats of enemies
dummy = Enemy("Dummy", 0, 50, 0, 10, 50)
trainer = Enemy("Trainer Bot", 1, 80, 15, 50, 100)

# level + 1
def level_add1():
  global player

  player["level"] += 1
  player["reqEXP"] = int(100 + 100 * player["level"])
  player["maxHP"] = int(100 + 10 * player["level"])
  player["HP"] = player["maxHP"]
  player["damage"] = int(20 + 5 * player["level"])

  print("-----------------------------------------")

# run the tutorial
def tutorial():
  global player, prot

  dummy.HP = dummy.MHP
  player["shield"] = 0

  while True:

    if dummy.HP <= 0:
      player["EXP"] += dummy.exp
      player["money"] += dummy.drop
      print(f"earned ${dummy.drop}")
      print(f"You've won the tutorial and earned {dummy.exp} exp!")
      time.sleep(0.5)
      player["game1"] += 1
      if player["EXP"] >= player["reqEXP"]:
        player["level"] += 1
        player["EXP"] -= player["reqEXP"]
        player["reqEXP"] = int(100 + 100 * player["level"])
        player["maxHP"] = int(100 + 10 * player["level"])
        player["HP"] = player["maxHP"]
        player["damage"] = int(20 + 5 * player["level"])
        print(f"LEVEL UP! You are now level {player['level']}!")
        time.sleep(0.5)
        break
      else: 
        break

    elif player["HP"] <= 0:
      print("wasted")
      player["HP"] = player["maxHP"]
      break
    
    else:
      if player["shield"] <= 0 and "Damage Reduction" in player["status"]:
        player["status"].remove("Damage Reduction")
        
      print("-----------------------------------------")
      print("    Welcome to the tutorial/freeplay")
      print("-----------------------------------------")
      print("introduce ; Basics, offense cause damage to the opponent, defense gives you an effect that protects you for 50% from 3 enemy's attacks")
      print("""
           _______
          |       |
          |  O_O  |
          |_______|
             ||
        _____||_____
       |            |
       |            |
       |            |
       |____________|
             ||
          ___||___
         |________|
""")
      print(f"Enemy: {dummy.name}")
      print(f"HP {dummy.HP}/{dummy.MHP} - Lv. {dummy.level}")
      print()
      print("You")
      print(f"HP {player['HP']}/{player['maxHP']} - Lv. {player['level']}")
      print()
      print("Status :")
      if len(player["status"]) >= 1:
        print(player["status"])
      else:
        print("nothing")
      print("1.offense")
      print("2.defense")
      print("0.run")
      print("-----------------------------------------")

      try:
        plan = int(input())

        if plan == 1:
          print("-----------------------------------------")

          dummy.HP -= player["damage"]
          print(f"dealt {player['damage']} damage to {dummy.name}")

          if player["shield"] >= 1:
            player["HP"] -= dummy.DMG * prot
            print(f"{dummy.name} dealt {dummy.DMG * prot} damage to you")
          else:
            player["HP"] -= dummy.DMG
            print(f"{dummy.name} dealt {dummy.DMG} damage to you")

        elif plan == 2:
          if player["shield"] >= 1:
            print("already used")
            print("-----------------------------------------")
          else:
            player["status"].append("Damage Reduction")
            player["shield"] = 3

            print(f"{dummy.name} dealt {dummy.DMG * prot} damage to you")

        elif plan == 0:
          break

      except ValueError:
        print("invalid plan")

# runs the game trainer bot
def trainer_bot():
  global player, prot

  trainer.HP = trainer.MHP
  player["shield"] = 0

  while True:

    if trainer.HP <= 0:
      player["EXP"] += trainer.exp
      print(f"You've won your practice and earned {trainer.exp} exp!")
      player["money"] += trainer.drop
      print(f"earned ${trainer.drop}")
      player["game2"] += 1
      time.sleep(0.5)
      if player["EXP"] >= player["reqEXP"]:
        player["level"] += 1
        player["EXP"] -= player["reqEXP"]
        player["reqEXP"] = int(100 + 100 * player["level"])
        player["maxHP"] = int(100 + 10 * player["level"])
        player["HP"] = player["maxHP"]
        player["damage"] = int(20 + 5 * player["level"])
        print(f"LEVEL UP! You are now level {player['level']}!")
        time.sleep(0.5)
        break
      else: 
        break

    elif player["HP"] <= 0:
      print("-----------------------------------------")
      print("wasted")
      player["HP"] = player["maxHP"]
      break

    else:
      if player["shield"] <= 0 and "Damage Reduction" in player["status"]:
        player["status"].remove("Damage Reduction")

#Hi Steven, maybe you could have multiple poses for your trainer bot (different expressions) and have it loop through them so it would make the game more interesting and interactive! cool game though :)
      print("-----------------------------------------")
      print("       Welcome to the Trainer Bot")
      print("-----------------------------------------")
      print("introduce ; Enemies fights back")
      print("""  
        .---------.
       |  O     O  |
       |     ▫     |
       |  -------  |
        '---------'
           /|\\
          / | \\
         /  |  \\
           / \\
          /   \\
""")
      print(f"Enemy: {trainer.name}")
      print(f"HP {trainer.HP}/{trainer.MHP} - DMG {trainer.DMG} - Lv. {trainer.level}")
      print()
      print("You")
      print(f"HP {player['HP']}/{player['maxHP']} - Lv. {player['level']}")
      print()
      print("Status :")
      if len(player["status"]) >= 1:
        print(player["status"])
      else:
        print("nothing")
      print("1.offense")
      print("2.defense")
      print("0.run")
      print("-----------------------------------------")

      try:
        plan = int(input())

        if plan == 1:
          print("-----------------------------------------")

          trainer.HP -= player["damage"]
          print(f"dealt {player['damage']} damage to {trainer.name}")

          if player["shield"] >= 1:
            player["HP"] -= trainer.DMG * prot
            print(f"{trainer.name} dealt {trainer.DMG * prot} damage to you")
            player["shield"] -= 1
          else:
            player["HP"] -= trainer.DMG
            print(f"{trainer.name} dealt {trainer.DMG} damage to you")

        elif plan == 2:
          if player["shield"] >= 1:
            print("already used")
            print("-----------------------------------------")
          else:
            player["status"].append("Damage Reduction")
            player["shield"] = 3

            player["HP"] -= trainer.DMG * prot
            player["shield"] -= 1

            print(f"{trainer.name} dealt {trainer.DMG * prot} damage to you")

        elif plan == 0:
          break

      except ValueError:
        print("invalid plan")

# enters game selection menu
def arena():
  global player

  while True:
    print("-----------------------------------------")
    print("welcome to the arena")
    print("1.play")
    print("0.leave")
    print("-----------------------------------------")

    try:
      choice1 = int(input())

      if choice1 == 1:
        print("-----------------------------------------")
        print("1.tutorial/freeplay")
        print("2.trainer bot")
        print("0.back")
        print("-----------------------------------------")

        try:
          gamechoice = int(input())
        except ValueError:
          print("-----------------------------------------")
          print("invalid choice")
          continue

        if gamechoice == 1:
          tutorial()

        elif gamechoice == 2:
          trainer_bot()

        elif gamechoice == 0:
          continue

        else:
          print("-----------------------------------------")
          continue

      elif choice1 == 0:
        print("-----------------------------------------")
        break
      
      else:
        print("-----------------------------------------")
        print("invalid choice")

    except ValueError:
      print("-----------------------------------------")
      print("invalid choice")


def user_stats():
  global player

  print("------------------stats------------------")
  print(f"HP {player['HP']}/{player['maxHP']}")
  print(f"EXP {player['EXP']}/{player['reqEXP']}")
  print(f"Lv. {player['level']}")
  print(f"Damage {player['damage']}")
  print("-----------------------------------------")
  print("        Press Enter to continue")
  print("-----------------------------------------")

  input()

# inventory menu
def inven():
  global player

  while True:
    itemcount = 0
    totalitem = len(player["inventory"])

    print("----------------inventory----------------")

    for item in player["inventory"]:
      itemcount += 1
      print(f"{itemcount}. {item}")

    print(f"{totalitem}/{stash} inventory space used")
    print("-----------------------------------------")
    print("0.back")

    try:
      choice = int(input())

      if choice == 0:
        break

      if choice < 1 or choice > len(player["inventory"]):
            print(f"invalid choice")
            continue

      selected_item = player["inventory"][choice - 1]

      print("-----------------------------------------")
      print(selected_item)

      if items[selected_item]["usable"]:
        print()
        print("-----------------------------------------")
        print("1.use")
        print("0.back")

        try:
          action = int(input())

          if action == 1:
            if player["HP"] < player["maxHP"]:
              heal = items[selected_item]["heal"]

              oldHP = player["HP"]
              player["HP"] = min(player["HP"] + heal, player["maxHP"])
              healed = player["HP"] - oldHP

              print("-----------------------------------------")
              print(f"Healed {healed} HP")

              player["inventory"].remove(selected_item)
              time.sleep(0.5)

            else:
              print("-----------------------------------------")
              print("You are not damaged")
              time.sleep(0.5)

          elif action == 0:
            continue

          else:
            print("-----------------------------------------")
            print("invalid option")

        except ValueError:
          print("-----------------------------------------")
          print("invalid option")

      else:
        print("-----------------------------------------")
        print("item unusable")
        time.sleep(0.5)

    except ValueError:
      print("-----------------------------------------")
      print("invalid item")

# wipes
def progress_wipe():
  global player

  print("confirm/decline")
  wipeCheck = input()

  if wipeCheck.lower() == "confirm":
    player["level"] = 0
    player["reqEXP"] = int(100 + 100 * player["level"])
    player["EXP"] = 0
    player["maxHP"] = int(100 + 10 * player["level"])
    player["HP"] = player["maxHP"]
    player["damage"] = int(20 + 5 * player["level"])
    player["inventory"].clear()
    player["money"] = 100

    print("-----------------------------------------")
    print("wipe successful")

  elif wipeCheck.lower() == "decline":
    print("declined")
    print("-----------------------------------------")

  else:
    print("declined")
    print("-----------------------------------------")

# contact selection menu
def contact():
  global player

  while True:
    count = 0

    print("------------------contact----------------")

    for contact in traders:
      count += 1
      print(f"{count}. {contact}")

    print()
    print("0.back")
    print("-----------------------------------------")

    try:
      choice = int(input())

      if choice == 0:
        break

      if choice < 1 or choice > len(traders):
        print("invalid choice")
        continue

      selected_contact = list(traders.keys())[choice - 1]
 
      print("-----------------------------------------")
      print(selected_contact)

      count = 0

      for count, action in enumerate(traders[selected_contact]["actions"], 1):
        print(f"{count}. {action}")

      print()
      print("0. back")
      print("-----------------------------------------")

      try:
        action_choice = int(input())

        if action_choice < 1 or action_choice > len(traders[selected_contact]["actions"]):
          print("invalid option")
          continue

        selected_action = traders[selected_contact]["actions"][action_choice - 1]

        if selected_action == "mission":

          if player["quest"] == 1:
            print("-----------------------------------------")
            if player["game1"] == 1 and player["game2"] == 1:
              print("Congrats, you have verymuch finished all the contents this game currently has")
              player["money"] += 100000
              print(f"you've been granted $100000")
              player["quest"] += 1
            else:
              print(selected_contact)
              print("Hey there bud, I don't think you're done yet")

          elif player["quest"] == 0:

            print("-----------------------------------------")
            print(selected_contact)

            print("Welcome to the Arena, rookie! To make sure you understand how to play Arena, I'll give you some tasks to do. It should help you with the basics.")
            print()
            print("-----------------------------------------")
            print("1. accept")
            print("0. decline")

            try:
              mission_choice = int(input())

              if mission_choice == 1:
                print("-----------------------------------------")
                print(selected_contact)
                print("Great, I like your confidence! go ahead to the Arena. Play the tutorial and fight with the Trainer bot. ")
                player["quest"] += 1
                print()
                print("-----------------------------------------")
                print("        Press Enter to continue")
                print("-----------------------------------------")
                input()

              elif mission_choice == 0:
                print("-----------------------------------------")
                print("declined")

              else:
                print("invalid option")
                
            except ValueError:
              print("invalid choice")
          
          else:
            print("-----------------------------------------")
            print("no mission available")

        elif selected_action == "trade":
        
          count = 0
        
          print("-----------------------------------------")
        
          for product in traders[selected_contact]["products"]:
            count += 1
            print(f"{count}. {product} - ${items[product]['price']}")

          print()
          print("0. back")
          print("-----------------------------------------")

          try:
            product_choice = int(input())

            if product_choice == 0:
              continue

            elif product_choice < 1 or product_choice > len(traders[selected_contact]["products"]):
              print("invalid option")
              continue

            selected_product = traders[selected_contact]["products"][product_choice - 1]

            if player["money"] >= items[selected_product]['price']:

              if len(player["inventory"]) < stash:
                player["money"] -= items[selected_product]['price']
                player["inventory"].append(selected_product)

                print(f"you've spent {items[selected_product]['price']} for {selected_product}")

              else:
                print("no space")

            else:
              print("not enough cash")
              
          except ValueError:
            print("invalid option")

      except ValueError:
        print("invalid option")

    except ValueError:
      print("invalid option")
    
# main menu
def main_menu():
  global player

  while True:
    time.sleep(0.5)

    print("-----------------------------------------")
    print(f"HP {player['HP']}/{player['maxHP']} - ${player['money']} - Lv. {player['level']} - EXP {player['EXP']}/{player['reqEXP']}")
    print("Arena, a round based rpg game")
    print("-----------------------------------------")
    print("1.level up once(test use)")
    print("2.arena")
    print("3.stats")
    print("4.inventory")
    print("5.contact")
    print("6.progress wipe")
    print("0.exit")
    print("-----------------------------------------")

    try:
      print("enter choice number")
      option = int(input())

    except ValueError:
      print("-----------------------------------------")
      print("invalid option")
      print("-----------------------------------------")
      continue

    if option == 1:
      level_add1()

    elif option == 2:
      arena()

    elif option == 3:
      user_stats()

    elif option == 4:
      inven()
    elif option == 5:
      contact()
      
    elif option == 6:
      progress_wipe()

    elif option == 0:
      print("see you next time")
      break

    else:
      print("-----------------------------------------")
      print("invalid option")
      print("-----------------------------------------")

# start menu
print("-----------------------------------------")
print("Caution this is a 7+ and a mid developement game!")
print("1.enter")
print("0.leave")
print("-----------------------------------------")

try:
  start = int(input())

except ValueError:
  start = 0

if start == 1:
  main_menu()

else:
  print("see you next time")
