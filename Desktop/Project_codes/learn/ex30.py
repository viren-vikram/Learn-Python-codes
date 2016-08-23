print("you enter a dark room with two doors which door you will prefer to take")

door = raw_input(" > " )

if door=="1":
	print(" there is a bear eating a cake . what do you do?")
	print("1. take the cake")
	print("2. scream at the bear")
	
	bear = raw_input("_> ")

	if bear=="1":
		print("bear eats your face")
	elif bear =="2":
		print("bear eats your legs")
	else:
		print ("well done you saved yourself by pressing %d" %bear)

elif door=="2":
	print("when you are high on acid you need one of the following")
	print("1. blueberries")
	print("2. yellow jacket")
	print("understanding revolver yelling melodies")
	insanity = raw_input("_> ")
	if insanity =="1" or insanity =="2":
		print("your body usurviveds the power by mind of jello ")
	else:
		print("insanity took you down my boy")
else: 
	print("you stumble upon and drop on a knife and die")
		
