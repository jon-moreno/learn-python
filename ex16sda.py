#import module
from sys import argv

#unpack argv
script, filename = argv

print "Opening the file..."
target = open(filename)

print target.read()
target.close()