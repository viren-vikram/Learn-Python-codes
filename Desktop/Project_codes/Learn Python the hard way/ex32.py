the_count =[1,2,3,4,5,6]
fruits = ['apple','oranges','pears','raspberry']
changes =[1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
	print("this is the count %d" %number)
	
for fruit in fruits:	
	print("a fruit of type %s" %fruit)
	
for i in changes:
	print(" i got %r" %i)
	
elements = []

for i in range(0,6):
	print("adding %d to the list" %i)
	elements.append(i)

for i in elements:
	print(" element was %d" %i)
	
