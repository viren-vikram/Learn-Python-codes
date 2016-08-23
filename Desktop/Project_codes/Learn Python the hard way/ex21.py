def add(a,b):
	print("adding %d + %d" %(a,b))
	return a+b

def subtract(a,b):
	print("subtracting %d - %d "%(a,b) )
	return a-b

def multi(a,b):
	print("multiplying following %d *%d" %(a,b))
	return a*b
	
def divide(a,b):	
	print("dividing following %d / %d" %(a,b))
	return a/b
	
print("lets do math functions")

	
	
age  = add(30,5)
height = subtract(78,4)
weight = multi(90,2)
iq    = divide(100,2)


print ("age: %d  height: %d, weight: %d, IQ : %d  " %(age,height,weight,iq))

#type items

what = add(age,subtract(height,multi(weight,divide(iq,2))))

print(" that becomes: ", what, " lets check if we can do by hand")


