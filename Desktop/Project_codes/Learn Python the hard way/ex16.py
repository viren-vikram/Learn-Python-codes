from sys import argv

script, filename = argv

print("we are going to erase file %r" %filename)
print("if you want to abort the operation press ctrl + c")
print ("if you donot want to abort press enter")

input("? ")
print("opening the file")

target = open(filename, 'w')

print(" truncating the file")
target.truncate()

print (" now we are going to type three lines in this file")

line1 = input("type line 1 : " )
line2 =input("type line2: ")
line3 = input("type line 3:")

print("now we are going to write these typed line into this file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(" And closing this file now")
target.close()








