print("lets practove everything we need to know about python as of now")
print('you\'d need to know \'bout escapes with \\ that do \n new lines and \t tabs ')

poem = """
\t the lovely world of tommorrowland
with logic so firmly established 
cant discern \n the needs of love 
nor comprehend passion from institution
and requires an explaination
\n\t\t where there is none
"""

print("-------------")
print(poem)
print("-------------")

five = 10-2+5-8
print("this should be five %s" %five)

def secret_formua(started):
	jelly_beans=started*500
	jars =jelly_beans/1000
	crates=jars/100
	return jelly_beans,jars,crates
	
start_point=1000

beans,jars,crates = secret_formua(start_point)

print("there is a starting point of %d" %start_point)
print("we have %d beans, %d jars, and %d crates " %(beans,jars,crates))
start_point=start_point/10

#we also do this way

print("we have %d beans, %d jars, and %d crates " %secret_formua(start_point))


