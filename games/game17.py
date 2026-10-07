#you still need to add your art and double check your error checking

#TEST
import sys
import time

# This controls how fast the story types on the screen.
TEXT_SPEED = 0.05

# Type this instead of any math answer while testing the game.
DEBUG_PASSWORD = "Noobking1"


def slow_print(text, speed=TEXT_SPEED):
    # Prints text one letter at a time.
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def print_separator():
    # Prints a line to separate story sections.
    print("\n" + "=" * 60 + "\n")


def get_choice(max_options):
    # Keeps asking until the player enters a valid choice.
    while True:
        try:
            choice = int(input(f"\nChoose 1 to {max_options}: "))

            if 1 <= choice <= max_options:
                return choice

            print("That choice is not available.")

        except ValueError:
            print("Please type a number.")


def pause():
    # Pauses the game until the player presses Enter.
    input("\nPress Enter to continue...")


def is_correct_answer(answer, correct_answer):
    # Accepts either the real answer or the debug password.
    return answer.strip() == DEBUG_PASSWORD or answer.strip() == str(correct_answer)


class WW2AdventureGame:
    # This class contains the player information and story sections.

    def __init__(self):
        # Player name.
        self.soldier_name = ""

        # Player supplies and statistics.
        self.health = 100
        self.ammo = 30
        self.grenades = 2
        self.medkits = 1
        self.documents = 0
        self.squad_alive = 3

        # Stores choices and final game information.
        self.route = []
        self.score = 0
        self.ending_name = ""
        self.ending_text = ""

    def record_choice(self, choice):
        # Saves the player's choices for the ending.
        self.route.append(choice)

    def stats(self):
        # Displays the player's current statistics.
        print("-" * 60)
        print(f"Health: {self.health}/100")
        print(f"Ammo: {self.ammo}")
        print(f"Grenades: {self.grenades}")
        print(f"Medkits: {self.medkits}")
        print(f"Squad members: {self.squad_alive}")
        print(f"Documents: {self.documents}")
        print("-" * 60)

    def use_medkit(self):
        # Uses a medkit and restores 30 health.
        if self.medkits <= 0:
            slow_print("You do not have a medkit.")

        elif self.health == 100:
            slow_print("Your health is already full.")

        else:
            self.medkits -= 1
            self.health = min(100, self.health + 30)
            slow_print("You use a medkit and gain 30 health.")

    def take_damage(self, damage):
        # Removes health and checks if the player dies.
        self.health -= damage
        slow_print(f"You lose {damage} health.")

        if self.health <= 0:
            self.game_over("You were killed in action.")
            return True

        return False

    def ask_math(self, question, answer):
        # Repeats the question until the correct answer is entered.
        while True:
            player_answer = input(question).strip()

            if is_correct_answer(player_answer, answer):
                slow_print("Correct.")
                return

            slow_print("Not quite. Try again.")

    def start_game(self):
        # Starts the game and asks for the player's name.
        print_separator()
        print("OPERATION OVERLORD: CALL TO THE FRONT") #you can add a border here for the game start
        print_separator()

        slow_print("You are a paratrooper on a mission to stop enemy artillery.") #add ASCII of enemy artillery example (cannon or something)

        self.soldier_name = input("Enter your soldier name: ").strip().title()

        if not self.soldier_name:
            self.soldier_name = "Miller"

        slow_print(f"Welcome, Private {self.soldier_name}.")

        self.stats()
        pause()
        self.ammo_question()

    def ammo_question(self):
        # First math question.
        print_separator()
        print("ACT 1: THE AMMO CRATE") #add ASCII of ammo / bullets

        slow_print("The quartermaster needs help.")
        slow_print("You have 5 soldiers.")
        slow_print("Each soldier needs 2 ammo clips.")
        slow_print("How many clips are needed altogether?")

        # The answer is 5 x 2 = 10.
        self.ask_math("Answer: ", 10)

        self.ammo += 10
        self.documents += 1

        slow_print("You get 10 extra ammo and one mission paper.")

        pause()
        self.drop_zone()

    def drop_zone(self):
        # Gives the player the first major choice.
        print_separator()
        print("ACT 2: THE DROP ZONE")

        slow_print("You land in a field near a farmhouse.") #add ASCII of farmhouse or farm land

        if self.take_damage(10):
            return

        self.stats()

        print("1. Search a glider for supplies")
        print("2. Walk through the field")
        print("3. Use a medkit and wait")

        choice = get_choice(3)

        if choice == 1:
            self.record_choice("glider")
            self.ammo += 10
            self.grenades += 1
            slow_print("You find 10 ammo and one grenade.")

        elif choice == 2:
            self.record_choice("field")
            slow_print("You reach the village quietly.")

        else:
            self.record_choice("wait")
            self.use_medkit()
            slow_print("You wait for your squad.")

        pause()
        self.bridge()

    def bridge(self):
        # Second math question.
        print_separator()
        print("ACT 3: THE BRIDGE") #add ASCII art of bridge here

        slow_print("There are 8 enemy soldiers.")
        slow_print("3 walk away from the bridge.")
        slow_print("How many soldiers are still near the bridge?")

        # The answer is 8 - 3 = 5.
        self.ask_math("Answer: ", 5)

        self.documents += 1

        print("1. Send the squad across first")
        print("2. Cover the squad as they cross")
        print("3. Find a safe path around the bridge")

        choice = get_choice(3)

        if choice == 1:
            self.record_choice("squad_first")
            self.squad_alive -= 1
            slow_print("One squad member is separated in the fog.")

        elif choice == 2:
            self.record_choice("cover_squad")

            if self.take_damage(10):
                return

            slow_print("Your squad crosses safely.")

        else:
            self.record_choice("detour")
            slow_print("The long path is safe.")

        pause()
        self.farmhouse()

    def farmhouse(self):
        # Third math question and another choice.
        print_separator()
        print("ACT 4: THE FARMHOUSE")

        slow_print("You find a locked resistance radio box.") #add ASCII art of locked box here
        slow_print("The lock asks: 6 plus 4 equals what?")

        # The answer is 6 + 4 = 10.
        self.ask_math("Lock code: ", 10)

        self.documents += 1
        slow_print("The box opens. You find a keycard.") 

        print("1. Hide from an enemy truck")
        print("2. Ambush the truck")
        print("3. Escape through the cellar")

        choice = get_choice(3)

        if choice == 1:
            self.record_choice("hide")
            slow_print("The truck drives away.")

        elif choice == 2:
            self.record_choice("ambush")
            self.ammo -= 5
            self.documents += 1
            slow_print("You stop the truck and find a map.")

        else:
            self.record_choice("cellar")
            slow_print("You escape through a dark tunnel.")

        pause()
        self.bunker()

    def bunker(self):
        # Lets the player choose how to enter the bunker.
        print_separator()
        print("ACT 5: BUNKER C-4")

        slow_print("The enemy bunker is ahead.") 

        print("1. Throw a grenade")
        print("2. Start a firefight")
        print("3. Use the keycard to enter a side door")

        choice = get_choice(3)

        if choice == 1:
            self.record_choice("grenade")

            if self.grenades > 0:
                self.grenades -= 1
                slow_print("The grenade clears the guard room.")

            else:
                slow_print("No grenades. You must fight.")
                self.ammo -= 5

                if self.take_damage(15):
                    return

        elif choice == 2:
            self.record_choice("firefight")
            self.ammo -= 5

            if self.take_damage(10):
                return

            slow_print("You win the firefight.")

        else:
            self.record_choice("service_passage")
            slow_print("The keycard opens the side door.")

        pause()
        self.safe()

    def safe(self):
        # Uses two simple math questions.
        print_separator()
        print("ACT 6: THE SAFE") #add ASCII art of safe

        slow_print("You find a safe with important artillery plans.")

        slow_print("First question: 7 plus 2 equals what?")

        # The answer is 7 + 2 = 9.
        self.ask_math("First code: ", 9)

        slow_print("Second question: 10 minus 3 equals what?")

        # The answer is 10 - 3 = 7.
        self.ask_math("Second code: ", 7)

        self.documents += 3

        slow_print("The safe opens. You take the artillery plans.")

        pause()
        self.radio_tower()

    def radio_tower(self):
        # Final math question.
        print_separator()
        print("ACT 7: THE RADIO TOWER")

        slow_print("You must send a code to Allied ships.")
        slow_print("The radio asks: 5 times 2 equals what?")

        # The answer is 5 x 2 = 10.
        self.ask_math("Radio code: ", 10)

        slow_print("The ships receive your message.")

        pause()
        self.ending()

    def ending(self):
        # Calculates the final score.
        print_separator()

        slow_print("Allied ships destroy the enemy artillery bunker.")
        slow_print("The mission is complete.")

        # Adds health, ammo, documents, and squad members to the score.
        self.score = self.health + self.ammo
        self.score += self.documents * 20
        self.score += self.squad_alive * 20

        self.choose_ending()
        self.show_results()

    def choose_ending(self):
        # Chooses an ending based on the player's decisions.
        if "cellar" in self.route and "service_passage" in self.route:
            self.ending_name = "THE SHADOW ROUTE"
            self.ending_text = "You used hidden tunnels and entered the bunker quietly."

        elif "ambush" in self.route and "grenade" in self.route:
            self.ending_name = "THE LOUD VICTORY"
            self.ending_text = "You won with loud attacks and explosions."

        elif "cover_squad" in self.route and self.squad_alive == 3:
            self.ending_name = "THE COMMANDERS PROMISE"
            self.ending_text = "You protected every member of your squad."

        elif "squad_first" in self.route or self.squad_alive < 3:
            self.ending_name = "THE EMPTY ROLL CALL"
            self.ending_text = "The mission worked, but not everyone returned."

        elif "hide" in self.route and "wait" in self.route:
            self.ending_name = "THE SILENT SURVIVOR"
            self.ending_text = "You stayed safe and avoided danger when possible."

        elif "firefight" in self.route:
            self.ending_name = "THE RIFLEMANS END"
            self.ending_text = "You fought your way through the bunker."

        else:
            self.ending_name = "THE NORMANDY GHOST"
            self.ending_text = "You completed the mission and disappeared into the fog."

    def choose_medal(self):
        # Selects an award based on the player's performance.
        if self.score >= 250 and self.squad_alive == 3:
            return "Medal of Honor", "You were brave and kept your whole squad safe."

        elif self.score >= 200:
            return "Silver Star", "You did an excellent job on the mission."

        elif self.score >= 150:
            return "Bronze Star", "You completed the mission well."

        elif self.health < 40:
            return "Purple Heart", "You were badly hurt but kept going."

        elif self.squad_alive < 3:
            return "Letter of Regret", "The mission was successful, but a squad member did not return."

        elif "hide" in self.route and "wait" in self.route:
            return "Cowards Commendation", "You finished the mission, but avoided danger too often."

        else:
            return "Muddy Boots Certificate", "You completed the mission and got very muddy."

    def show_results(self):
        # Shows the final ending, score, and award.
        print_separator()
        print("MISSION RESULTS")

        print(f"Private {self.soldier_name}")
        print(f"Ending: {self.ending_name}")

        slow_print(self.ending_text)

        print(f"Health: {self.health}")
        print(f"Ammo: {self.ammo}")
        print(f"Documents: {self.documents}")
        print(f"Squad members left: {self.squad_alive}")
        print(f"Score: {self.score}")

        medal, message = self.choose_medal()

        print(f"Award: {medal}")
        slow_print(message)

    def game_over(self, reason):
        # Displays the game-over message.
        print_separator()
        print("GAME OVER")
        slow_print(reason)


if __name__ == "__main__":
    # Creates the game and starts it.
    game = WW2AdventureGame()
    game.start_game()
    
