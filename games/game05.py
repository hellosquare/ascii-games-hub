#IMPORTS----------------
import time
import random
 
 
# ==========================================
# TYPEWRITER
# ==========================================
 
def typewriter(text, delay=0.02):
    for letter in str(text):
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()

#CONSTANTS---------------


#VARIABLES--------------
#make sure you declare your values here at the start
 
# ==========================================
# INTRO
# ==========================================
 
typewriter("================================")
typewriter("        SHADOW HERO")
typewriter("================================")
typewriter("")
typewriter("The kingdom is in danger!")
typewriter("Three monsters have taken over.")
typewriter("")
<<<<<<< HEAD
typewriter("You must defeat them and save")
typewriter("the kingdom.")
=======
typewriter("Only one hero can stop them.")
typewriter("That hero is YOU.")
typewriter("")

print(r"""zeeeeee-
        z$$$$$$$
        d$$$$$P
       d$$$$$P
      $$$$$$
    .$$$$$$
   .$$$$$$
  4$$$$$$$$$$$$$
 z$$$$$$$$$$$$$
"""""""3$$$$$
       z$$$$P
      d$$$$"
    .$$$$$"
   z$$$$$"
  z$$$$P
 d$$$$$$$$$$"
 *******$$$"
      .$$$"
     .$$"
    4$P"
   z$"
  zP
 z"
""")
 
input("Press ENTER to begin your journey...")
 
typewriter("")
typewriter("Before your adventure begins, you must choose who you are.")
>>>>>>> 64138869a02cc0b30f38218663128f183a7ae073
typewriter("")
 
input("Press ENTER to start...")
 
 
# ==========================================
# CHOOSE CHARACTER
# ==========================================
 
typewriter("")
typewriter("Choose your hero:")
typewriter("")
typewriter("1. Human")
typewriter("2. Wizard")
typewriter("3. Goblin")
typewriter("")
 
choice = input("Choose 1, 2, or 3: ")
 
if choice == "1":
    species = "Human"
elif choice == "2":
    species = "Wizard"
else:
    species = "Goblin"
 
typewriter("")
typewriter("You are a " + species + "!")
 
 
# ==========================================
# CHOOSE POWER
# ==========================================
 
typewriter("")
typewriter("Choose your power:")
typewriter("")
typewriter("1. Super Strength")
typewriter("2. Fire Magic")
typewriter("3. Super Speed")
typewriter("")
<<<<<<< HEAD
=======
typewriter("1. Super Strength  - 5 Lives") #you can make the lives as a constant
typewriter("2. Super Speed     - 4 Lives")
typewriter("3. Fire Magic      - 3 Lives")
typewriter("4. Ice Blast       - 3 Lives")
typewriter("5. Teleportation   - 3 Lives")
>>>>>>> 64138869a02cc0b30f38218663128f183a7ae073
 
choice = input("Choose 1, 2, or 3: ")
 
if choice == "1":
    power = "Super Strength"
    attack = "Punch"
    damage = 20
    special = "Power Smash"
    special_damage = 35
    lives = 5
 
elif choice == "2":
    power = "Fire Magic"
    attack = "Fireball"
    damage = 15
    special = "Fire Blast"
    special_damage = 35
    lives = 4
 
else:
    power = "Super Speed"
    attack = "Speed Strike"
    damage = 15
    special = "Lightning Rush"
    special_damage = 30
    lives = 4
 
 
# ==========================================
# CHARACTER
# ==========================================
 
typewriter("")
typewriter("Your hero:")
typewriter("Species: " + species)
typewriter("Power: " + power)
typewriter("Lives: " + str(lives))
typewriter("")
 
input("Press ENTER to begin your adventure...")
 
 
# ==========================================
# BATTLE FUNCTION
# ==========================================
 
def battle(boss, boss_hp, boss_damage):
 
    global lives
 
    player_hp = 100
    special_ready = True
 
    typewriter("")
    typewriter("================================")
    typewriter("You are fighting " + boss + "!")
    typewriter("================================")
    typewriter("")
 
    while boss_hp > 0 and lives > 0:
 
        typewriter("")
        typewriter(boss + " HP: " + str(boss_hp))
        typewriter("Your HP: " + str(player_hp))
        typewriter("Lives: " + str(lives))
        typewriter("")
        typewriter("1. " + attack)
        typewriter("2. " + special)
        typewriter("3. Heal")
        typewriter("4. Defend")
        typewriter("")
 
        choice = input("Choose your move: ")
 
        # -------------------------------
        # NORMAL ATTACK
        # -------------------------------
 
        if choice == "1":
 
            typewriter("")
            typewriter("You use " + attack + "!")
 
            hit = random.randint(1, 10)
 
            if hit == 1:
                typewriter("You missed!")
 
            else:
                boss_hp -= damage
 
                if boss_hp < 0:
                    boss_hp = 0
 
                typewriter("You dealt " + str(damage) + " damage!")
 
        # -------------------------------
        # SPECIAL ATTACK
        # -------------------------------
 
        elif choice == "2":
 
            if special_ready:
 
                typewriter("")
                typewriter("You use " + special + "!")
                boss_hp -= special_damage
 
                if boss_hp < 0:
                    boss_hp = 0
 
                typewriter("You dealt " +
                           str(special_damage) +
                           " damage!")
 
                special_ready = False
 
            else:
 
                typewriter("")
                typewriter("Your special attack is charging!")
                typewriter("You cannot use it yet.")
                continue
 
        # -------------------------------
        # HEAL
        # -------------------------------
 
        elif choice == "3":
 
            heal = 25
            player_hp += heal
 
            if player_hp > 100:
                player_hp = 100
 
            typewriter("")
            typewriter("You healed 25 HP!")
            typewriter("Your HP: " + str(player_hp))
 
        # -------------------------------
        # DEFEND
        # -------------------------------
 
        elif choice == "4":
 
            typewriter("")
            typewriter("You defend yourself.")
            typewriter("The next attack will do less damage.")
 
            boss_damage = boss_damage // 2
 
        else:
 
            typewriter("")
            typewriter("That is not a choice.")
            continue
 
        # -------------------------------
        # BOSS DEFEATED
        # -------------------------------
 
        if boss_hp <= 0:
 
            typewriter("")
            typewriter("================================")
            typewriter(boss + " has been defeated!")
            typewriter("================================")
            return True
 
        # -------------------------------
        # BOSS ATTACK
        # -------------------------------
 
        typewriter("")
        typewriter(boss + " attacks!")
 
        player_hp -= boss_damage
 
        if player_hp < 0:
            player_hp = 0
 
        typewriter("You lost " +
                   str(boss_damage) +
                   " HP.")
 
        # -------------------------------
        # LOSE LIFE
        # -------------------------------
 
        if player_hp <= 0:
 
            lives -= 1
 
            typewriter("")
            typewriter("You were defeated!")
            typewriter("You lost a life.")
            typewriter("Lives left: " + str(lives))
 
            if lives > 0:
 
                typewriter("")
                typewriter("You get back up!")
                typewriter("Your HP is restored.")
 
                player_hp = 100
                special_ready = True
 
            else:
 
                typewriter("")
                typewriter("You have no lives left.")
                return False
 
        # -------------------------------
        # RECHARGE SPECIAL
        # -------------------------------
 
        special_ready = True
 
    return False
 
 
# ==========================================
# BOSS 1
# ==========================================
 
typewriter("")
typewriter("================================")
typewriter("          LEVEL 1")
typewriter("================================")
typewriter("")
typewriter("You enter a dark cave.")
typewriter("")
typewriter("A huge Stone Golem appears!")
typewriter("")
typewriter("Stone Golem: Leave my cave!")
typewriter("")
 
input("Press ENTER to fight...")
 
 
won = battle(
    "Stone Golem",
    80,
    8
)
 
if not won:
 
    typewriter("")
    typewriter("GAME OVER")
    exit()
 
 
# ==========================================
# REWARD
# ==========================================
 
typewriter("")
typewriter("You defeated the Stone Golem!")
typewriter("")
typewriter("You found a magic shield.")
typewriter("Your journey continues.")
typewriter("")
 
input("Press ENTER to continue...")
 
 
# ==========================================
# BOSS 2
# ==========================================
 
typewriter("")
typewriter("================================")
typewriter("          LEVEL 2")
typewriter("================================")
typewriter("")
typewriter("You enter a mysterious forest.")
typewriter("")
typewriter("Something moves behind you.")
typewriter("")
typewriter("A Shadow Beast appears!")
typewriter("")
typewriter("Shadow Beast: You cannot catch me!")
typewriter("")
 
input("Press ENTER to fight...")
 
 
won = battle(
    "Shadow Beast",
    100,
    10
)
 
if not won:
 
    typewriter("")
    typewriter("GAME OVER")
    exit()
 
 
# ==========================================
# REWARD
# ==========================================
 
typewriter("")
typewriter("The Shadow Beast disappears.")
typewriter("")
typewriter("You found a healing crystal!")
typewriter("Your HP is restored.")
typewriter("")
 
input("Press ENTER to continue...")
 
 
# ==========================================
# FINAL BOSS
# ==========================================
 
typewriter("")
typewriter("================================")
typewriter("          FINAL BATTLE")
typewriter("================================")
typewriter("")
typewriter("You arrive at a giant castle.")
typewriter("")
typewriter("The doors open.")
typewriter("")
typewriter("The Dark Lord is waiting.")
typewriter("")
typewriter("Dark Lord: You made it this far.")
typewriter("Dark Lord: But you will not defeat me!")
typewriter("")
 
input("Press ENTER to fight the final boss...")
 
 
won = battle(
    "Dark Lord",
    130,
    12
)
 
if not won:
 
    typewriter("")
    typewriter("================================")
    typewriter("           GAME OVER")
    typewriter("================================")
    typewriter("")
    typewriter("The Dark Lord wins.")
    exit()
 
 
# ==========================================
# WIN
# ==========================================
 
typewriter("")
typewriter("================================")
typewriter("             YOU WIN!")
typewriter("================================")
typewriter("")
typewriter("You defeated the Dark Lord!")
typewriter("")
typewriter("The kingdom is safe again.")
typewriter("")
typewriter("Everyone celebrates your victory.")
typewriter("")
typewriter("You are now a hero!")
typewriter("")
typewriter("Species: " + species)
typewriter("Power: " + power)
typewriter("Lives left: " + str(lives))
typewriter("")
typewriter("THE END")
 
