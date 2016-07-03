#import argv module
from sys import argv

#unpack argv into variables on left
script, filename = argv

#open a file and assign the file object to txt
txt = open(filename)

print "Here's your file %r:" % filename
#invokes the method of the file object, which returns a string
print txt.read()
#close the file object
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt.close()