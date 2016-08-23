class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
			for line in self.lyrics:
				print(line)


			
			
happy_bday = Song(["happy birthday  to you ,",
					"I dont want to get sued",
					"so lets stop there"])
					
bulls_on_parade = Song(["they will around the family ",
						"with pocket full of shell"])
						
						
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song() 	