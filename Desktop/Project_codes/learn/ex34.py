from sys import exit

def gold_room():
	print("this room is full of gold , how much did you take ?")
	
	choice =raw_input("> ")
	if "0" in choice or "1" in choice:
		howmuch =int(choice)
	else:
		print("you learnt how to type numbers")
	if howmuch < 50:
		print("nice you are not greedy")
		exit(0)
	else:
		dead("you are gredy bastard")
		
def bear_room():
		print ("There is a bear here.")
		print ("The bear has a bunch of honey.")
		print ("The fat bear is in front of another door.")
		print ("How are you going to move the bear?")
		bear_moved =False
	
		while True:
			choice =raw_input(" > ")
			if choice == "take honey":
				dead("bear give you a dick slap")
			elif choice == "taunt bear" and not bear_moved:
				print("bear has moved through the door , u can pass")
				bear_moved =True
			elif choice =="taunt bear" and bear_moved:
				dead("bear gets angry and fuck ur face")
			elif choice == "open door" and bear_moved:
				gold_room()
			else:
				print("i dont know what that means")
	
def cthulu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head")
	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
def dead(why):
	print("good job",why)
	exit(0)

def start():                                         
	print ("You are in a dark room."                 )
	print ("There is a door to your right and left." )
	print ("Which one do you take?"                  )
	
	choice =raw_input(" > ")
	if choice =="left":
		bear_room()
	elif choice== "right":
		cthulu_room()
	else:
		dead("you stumble around until you starve")
		
start()