#Game Mechanics
#Consists of all the if and else statements that determine if the user lost or win the round!
#Jan 18th, 2022
#Kevin Patel

#Import Functions
import random

#Function to generate a random option from the list and then take the user input of the options, then to compare them to see who wins the round
def game_mechanics(choice):

	#Computer generates a random choice from the options
	random_generator = random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])
	
	#Tie Condition#

	#If User and Computer Picks the Same Option
	if(choice.value == random_generator):
		print("YOU TIED!")
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)


	#Win Conditions#

	#Win Conditions for when User Picks Rock
	elif(choice.value == "Rock" and random_generator == "Scissors"):
		print("YOU WON!")
		print("Rock Crushes",random_generator)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Win Conditions for when User Picks Rock
	elif(choice.value == "Rock" and random_generator == "Lizard"):
		print("YOU WON!")
		print("Rock Crushes",random_generator)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)
	
	#Win Conditions for when User Picks Paper
	elif(choice.value == "Paper" and random_generator == "Spock"):
		print("YOU WON!")
		print("Paper Disproves",random_generator)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Win Conditions for when User Picks Paper
	elif(choice.value == "Paper" and random_generator == "Rock"):
		print("YOU WON!")
		print("Paper Covers",random_generator)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Win Conditions for when User Picks Scissors
	elif(choice.value == "Scissors" and random_generator == "Paper"):
		print("YOU WON!")
		print("Scissors Cuts",random_generator)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Win Conditions for when User Picks Scissors
	elif(choice.value == "Scissors" and random_generator == "Lizard"):
		print("YOU WON!")
		print("Scissors Decapitates",random_generator)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Win Conditions for when User Picks Spock
	elif(choice.value == "Spock" and random_generator == "Scissors"):
		print("YOU WON!")
		print("Spock Smashes",random_generator)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Win Conditions for when User Picks Spock
	elif(choice.value == "Spock" and random_generator == "Rock"):
		print("YOU WON!")
		print("Spock Vapourises",random_generator)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Win Conditions for when User Picks Lizard
	elif(choice.value == "Lizard" and random_generator == "Spock"):
		print("YOU WON!")
		print("Lizard Poisons",random_generator)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Win Conditions for when User Picks Lizard
	elif(choice.value == "Lizard" and random_generator == "Paper"):
		print("YOU WON!")
		print("Lizard Eats",random_generator)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)


	#Lose Condition#

	#Lose Conditions for when User Picks Rock
	elif(choice.value == "Rock" and random_generator == "Spock"):
		print("YOU LOST!")
		print("Spock Vapourises",choice.value)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Lose Conditions for when User Picks Rock
	elif(choice.value == "Rock" and random_generator == "Paper"):
		print("YOU LOST!")
		print("Paper Covers",choice.value)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Lose Conditions for when User Picks Paper
	elif(choice.value == "Paper" and random_generator == "Scissors"):
		print("YOU LOST!")
		print("Scissors Cuts",choice.value)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Lose Conditions for when User Picks Paper
	elif(choice.value == "Paper" and random_generator == "Lizard"):
		print("YOU LOST!")
		print("Lizard Eats",choice.value)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Lose Conditions for when User Picks Scissors
	elif(choice.value == "Scissors" and random_generator == "Spock"):
		print("YOU LOST!")
		print("Spock Smashes",choice.value)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Lose Conditions for when User Picks Scissors
	elif(choice.value == "Scissors" and random_generator == "Rock"):
		print("YOU LOST!")
		print("Rock Crushes",choice.value)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Lose Conditions for when User Picks Spock
	elif(choice.value == "Spock" and random_generator == "Lizard"):
		print("YOU LOST!")
		print("Lizard Poisons",choice.value)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Lose Conditions for when User Picks Spock
	elif(choice.value == "Spock" and random_generator == "Paper"):
		print("YOU LOST!")
		print("Paper Disproves",choice.value)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Lose Conditions for when User Picks Lizard
	elif(choice.value == "Lizard" and random_generator == "Rock"):
		print("YOU LOST!")
		print("Rock Crushes",choice.value)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)

	#Lose Conditions for when User Picks Lizard
	elif(choice.value == "Lizard" and random_generator == "Scissors"):
		print("YOU LOST!")
		print("Scissors Decapitates",choice.value)
		print("___________________________\n")
		print("You Choose:",choice.value,"\nComputer Choose:",random_generator)