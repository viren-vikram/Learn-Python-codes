from sys import exit 

def data_science():
	print("select one of the following options")
	print("press 'dc' for distributed computing '\n' for ml press 'm' '\n' for ai press 'a'   ")
	ds_input = raw_input(" . > ")
	if ds_input == "dc":
		return distributed_computing()
	elif ds_input == "m":
		return machine_learning()
	elif ds_input == "a":
		return ai()
	else:
		print(" please find the correct words again")
		dead("wrong choice of words!!! hahahahhahaha")
	
def distributed_computing():
	print("you are in data science folder")
	print(" to learn about apache spark press 's'")
	print("to learn about hadoop press 'h'")
	print("to learn about map reduce press 'm'")
	d_input =raw_input(" > ")
	if d_input == "s":
		print("go to apache spark file in google drive")
		exit(0)
	elif d_input == "h":
		print(" find hadoop material online as nothing available here")
	elif d_input == "m":
		print("you are here to learn about mapreduce")
	else:
		print(" wrong input nothing more to learn here ")
		dead("may this was a wrong option ")
def machine_learning():
	print(" to learn more about supervised learning press 'sl'")
	print("to learn about unsupervised learning press 'ul'")
	m_input = raw_input(" > ")
	if m_input == "sl":
		print("please read stanford supervised learning research paper")
	elif m_input == "ul":
		print(" you may want to know about clustering and segmentation ")
	else:
		print("there is no such option to learn as of now")
		dead("bad condition to search")
		
def ai():
	print("choose one of the option to use")
	print("for robotics and machine intelligence press 'mi'")
	print("for software automation and auto configure info press 'sa'")
	ai_input = raw_input(" > ")
	if ai_input == "mi":
		print(" please go through eth website to learn more or you can go to MIT csail as well")
		exit(0)
	elif ai_input =="sa":
		print("nice choice but nothing here to look for as of now, lmgt ")
	else:
		print("wrong option to choose, 403 error ")
		dead("died cause of error 403")
		
def analytics():
	print("press 'p' for predictive analytics")
	print("print 'dm' for data mining ")
	print("print 'pa' for prescriptive analytics")
	a_input = raw_input(" > ")
	if a_input == "p":
		print("to learn about sas type 'sas' \n to learn about R press 'r' \n to learn about python press 'py'")
		i_input = raw_input(" .> ")
		if i_input== "sas":
			print("good notes are available on ats.ucla")
		elif i_input == "r":
			print("best resource to learn is avilable on edx (analyticsedge )")
		elif i_input=="py":
			print("you have already found the best thing to learn from ")
			exit(0)
		else:
			print("I think you made a wrong decision")
			dead("killing program due to bad input")
	elif a_input == "dm":
		print("first you learn about database, choose one of the below")
		print("for NOsql press 'n' \n for postgres type 'ps' \n for mongodb type 'mg' ")
		if ii_input == "n":
			print("you came to right place for No sql we will provide tutorial very soon")
			exit(0)
		elif ii_input=="ps":
			print("postgres is not available as of now")
			exit(0)
		elif ii_input=="mg":
			print("mongodb !! good")
			exit(0)
	elif a_input=="pa":
		print("if you want to learn about excel and problem forming press 'e'")
		print (" for model simulation and advance topic press 'aa'")
		iii_input = raw_input(" >  ")
		if iii_input == "e":
			print(" learn from spreadsheet modeling book")
			exit(0)
		elif iii_input=="aa":
			print("start from monte carlo simulation")
		else:
			print("you are not serious about this option")
			dead("always trying to give wrong options")
	else:
		print("find out your own way as you have not selected a valid option")
		dead(" machine said you are done")
	
def start():
	print(" choose one of the following")
	print(" for data science press 'd'  '\n' for analytics press 'aa'")
	s_input = raw_input(" >.. ")
	if s_input == "d":
		return data_science()
	elif s_input == "aa":
		return analytics()
	else:
		print(" this is first warning for wrong input")
		return start()
	
def dead(why):
	print("he he he wait!!! %s" %why)
	exit(0)
	
	
start()