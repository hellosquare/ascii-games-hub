#final
import random, time
print("=" * 75)
print("                              THE TOWER OF DOOM")
print("=" * 75)
print("\nLong ago, the Four Realms lived in peace, bound by an ancient balance. But that balance has been shattered. A dark tower has risen, and within it dwell the most fearsome creatures ever summoned. At the top sits the Evil King, whose shadow creeps across all lands. The elders decreed: only a hero who climbs the tower and defeats every foe can restore the balance and decide the fate of the realms.\n")
print("Four heroes answered the call:")
print("  - The KNIGHT, a wall of honor and steel.")
print("  - The ARCHER, swift as the wind and sharp of eye.")
print("  - The WITCH / WIZARD, master of forbidden power.")
print("  - The ROBOT, a machine built for one purpose: victory.\n")
print("Each fights not only for the realms, but for their own personal victory. Only one path will be walked. Only one ending will be earned.\nYour legend begins now...\n")
print("=" * 75)
print()
characterName = input("What would you name your character? ")
while True:
    characterGender = input("What would you set your character's gender? (Male/Female) ").lower()
    if characterGender in ("male", "female"):
        break
    print("Please pick Male or Female.")
print("\nChoose your Job:")
print("1. Knight  (Health: 3, Damage: 2, Speed: 1)")
print("2. Archer  (Speed: 3,  Health: 2, Damage: 1)")
print("3. Witch / Wizard  (Damage: 3, Speed: 2,  Health: 1)")
print("4. Robot   (Health: 2, Damage: 2, Speed: 2)")
jobs = {"knight": (3, 2, 1), "archer": (2, 1, 3), "witch": (1, 3, 2), "wizard": (1, 3, 2), "robot": (2, 2, 2)}
while True:
    characterJob = input("What would you set your character's job? ").lower()
    if characterJob in jobs:
        p_health, p_damage, p_speed = jobs[characterJob]
        break
    print("Please pick Knight, Archer, Witch/Wizard, or Robot.")
if characterJob == "witch" and characterGender == "male":
    display_job = "Wizard"
elif characterJob == "wizard" and characterGender == "female":
    display_job = "Witch"
else:
    display_job = characterJob.capitalize()
print()
print("Hello " + ("Mr." if characterGender == "male" else "Ms.") + characterName + ". You are a " + display_job + ". Your health is LV " + str(p_health) + ". Your damage is LV " + str(p_damage) + ". Your speed is LV " + str(p_speed) + ".")
player_level = 1
cleared_arenas = []
def show_stats():
    print("\n" + "-"*40)
    print("       PLAYER STATUS")
    print("-"*40)
    print(f"Name:       {characterName}")
    print(f"Job:        {display_job}")
    print(f"Level:      {player_level}")
    print(f"Health:     {p_health}")
    print(f"Damage:     {p_damage}")
    print(f"Speed:      {p_speed}")
    print(f"Base Total: {(p_health + p_damage + p_speed) / 3:.1f}")
    print("-"*40)
def math_challenge():
    global p_health, p_speed, p_damage, player_level
    print("\n" + "="*40)
    print("       MATH CHALLENGE: UPGRADE LEVEL")
    print("="*40)
    print("Answer 5 math questions correctly to level up!")
    print("(Wrong answers will spawn new questions)")
    print("(Single digit numbers only, plus simple division)")
    correct_answers = 0
    question_number = 0
    while correct_answers < 5:
        question_number += 1
        print(f"\n--- Question {question_number} (Correct: {correct_answers}/5) ---")
        operation = random.randint(1, 4)
        if operation == 1:
            num1, num2 = random.randint(1, 9), random.randint(1, 9)
            correct_answer, symbol = num1 + num2, "+"
        elif operation == 2:
            num1, num2 = random.randint(1, 9), random.randint(1, 9)
            if num1 < num2:
                num1, num2 = num2, num1
            correct_answer, symbol = num1 - num2, "-"
        elif operation == 3:
            num1, num2 = random.randint(1, 9), random.randint(1, 9)
            correct_answer, symbol = num1 * num2, "×"
        else:
            num2 = random.randint(2, 9)
            num1 = num2 * random.randint(1, 12)
            correct_answer, symbol = num1 // num2, "÷"
        try:
            user_answer = int(input(f"What is {num1} {symbol} {num2}? "))
        except ValueError:
            user_answer = None
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect, try again.")
    player_level += 1
    p_health += 5
    p_damage += 5
    p_speed += 5
    print(f"\nPERFECT! You leveled up to Level {player_level}!")
    show_stats()
def pre_game_upgrade():
    print("\nYour character is too weak to enter the tower!")
    print("You must complete a Math Challenge to gain your first level.")
    input("Press Enter to begin the Math Challenge...")
    math_challenge()
    while True:
        print("\n" + "="*40)
        print("       TRAINING GROUNDS")
        print("="*40)
        print("\n1. Keep Upgrading (Math Challenge)")
        print("2. Enter the Tower")
        choice = input("Enter 1 or 2: ")
        if choice == '1':
            math_challenge()
        elif choice == '2':
            print("Heading to the Tower...")
            break
        else:
            print("Please type in 1 or 2")
def training_camp():
    while True:
        print("\n" + "="*40)
        print("       TRAINING CAMP")
        print("="*40)
        print("\n1. Continue")
        print("2. Check Stats")
        print("3. Math Challenge (Answer 5 questions to Level Up!)")
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            print("Continuing to the next battle...")
            return
        elif choice == '2':
            show_stats()
        elif choice == '3':
            math_challenge()
        else:
            print("Please type in 1, 2, or 3")
def battle(enemy_name, enemy_health, enemy_damage, enemy_speed):
    player_base = (p_health + p_damage + p_speed) / 3
    enemy_base = (enemy_health + enemy_damage + enemy_speed) / 3
    print(f"\n--- BATTLE START: {enemy_name} ---")
    print(f"Enemy Stats -> Health: {enemy_health}, Damage: {enemy_damage}, Speed: {enemy_speed}, Base Total: {enemy_base:.1f}")
    print(f"Your Stats  -> Health: {p_health}, Damage: {p_damage}, Speed: {p_speed}, Base Total: {player_base:.1f}")
    time.sleep(1)
    if player_base >= enemy_base:
        print(f"\nOutcome: WIN! You defeated the {enemy_name}!")
        return True
    print(f"\nOutcome: LOSE! The {enemy_name} was too strong.")
    return False
def sort_mobs(mobs):
    return sorted(mobs, key=lambda m: (m[1] + m[2] + m[3]) / 3)
def reward_arena_clear(arena_level):
    global p_health, p_damage, p_speed, player_level
    levels_gained = 1 if arena_level == 1 else 2
    player_level += levels_gained
    p_health += 5 * levels_gained
    p_damage += 5 * levels_gained
    p_speed += 5 * levels_gained
    print(f"\n*** ARENA {arena_level} BONUS: +{levels_gained} Level(s) ***")
    print(f"You are now Level {player_level}!")
def play_arena(arena_level):
    arenas = {
        1: [("Slime", 5, 2, 2), ("Skeleton", 10, 5, 5), ("Goblins", 15, 8, 8)],
        2: [("Zombie", 20, 10, 10), ("Barbarians", 30, 15, 15), ("Giant", 40, 20, 20)],
        3: [("Swordsmen", 30, 20, 20), ("Dark Knight", 40, 30, 30), ("Evil King", 50, 50, 50)]
    }
    print("\n" + "="*40)
    print(f"ENTERING ARENA {arena_level}")
    print("="*40)
    mobs = sort_mobs(arenas[arena_level])
    for mob in mobs:
        if not battle(*mob):
            return False
        training_camp()
    return True
def choose_arena():
    available = [(f"{i}. Arena {i}", i) for i in (1, 2, 3) if i not in cleared_arenas]
    if not available:
        return None
    while True:
        print("\nChoose your path:")
        for label, _ in available:
            print(label)
        valid = [str(n) for _, n in available]
        choice = input("Enter " + " or ".join(valid) + ": ")
        for _, n in available:
            if choice == str(n):
                return n
        print("Please type in " + " or ".join(valid))
def ending():
    print("\n" + "=" * 60)
    print("            YOUR VICTORY ENDING")
    print("=" * 60)
    if characterJob == "knight":
        print("\nThe Knight kneels atop the fallen Evil King, sword driven into the stone floor. The realms are safe. The order is restored. From this day forward, the Knight is honored as the Shield of the Realms, and their name is carved into the Hall of Heroes forever.")
    elif characterJob == "archer":
        print("\nThe Archer stands at the highest window of the tower, wind whipping through their cloak. From this height, the realms stretch endlessly below — safe, free, and watching. The Archer is hailed as the Eye of the Realms, and no shadow will ever escape their sight again.")
    elif characterJob in ("witch", "wizard"):
        print("\nThe " + display_job + " stands in silence over the Evil King, magic still crackling in the air. The forbidden power that once terrified the realms is now the very thing that saved them. The " + display_job + " is honored as the Keeper of the Balance, and their legend is whispered in every village.")
    else:
        print("\nThe Robot stands still as the Evil King falls. Systems check: complete. Mission: accomplished. But something new flickers inside — something like pride. The realms hail the Robot as the Iron Savior, the machine that proved even steel can hold a heart.")
    print("\nThe fate of the realms has been decided.")
    print("Your personal victory has been earned.")
    print("=" * 60)
def main():
    print("\nWELCOME TO THE TOWER OF DOOM")
    pre_game_upgrade()
    while True:
        arena_choice = choose_arena()
        if arena_choice is None:
            print("\n==========================================")
            print("ALL ARENAS CLEARED!")
            print("Congratulations! You conquered the Tower of Doom!")
            show_stats()
            print("==========================================")
            return
        if not play_arena(arena_choice):
            print("\n==========================================")
            print("FINAL RESULT: LOSE")
            print("GAME OVER")
            show_stats()
            print("==========================================")
            break
        cleared_arenas.append(arena_choice)
        print("\n==========================================")
        print(f"ARENA {arena_choice} CLEARED!")
        print("==========================================")
        if arena_choice == 3:
            print("\nYou have defeated the Evil King and conquered the Tower of Doom!")
            show_stats()
            ending()
            print("\n==========================================")
            print("FINAL RESULT: WIN")
            print("GAME OVER")
            print("==========================================")
            break
        reward_arena_clear(arena_choice)
        show_stats()
        while True:
            print("\n1. Enter another Arena")
            print("2. Go Upgrade (Math Challenge)")
            print("3. Quit the game")
            post_choice = input("Enter 1, 2, or 3: ")
            if post_choice == '1':
                break
            elif post_choice == '2':
                math_challenge()
            elif post_choice == '3':
                print("\nYou leave the Tower of Doom. Thanks for playing!")
                show_stats()
                return
            else:
                print("Please type in 1, 2, or 3")
if __name__ == "__main__":
    main()
