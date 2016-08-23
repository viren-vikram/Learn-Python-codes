from sys import argv  # from sys it imports argv module
script, filename = argv  # argv has one variable 

txt = open(filename) #txt fild will store file information in a txt variable 
print("here is your file %r" %filename)  # it just print the filename

print(txt.read())   #this line read the txt variable value & then print it

print("type the name of first file")  # second method to store the file
file_again = input(" --> ")  # second file variable which will take the file into system
txt_again = open(file_again)  # second variable which store the file text 
print(txt_again.read())  # read the text variable and then print it

 

