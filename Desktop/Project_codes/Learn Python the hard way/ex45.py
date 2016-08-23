from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
		
class Death(Scene):
	scenario =[
				"yoy=u have tried for three times which means you are dead",
				"kids are better than you",
				"lets go back to the main menu & start from scratch",
				"dont forget , practice is going to make you perfect, go back & try again",
				
				]
	def enter(self):	
		print(Death.scenario[randint(0,len(self.scenario)-1)])
		exit(1)
		

class Skates(Scene):	
	def enter(self):
		
		
		print(" your first task is to learn skateboarding, are you able to do it type 'yes' or 'no'")
		action = raw_input(" ..> ")
		if action == "yes":
			print("congratulation you are going to the next step ")
			return 'surf'
		elif action == "no":
			over_counter + 1
			print("you failed for %d th time, try again" %over_counter)
			if over_counter == 3:
				return 'death'
			else:
				print("try again")
				return 'skates'
		else:	
			print("wrong input, try to provide answer in yes and no")
			return 'skates'
			
class Surf(Scene):
	def enter(self):
		print("which palce you would liketo surf")
		print("for australia press 'a' ")
		argument = raw_input("..> ")
		
		if argument == "a":
			print(" try doing it if able to do it type yes or no")
			trya = raw_input("..> ")
			if trya =='yes':
				print("congratulation you done it again now go for the next stage")
				return 'finished'
			elif trya == 'no':
				print(" yo failed go back and learn again")
				return 'surf'
			else:
				print("wrong input")
				return 'death'
class Finished(Scene):
	def enter(self):
		print(" you won nice job")
		return 'finished'

		
class Map(object):
	scene = {
			'skates':Skates(),
			'surf': Surf(),
			'finished': Finished(),
			'death': Death(),	
			}	
	def __init__(self,start_scene):
		self.start_scene = start_scene
		
	def next_scene(self,scene_name):
		val = Map.scene.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
		
class Engine(object):
	def __init__(self,scene_map):
		self.scene_map =scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		current_scene.enter()
			
			
a_map = Map('skates')
a_game = Engine(a_map)
a_game.play()