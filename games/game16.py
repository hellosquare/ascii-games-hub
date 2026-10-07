#Third Checkpoint - Ms. Christine

#it would be a good idea to add your variables here like...
#energy
#punctual
#reputation
#prepared

"""A branching text adventure about Bob's school day."""

print('Your choice will impact the outcome of the game')
def choose(prompt, options):
	"""Keep asking until the player enters one of the available options."""
	while True:
		answer = input(f"{prompt} ({'/'.join(options)}) ").strip().lower()
		if answer in options:
			return answer
		print(f"Please choose: {', '.join(options)}.")


def play_game():
	print("\n=== Bob's Big School Day ===")
	print("Bob wakes up late. His first class starts in twenty minutes!")

	breakfast = choose("Does Bob eat a quick breakfast or skip it?", ["eat", "skip"])
	if breakfast == "eat":
		print("Bob grabs a banana and feels more focused.")
		energy = 2
	else:
		print("Bob rushes out hungry, hoping lunch comes soon.")
		energy = 0

	route = choose("How should Bob get to school?", ["bus", "bike"])
	if route == "bus":
		print("The bus is crowded, but Bob arrives safely.")
		punctual = True
	elif breakfast == "eat":
		print("Bob bikes quickly and reaches school before the bell.")
		punctual = True
		energy -= 1
	else:
		print("Without breakfast, Bob gets tired while biking and arrives late.")
		punctual = False

	if punctual:
		class_choice = choose(
			"In math class, does Bob help a classmate or work alone?",
			["help", "alone"],
		)
	else:
		class_choice = choose(
			"Bob arrives late. Does he apologize or quietly take his seat?",
			["apologize", "quietly"],
		)

	if class_choice in ("help", "apologize"):
		print("Bob makes a good impression on his teacher.")
		reputation = 1
	else:
		print("Bob gets through class, but misses a chance to connect.")
		reputation = 0

	if energy == 0:
		lunch = choose("At lunch, does Bob buy food or ask a friend to share?", ["buy", "share"])
		if lunch == "buy":
			print("Bob eats a warm meal and gets his energy back.")
			energy = 1
		else:
			print("A friend shares lunch, and Bob promises to return the favor.")
			reputation += 1
	else:
		lunch = choose("At lunch, does Bob join the chess club or play outside?", ["chess", "outside"])
		if lunch == "chess":
			print("Bob discovers he is surprisingly good at chess.")
			reputation += 1
		else:
			print("Bob has fun outside and feels ready for the afternoon.")

	activity = choose("After lunch, does Bob attend science club or study in the library?", ["science", "library"])
	if activity == "science":
		print("Bob builds a small water filter with his team.")
		reputation += 1
	else:
		print("Bob reviews his notes and understands a difficult lesson.")
		energy += 1

	homework = choose("Before going home, does Bob start his homework or help clean the classroom?", ["homework", "clean"])
	if homework == "homework":
		print("Bob finishes most of his homework before dinner.")
		prepared = True
	else:
		print("Bob helps clean up and earns a grateful smile from his teacher.")
		reputation += 1
		prepared = False

	afternoon = choose("On the way home, does Bob plan tomorrow or relax with music?", ["plan", "music"])
	if afternoon == "plan":
		prepared = True
		print("Bob packs his bag for tomorrow and sets an alarm.")
	else:
		print("Bob listens to music and enjoys a peaceful ride home.")

	if reputation >= 3 and prepared and punctual and energy > 0:
		event = "Winning event"
		ending = "Bob wins the school science fair with a clever project, and the whole class cheers for him."
	elif not punctual and not prepared:
		event = "Losing event 1"
		ending = "Bob misses the bus, forgets his homework, and gets sent to detention for the afternoon."
	elif energy <= 0 and not prepared:
		event = "Losing event 2"
		ending = "Bob is too exhausted to focus, falls asleep in class, and gets a failing grade on the quiz."
	elif reputation >= 2:
		event = "Winning event"
		ending = "Bob ends the day with new friends and an invitation to join the chess club."
	elif prepared and punctual and energy > 0:
		event = "Winning event"
		ending = "Bob finishes the day proud that his choices helped him stay on track."
	else:
		event = "Losing event"
		ending = "Bob has a tiring day, but learns that small choices can change everything tomorrow."

	print(f"\n{event}: {ending}")


if __name__ == "__main__":
	print("Welcome to Bob's morning!")
	play_game()
