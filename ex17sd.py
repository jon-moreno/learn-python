# The purpose of this script is to copy one file into another
# The filenames are given as parameters before the program starts

from sys import argv
# the exists module defines the exists function
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# in_file = open(from_file)
# indata = in_file.read()
#
# we could do these two on one line, how?
# indata = open(from_file).read()

in_file, out_file = open(from_file), open(to_file, 'w')
out_file.write(in_file.read())

#in_file, out_file = open(from_file).read(), open(to_file, 'w')
#out_file.write(in_file)


# the exists function takes the parameter of a file and returns a boolean
# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
#open(from_file).read() automatically closes the file