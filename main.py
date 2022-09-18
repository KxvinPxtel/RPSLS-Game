#Rock, Paper, Scissors, Lizard, Spock Game
#Create a program that will allow the user to play “Rock, paper, scissor, lizard, spock” with the computer.
#Jan 18th, 2022
#Kevin Patel

#Import Functions
import clearconsole
import game_mechanics
import time
import guizero
from guizero import App, Box, Text, TextBox, Picture, PushButton, MenuBar, ButtonGroup, Window


#Function for when user clicks help, to display certain info out to the console
def help_info():
	clearconsole.clearconsole()
	print("HELP INFO:\n___________\n")
	print("# The image will show which of the five options will win against or lose against the other options. Or go to the ABOUT INFO tab for further clarification!\n")
	print("# Pick one of the five options below and click the button called 'Press'. The game will then randomly choose one of the five option and the winner will be shown in the console!")

#Function for when user clicks about, to display certain info out to the console
def about_info():
	clearconsole.clearconsole()
	print("ABOUT INFO:\n___________\n")
	print("# Rock, Paper, Scissors, Lizard, Spock is a game variation of the famous Rock, Paper, Scissors game!\n")
	print("# Below will be listed what wins against what:\n")
	print("Rock > Lizard\nRock > Scissors\n\nPaper > Spock\nPaper > Rock\n\nScissors > Lizard\nScissors > Paper\n\nSpock > Scissors\nSpock > Rock\n\nLizard > Spock\nLizard > Paper")

#When Button is Pressed
def button_pressed():
	global choice
	
	#Clear Console
	clearconsole.clearconsole()

	#Call the Function to determine who wins the round
	game_mechanics.game_mechanics(choice)


#When "Click To Begin" button is pressed, it prints game is loading to the console for a certain period of time, then  loads the game by switching windows
def open_window():
	
	#Set X to 0
	x = 0

	#While x is equal to 0, print that the game is loading, then when x is equal to 1, switch the screen to the actual game.
	while(x==0):
		
		#Statements to load up the game
		time.sleep(0.6)
		print("\nGame is Loading.")
		time.sleep(0.6)
		clearconsole.clearconsole()
		print("\nGame is Loading..")
		time.sleep(0.6)
		clearconsole.clearconsole()
		print("\nGame is Loading...")
		time.sleep(0.6)
		clearconsole.clearconsole()
		print("\nGame is Loading.")
		time.sleep(0.6)
		clearconsole.clearconsole()
		print("\nGame is Loading..")
		time.sleep(0.6)
		clearconsole.clearconsole()
		print("\nGame is Loading...")
		time.sleep(0.6)
		clearconsole.clearconsole()
		x = 1
	
	#Switch screen to the actual game
	app.hide()
	main.show()


#Main Program

#Slash Screen
app = App(title = 'Game Launcher', height = 300, width = 511)
button1 = PushButton(app,open_window, text="Click To Begin", align = "bottom", height= 2, width = 16)

#Content Box to Put the Slash Screen images into
content_box_2=Box(app,align='top',height="fill", width= "fill",border=True)

#Put the Rock Image into the Content Box in the Slash Screen
picture2=Picture(content_box_2,image='rock.png', align = "left")
picture2.height=100
picture2.width=100

#Put the Paper Image into the Content Box in the Slash Screen
picture3=Picture(content_box_2,image='paper.png', align = "left")
picture3.height=100
picture3.width=100

#Put the Scissors Image into the Content Box in the Slash Screen
picture4=Picture(content_box_2,image='scissors.png', align = "left")
picture4.height=100
picture4.width=100

#Put the Spock Image into the Content Box in the Slash Screen
picture5=Picture(content_box_2,image='spock.png', align = "left")
picture5.height=100
picture5.width=100

#Put the Lizard Image into the Content Box in the Slash Screen
picture6=Picture(content_box_2,image='lizard.png',align = "left")
picture6.height=100
picture6.width=100


#Main GUI for Main Game
main = Window(app,title = "Rock, Paper, Scissors, Lizard, Spock Game", height = 500, width = 500)
main.hide()

#Button Box for Main Game
button_box = Box(main, width = "fill", align = "bottom", border = True)
Text(button_box, text = "Choose One From Above")
roll = PushButton(button_box, text ="Press", align ="bottom", command = button_pressed)

#Content Box with Main Image
content_box=Box(main,align='top',height='fill', width= "fill",border=True)
Text(content_box)

#Put the RPSLS Image into the Content Box in the Main Screen
picture1=Picture(content_box,image='rpslspic.png')
picture1.height=265
picture1.width=440


#Create the Radio Buttons for Game
choice = ButtonGroup(main, options=["Rock", "Paper","Scissors", "Lizard", "Spock"], align="bottom")

#Create Menu Bar for About and Help Form to output info into the console 
menubar = MenuBar(main, toplevel = ["INFO"], 
options = [
	[[ "About", about_info], ["Help", help_info]]
	])

#Set colours to the App to make it Visually Appealing
app.bg = "Light Blue"
main.bg = "Light Blue"
menubar.bg = "White"
button1.bg = "White"
roll.bg = "White"


#Display the App
app.display()