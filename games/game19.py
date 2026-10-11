#final
import sys
import time
import random
 
def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
 
# COLOR CODES FOR ASCII ART
RED = "\033[31m"
DARK_BLUE = "\033[34m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
GREY = "\033[90m"
LIGHT_BLUE = "\033[96m"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"
 
# ASCII ART
 
CAT_ART = r"""
       /\_/\
      ( o.o )
       > ^ <
      /     \
     /       \
    |         |
    |  _   _  |
    | | | | | |
    | | | | | |
    | |_| |_| |
    |         |
     \       /
      |     |
      |     |
     /       \
    /         \
"""
 
def show_cat_art(cat_type):
    if cat_type == "Fire Cat":
        print(RED + CAT_ART + RESET)
    elif cat_type == "Water Cat":
        print(DARK_BLUE + CAT_ART + RESET)
    elif cat_type == "Electric Cat":
        print(YELLOW + CAT_ART + RESET)
    elif cat_type == "Grass Cat":
        print(GREEN + CAT_ART + RESET)
    elif cat_type == "Rock Cat":
        print(GREY + CAT_ART + RESET)
    elif cat_type == "Ice Cat":
        print(LIGHT_BLUE + CAT_ART + RESET)
    elif cat_type == "Shadow":
        print(ORANGE + CAT_ART + RESET)
    else:
        print(CAT_ART)
 
# CAT STATS
fireCat_health = 100
fireCat_damage = 20
fireCat_SpecialAttack = 25
fireCat_Burn = 5
 
waterCat_health = 100
waterCat_damage = 15
waterCat_SpecialAttack = 30
waterCat_Heal = 10
 
grassCat_health = 100
grassCat_damage = 15
grassCat_SpecialAttack = 25
grassCat_Restore = 5
 
electricCat_health = 100
electricCat_damage = 20
electricCat_SpecialAttack = 30
electricCat_Paralyze = 5
 
rockCat_health = 100
rockCat_damage = 15
rockCat_SpecialAttack = 25
rockCat_reduceDamage = 10
 
iceCat_health = 100
iceCat_damage = 15
iceCat_SpecialAttack = 30
iceCat_freeze = 10
 
# BOSS VARIABLES (Shadow Cat)
boss_name = "Shadow Cat"
boss_health = 200 #change this to 120
boss_damage = 20
boss_SpecialAttack = 30 #change this to 20
boss_defence = 0.10
 
# TUTORIAL ENEMY VARIABLES
tutorial_enemy_health = 40
tutorial_enemy_damage = 10
tutorial_enemy_name = "Frost the Ice Cat"
 
# SETUP PHASE
type_text("LOADING ASSETS...")
type_text("LOADING CREATURES...")
type_text("LOADING STATS...")
type_text("SYSTEM READY.")
print("---------------------------------------")
type_text("WELCOME TO CAT ADVENTURE!")
print()
name = input("Enter your name: ")
print()
type_text(f"Hello {name}!")
time.sleep(1)
print("You now have the opportunity to choose your very first cat.")
time.sleep(1)
type_text("The options are: ")
print("1. Fire Cat - High attack power")
print("2. Water Cat - Balance")
print("3. Grass Cat - Defensive")
print("4. Electric Cat - Fast")
print("5. Rock Cat - Tough")
print("6. Ice Cat - Strategic")
print()
 
cat1 = input("Your choice: ").strip().lower().replace(" ", "").replace("_", "")
print()
 
cat_map = {
    "1": "fireCat", "firecat": "fireCat", "fire": "fireCat",
    "2": "waterCat", "watercat": "waterCat", "water": "waterCat",
    "3": "grassCat", "grasscat": "grassCat", "grass": "grassCat",
    "4": "electricCat", "electriccat": "electricCat", "electric": "electricCat",
    "5": "rockCat", "rockcat": "rockCat", "rock": "rockCat",
    "6": "iceCat", "icecat": "iceCat", "ice": "iceCat"
}
 
if cat1 in cat_map:
    cat1 = cat_map[cat1]
else:
    print("Invalid choice. Defaulting to Fire Cat.")
    cat1 = "fireCat"
 
cat1Name = input("Name your cat: ").strip()
if not cat1Name:
    cat1Name = "Flame"
print()
 
if cat1 == "fireCat":
    player_health = fireCat_health
    player_damage = fireCat_damage
    player_special = fireCat_SpecialAttack
    player_ability = fireCat_Burn
    player_ability_name = "Ember Burn"
    player_type = "Fire Cat"
elif cat1 == "waterCat":
    player_health = waterCat_health
    player_damage = waterCat_damage
    player_special = waterCat_SpecialAttack
    player_ability = waterCat_Heal
    player_ability_name = "Healing Rain"
    player_type = "Water Cat"
elif cat1 == "grassCat":
    player_health = grassCat_health
    player_damage = grassCat_damage
    player_special = grassCat_SpecialAttack
    player_ability = grassCat_Restore
    player_ability_name = "Leaf Restore"
    player_type = "Grass Cat"
elif cat1 == "electricCat":
    player_health = electricCat_health
    player_damage = electricCat_damage
    player_special = electricCat_SpecialAttack
    player_ability = electricCat_Paralyze
    player_ability_name = "Static Shock"
    player_type = "Electric Cat"
elif cat1 == "rockCat":
    player_health = rockCat_health
    player_damage = rockCat_damage
    player_special = rockCat_SpecialAttack
    player_ability = rockCat_reduceDamage
    player_ability_name = "Stone Shield"
    player_type = "Rock Cat"
elif cat1 == "iceCat":
    player_health = iceCat_health
    player_damage = iceCat_damage
    player_special = iceCat_SpecialAttack
    player_ability = iceCat_freeze
    player_ability_name = "Frozen Whisper"
    player_type = "Ice Cat"
 
type_text(f"Hi {name}! You have chosen {cat1Name}, the {player_type}.")
show_cat_art(player_type)
print()
 
# TUTORIAL BATTLE
print("-------------------------------------------------------")
type_text("Let's start with a tutorial battle!")
time.sleep(1)
type_text("The battle continues until the training cat's health reaches zero.")
type_text("If you win, there will be 30 coins as a reward!")
time.sleep(1)
print()
type_text("Frost the Ice Cat attacks without warning!")
type_text("A wild cat challenges you to battle!")
show_cat_art("Ice Cat")
print()
 
coins = 0
tutorial_enemy_current_health = tutorial_enemy_health
player_current_health = player_health
turn = 1
special_attack_limit = 2
special_attack_used = 0
 
while tutorial_enemy_current_health > 0 and player_current_health > 0:
    print(f"--- Turn {turn} ---")
    print(f"{cat1Name}'s Health: {player_current_health}/{player_health}")
    print(f"{tutorial_enemy_name}'s Health: {tutorial_enemy_current_health}/{tutorial_enemy_health}")
    print()
 
    print("Which power do you want to use?")
    print()
    print(f"1. Normal Attack (Damage: {player_damage})")
 
    if special_attack_used < special_attack_limit:
        remaining = special_attack_limit - special_attack_used
        print(f"2. Special Attack (Damage: {player_special}) — {remaining} use(s) left")
    else:
        print(f"2. Special Attack — OUT OF USES")
 
    print(f"3. Ability - {player_ability_name}")
    print()
 
    choice = input("Type in the name or number of the power: ").strip().lower()
    print()
 
    if choice in ["1", "normal", "normal attack", "attack"]:
        type_text(f"{cat1Name} uses Normal Attack!")
        damage_dealt = player_damage
        tutorial_enemy_current_health -= damage_dealt
        type_text(f"It deals {damage_dealt} damage!")
 
    elif choice in ["2", "special", "special attack"]:
        if special_attack_used < special_attack_limit:
            special_attack_used += 1
            type_text(f"{cat1Name} uses Special Attack!")
            damage_dealt = player_special
            tutorial_enemy_current_health -= damage_dealt
            type_text(f"It deals {damage_dealt} damage!")
            remaining = special_attack_limit - special_attack_used
            type_text(f"Special Attack uses remaining: {remaining}")
        else:
            type_text("You're out of Special Attack uses!")
            type_text("You hesitate and lose your turn.")
 
    elif choice in ["3", "ability", player_ability_name.lower()]:
        type_text(f"{cat1Name} uses {player_ability_name}!")
        if cat1 == "fireCat":
            type_text(f"Burn effect applied! Deals {player_ability} extra damage.")
            tutorial_enemy_current_health -= player_ability
        elif cat1 == "waterCat":
            type_text(f"Heals {player_ability} HP!")
            player_current_health = min(player_health, player_current_health + player_ability)
        elif cat1 == "grassCat":
            type_text(f"Restores {player_ability} HP!")
            player_current_health = min(player_health, player_current_health + player_ability)
        elif cat1 == "electricCat":
            type_text(f"Paralyze chance! Deals {player_ability} extra damage.")
            tutorial_enemy_current_health -= player_ability
        elif cat1 == "rockCat":
            type_text(f"Reduces incoming damage by {player_ability} this turn!")
        elif cat1 == "iceCat":
            type_text(f"Freeze chance! Deals {player_ability} extra damage.")
            tutorial_enemy_current_health -= player_ability
    else:
        type_text("Invalid choice! You hesitate and lose your turn.")
 
    if tutorial_enemy_current_health <= 0:
        tutorial_enemy_current_health = 0
        print()
        type_text("Frost the Ice Cat has been defeated!")
        break
 
    print()
    type_text(f"{tutorial_enemy_name} attacks!")
 
    enemy_damage = tutorial_enemy_damage
    if cat1 == "rockCat":
        enemy_damage = max(0, enemy_damage - rockCat_reduceDamage)
        if rockCat_reduceDamage > 0:
            type_text(f"Stone Shield reduces damage by {rockCat_reduceDamage}!")
 
    player_current_health -= enemy_damage
    type_text(f"{cat1Name} takes {enemy_damage} damage!")
 
    if player_current_health <= 0:
        player_current_health = 0
        print()
        type_text(f"{cat1Name} has fainted!")
        type_text("You lost the tutorial battle...")
        break
 
    turn += 1
    print()
 
if tutorial_enemy_current_health <= 0:
    print("-------------------------------------------------------")
    type_text("Congratulations! You won the tutorial battle!")
    coins += 30
    type_text(f"You earned 30 coins! Total coins: {coins}")
    type_text("These coins can be used to buy items and upgrades later.")
else:
    type_text("The tutorial battle is over. Better luck next time!")
    coins += 30
    player_current_health = player_health
 
print()
type_text("Tutorial complete!")
type_text(f"{cat1Name} is now your partner!")
print()
 
# STORE PLAYER'S TEAM
 
team = [
    {
        "name": cat1Name,
        "type": player_type,
        "hp": player_current_health if player_current_health > 0 else player_health,
        "max_hp": player_health,
        "dmg": player_damage,
        "sp_dmg": player_special,
        "ability": player_ability,
        "ability_name": player_ability_name,
        "evolved": False
    }
]
 
# SHOP FUNCTION
def shop(coins, team):
    type_text("\nWelcome to the Cat Shop!")
    time.sleep(1)
    while True:
        print()
        print("=" * 30)
        print("           CAT SHOP")
        print("=" * 30)
        print(f"Coins: {coins}")
        print("-" * 30)
        print("YOUR TEAM:")
        for cat in team:
            print(f"  {cat['name']} ({cat['type']})")
            print(f"    HP: {cat['hp']}/{cat['max_hp']}  |  Power: {cat['dmg']}  |  Sp. Dmg: {cat['sp_dmg']}")
            print()  # <--- SPACE between cats
        print("-" * 30)
        print("1. Heal All Cats - 30 coins (Fully heals all cats)")
        print("2. Cat Treat - 15 coins (Heals each cat by 15 HP)")
        print("3. Power Upgrade - 20 coins (Increases power by 5)")
        print("4. Health Upgrade - 35 coins (Increases max HP by 20)")
        print("5. Special Upgrade - 50 coins (Increases special damage by 10)")
        print("6. Evolution Stone - 100 coins (Evolves cat to next level)")
        print("0. Exit Shop")
        print("=" * 30)
        print()
 
        choice = input("What would you like to buy? ").strip()
        print()
 
        if choice == "0":
            type_text("Leaving the shop...")
            break
 
        if choice == "1":
            if coins >= 30:
                coins -= 30
                for cat in team:
                    cat["hp"] = cat["max_hp"]
                type_text("All cats fully healed!")
            else:
                type_text("Not enough coins!")
 
        elif choice == "2":
            if coins >= 15:
                coins -= 15
                for cat in team:
                    cat["hp"] = min(cat["max_hp"], cat["hp"] + 15)
                type_text("All cats healed by 15 HP!")
            else:
                type_text("Not enough coins!")
 
        elif choice in ["3", "4", "5", "6"]:
            prices = {"3": 20, "4": 35, "5": 50, "6": 100}
            cost = prices[choice]
 
            if coins < cost:
                type_text("Not enough coins!")
                continue
 
            print("Which cat?")
            for i, cat in enumerate(team):
                print(f"{i+1}. {cat['name']} ({cat['type']}) - HP: {cat['hp']}/{cat['max_hp']}")
            cat_choice = input("Choice: ").strip()
 
            if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(team):
                target = team[int(cat_choice) - 1]
                coins -= cost
 
                if choice == "3":
                    target["dmg"] += 5
                    type_text(f"{target['name']}'s Power increased by 5!")
                elif choice == "4":
                    target["max_hp"] += 20
                    target["hp"] += 20
                    type_text(f"{target['name']}'s Max HP increased by 20!")
                elif choice == "5":
                    target["sp_dmg"] += 10
                    type_text(f"{target['name']}'s Special Damage increased by 10!")
                elif choice == "6":
                    if not target["evolved"]:
                        target["max_hp"] += 20
                        target["hp"] += 20
                        target["dmg"] += 5
                        target["sp_dmg"] += 10
                        target["evolved"] = True
                        type_text(f"{target['name']} evolved! Stats increased!")
                    else:
                        type_text("This cat has already evolved!")
                        coins += cost
            else:
                type_text("Invalid choice.")
        else:
            type_text("Invalid choice.")
 
    return coins
 
# BATTLE FUNCTION (With cat selection + ASCII art)
def battle(team, enemy, is_boss=False):
    # LET PLAYER CHOOSE THEIR CAT
    if len(team) > 1:
        print()
        print("=" * 40)
        print("CHOOSE YOUR CAT FOR THIS BATTLE")
        print("=" * 40)
        for i, cat in enumerate(team):
            print(f"{i+1}. {cat['name']} ({cat['type']})")
            print(f"   HP: {cat['hp']}/{cat['max_hp']}  |  Power: {cat['dmg']}  |  Sp. Dmg: {cat['sp_dmg']}")
            print()
        print("=" * 40)
 
        while True:
            cat_choice = input("Which cat will fight? ").strip()
            if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(team):
                active_cat = team[int(cat_choice) - 1]
                break
            else:
                print("Invalid choice. Try again.")
 
        type_text(f"\n{active_cat['name']} steps forward to fight!")
        show_cat_art(active_cat['type'])
        print()
    else:
        active_cat = team[0]
        show_cat_art(active_cat['type'])
        print()
 
    print()
    print("=" * 40)
    type_text(f"{enemy['name']} challenges you to battle!")
    show_cat_art(enemy['type'])
    print("=" * 40)
    print()
 
    turn = 1
    special_attack_used = 0
    special_attack_limit = 2
    player_defending = False
 
    while enemy["hp"] > 0 and active_cat["hp"] > 0:
        print(f"--- Turn {turn} ---")
        print(f"{active_cat['name']} HP: {active_cat['hp']}/{active_cat['max_hp']}")
        print(f"{enemy['name']} HP: {enemy['hp']}/{enemy['max_hp']}")
        print()
 
        print("Which power do you want to use?")
        print(f"1. Normal Attack (Damage: {active_cat['dmg']})")
 
        if special_attack_used < special_attack_limit:
            remaining = special_attack_limit - special_attack_used
            print(f"2. Special Attack (Damage: {active_cat['sp_dmg']}) — {remaining} use(s) left")
        else:
            print("2. Special Attack — OUT OF USES")
 
        print(f"3. Ability - {active_cat['ability_name']}")
        print()
 
        choice = input("Type in the name or number of the power: ").strip().lower()
        print()
 
        player_defending = False
 
        if choice in ["1", "normal", "normal attack", "attack"]:
            type_text(f"{active_cat['name']} uses Normal Attack!")
            damage = active_cat["dmg"]
            if is_boss:
                damage = int(damage * 0.9)
                type_text("Boss defense reduces damage!")
            enemy["hp"] -= damage
            type_text(f"It deals {damage} damage!")
 
        elif choice in ["2", "special", "special attack"]:
            if special_attack_used < special_attack_limit:
                special_attack_used += 1
                type_text(f"{active_cat['name']} uses Special Attack!")
                damage = active_cat["sp_dmg"]
                if is_boss:
                    damage = int(damage * 0.9)
                    type_text("Boss defense reduces damage!")
                enemy["hp"] -= damage
                type_text(f"It deals {damage} damage!")
                remaining = special_attack_limit - special_attack_used
                type_text(f"Special Attack uses remaining: {remaining}")
            else:
                type_text("You're out of Special Attack uses!")
                type_text("You hesitate and lose your turn.")
 
        elif choice in ["3", "ability", active_cat["ability_name"].lower()]:
            type_text(f"{active_cat['name']} uses {active_cat['ability_name']}!")
 
            if active_cat["type"] == "Fire Cat":
                type_text(f"Burn effect applied! Deals {active_cat['ability']} extra damage.")
                enemy["hp"] -= active_cat["ability"]
            elif active_cat["type"] == "Water Cat":
                type_text(f"Heals {active_cat['ability']} HP!")
                active_cat["hp"] = min(active_cat["max_hp"], active_cat["hp"] + active_cat["ability"])
            elif active_cat["type"] == "Grass Cat":
                type_text(f"Restores {active_cat['ability']} HP!")
                active_cat["hp"] = min(active_cat["max_hp"], active_cat["hp"] + active_cat["ability"])
            elif active_cat["type"] == "Electric Cat":
                type_text(f"Paralyze chance! Deals {active_cat['ability']} extra damage.")
                enemy["hp"] -= active_cat["ability"]
            elif active_cat["type"] == "Rock Cat":
                type_text(f"Reduces incoming damage by {active_cat['ability']} this turn!")
                player_defending = True
            elif active_cat["type"] == "Ice Cat":
                type_text(f"Freeze chance! Deals {active_cat['ability']} extra damage.")
                enemy["hp"] -= active_cat["ability"]
        else:
            type_text("Invalid choice! You hesitate and lose your turn.")
 
        if enemy["hp"] <= 0:
            enemy["hp"] = 0
            print()
            type_text(f"{enemy['name']} has been defeated!")
            return True
 
        print()
        type_text(f"{enemy['name']} attacks!")
 
        enemy_damage = enemy["dmg"]
        if active_cat["type"] == "Rock Cat" and player_defending:
            enemy_damage = max(0, enemy_damage - rockCat_reduceDamage)
            type_text(f"Stone Shield reduces damage by {rockCat_reduceDamage}!")
 
        active_cat["hp"] -= enemy_damage
        type_text(f"{active_cat['name']} takes {enemy_damage} damage!")
 
        if active_cat["hp"] <= 0:
            active_cat["hp"] = 0
            print()
            type_text(f"{active_cat['name']} has fainted!")
            return False
 
        turn += 1
        print()
 
    return enemy["hp"] <= 0
 
# HELPER: Create a Wild Cat
def create_wild_cat(wild_type, name, hp, dmg):
    if wild_type == "fireCat":
        ability, ability_name = fireCat_Burn, "Ember Burn"
        cat_type_display = "Fire Cat"
    elif wild_type == "waterCat":
        ability, ability_name = waterCat_Heal, "Healing Rain"
        cat_type_display = "Water Cat"
    elif wild_type == "grassCat":
        ability, ability_name = grassCat_Restore, "Leaf Restore"
        cat_type_display = "Grass Cat"
    elif wild_type == "electricCat":
        ability, ability_name = electricCat_Paralyze, "Static Shock"
        cat_type_display = "Electric Cat"
    elif wild_type == "rockCat":
        ability, ability_name = rockCat_reduceDamage, "Stone Shield"
        cat_type_display = "Rock Cat"
    else:
        ability, ability_name = iceCat_freeze, "Frozen Whisper"
        cat_type_display = "Ice Cat"
 
    return {
        "name": name,
        "type": cat_type_display,
        "hp": hp,
        "max_hp": hp,
        "dmg": dmg,
        "sp_dmg": dmg + 10,
        "ability": ability,
        "ability_name": ability_name,
        "evolved": False
    }
 
wild_types = ["fireCat", "waterCat", "grassCat", "electricCat", "rockCat", "iceCat"]
 
# CATCH CAT HELPER (Lets player name it)
def catch_cat(team, wild_type, wild_hp, wild_dmg):
    if len(team) >= 6:
        type_text("Your team is full! You can't catch more cats.")
        return
 
    print()
    print("The wild cat is weakened. Do you want to catch it?")
    print("1. Yes")
    print("2. No")
    catch = input("Choice: ").strip()
 
    if catch == "1":
        new_name = input("Give your new cat a name: ").strip()
        if not new_name:
            new_name = "Wild Cat"
        new_cat = create_wild_cat(wild_type, new_name, wild_hp, wild_dmg)
        team.append(new_cat)
        type_text(f"{new_name} joined your team!")
        show_cat_art(new_cat['type'])
    else:
        type_text("You let the wild cat go.")
 
# LEVEL 2: COMMON CATS (EARLY GAME)
 
print()
print("=" * 40)
print("=" * 40)
time.sleep(1)
 
wild_type = random.choice(wild_types)
wild_name = f"Wild {wild_type.replace('Cat', '')} Cat"
wild_hp = random.randint(50, 65)
enemy = create_wild_cat(wild_type, wild_name, wild_hp, 15)
 
if battle(team, enemy):
    reward = random.randint(25, 40)
    coins += reward
    type_text(f"You earned {reward} coins! Total coins: {coins}")
    catch_cat(team, wild_type, wild_hp, 15)
else:
    type_text("You lost the battle. Your cat is still hurt!")
 
coins = shop(coins, team)
 
# LEVEL 3: UNCOMMON CATS (MID GAME)
print()
print("=" * 40)
print("=" * 40)
time.sleep(1)
 
wild_type = random.choice(wild_types)
wild_name = f"Elite {wild_type.replace('Cat', '')} Cat"
wild_hp = random.randint(60, 80)
enemy = create_wild_cat(wild_type, wild_name, wild_hp, 25)
 
if battle(team, enemy):
    reward = random.randint(35, 50)
    coins += reward
    type_text(f"You earned {reward} coins! Total coins: {coins}")
    catch_cat(team, wild_type, wild_hp, 25)
else:
    type_text("You lost the battle. Your cat is still hurt!")
 
coins = shop(coins, team)
 
# LEVEL 4: RARE CATS (LATE GAME)
print()
print("=" * 40)
print("=" * 40)
time.sleep(1)
 
wild_type = random.choice(wild_types)
wild_name = f"Legendary {wild_type.replace('Cat', '')} Cat"
wild_hp = random.randint(75, 100)
enemy = create_wild_cat(wild_type, wild_name, wild_hp, 30)
 
if battle(team, enemy):
    reward = random.randint(45, 70)
    coins += reward
    type_text(f"You earned {reward} coins! Total coins: {coins}")
    catch_cat(team, wild_type, wild_hp, 30)
else:
    type_text("You lost the battle. Your cat is still hurt!")
 
coins = shop(coins, team)
 
# FINAL BOSS BATTLE: SHADOW CAT
print()
print("=" * 40)
print("FINAL BOSS: SHADOW CAT")
print("=" * 40)
time.sleep(1)
type_text("The ground trembles as the Shadow Cat emerges...")
type_text("It is not like the others. You must defeat it to become the Cat Master!")
show_cat_art("Shadow")
print()
 
boss_defeated = False
 
while not boss_defeated:
    boss_cat = {
        "name": "Shadow Cat",
        "type": "Shadow",
        "hp": boss_health,
        "max_hp": boss_health,
        "dmg": boss_damage,
        "sp_dmg": boss_SpecialAttack,
        "ability": 0,
        "ability_name": "Shadow Strike",
        "evolved": False
    }
 
    if battle(team, boss_cat, is_boss=True):
        boss_defeated = True
        print()
        print("*" * 40)
        type_text("CONGRATULATIONS!")
        type_text("You have defeated the Shadow Cat!")
        type_text("You are now the CAT MASTER!")
        print("*" * 40)
    else:
        print()
        type_text("The Shadow Cat was too powerful.")
        type_text("You lost the battle.")
        print()
        print("What would you like to do?")
        print("1. Return to the shop and try again")
        print("2. End the game")
        choice = input("Choice: ").strip()
 
        if choice == "1":
            coins = shop(coins, team)
            print()
            type_text("You return to face the Shadow Cat once more...")
            print()
        else:
            type_text("You flee from the Shadow Cat. Game Over.")
            type_text("Better luck next time!")
            break
