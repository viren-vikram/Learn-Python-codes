from sys import argv
from os.path import exists 

script, from_file, to_file = argv

#we could do these two on one line, how ??? 

indata = open(from_file).read()
input("press return to continue , to quit press ctrl+c " )

out_file = open(to_file,'w')
out_file.write(indata)


print("älright, alright , alright")

out_file.close()


