from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)
	#f.seek(offset, from_what)

def print_a_line(f):
	print f.readline(),

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print each line:"
#print "Let's print three lines:"

for x in current_file:
	print x

#current_line = 1
#print_a_line(current_file)

#  1
#print_a_line(current_file)

#  1
#print_a_line(current_file)

#print_a_line(current_file)

#print_a_line(current_file)

#file.read() returns the entire file

#file.seek(offset, from_what) moves the pointer <offset> amt of bytes from these positions:
#0 = beginning (default)
#1 = where pointer currently is
#2 = from the end (offset likely negative)

#file.readline() returns file from where the pointer is to a \n character (incl. \n)
#returns an empty string at end-of-file