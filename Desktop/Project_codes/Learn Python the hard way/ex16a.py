from sys import argv

script, filename =argv

fileopen = open(filename,'r+')
print("currently this file has below text \n")

print(fileopen.read())

print("do you want to append \n if no then press ctrl c ")

input("? ")

fileopen.truncate()
print(" ready to type few line to add")

line1 = input("type your first line ")
line2 = input("add more line ")
line3 = input(" pick your last line " )

fileopen.write(line1 +"\n"+ line2+"\n"+line3+ "\n")



#close the file

fileopen.close()






