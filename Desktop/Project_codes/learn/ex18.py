def print_two(*args):
	arg1,arg2 =args
	print("arg1 : %r  arg2:  %r" %(arg1,arg2))

# alternative way of typing the same function

def print_two_again(arg1,arg2):
	print("arg1 is : %r , arg2 is %r  " %(arg1,arg2))

#this just takes one argument

def print_one(arg1):
	
	print("arg1 is %r" %arg1)

def print_none():
	print("I got nothing")

print_two("viren", "vikram")
print_two_again("Zed","shaw")
print_one("singh")
print_none() 

