#This was written for Python 2.7
#This covers the interesting material from exercises 13 through 36 from http://learnpythonthehardway.org/book/ 
from sys import argv
from os.path import exists
#script, first, second, third = argv
#print "The script is called:", script
#print "Your first variable is: ", first
#print "Your Second variable is:", second
#print "Your Third variable is:", third

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def add_two(arg1, arg2):
	return arg1 + arg2

#This method of unpacking requires an exact number of arguments
script, filename = argv

print "Does the input file exist? %r" % exists(filename)

file = open(filename)

print "Here's your file %r:" % filename
myFile = file.read()
print myFile
print len(myFile)
file.close()

#pydoc can be used to look up command information
outfile = open(".\output.txt", 'w')
outfile.write("Really now?\n")
outfile.write("Lame.")
outfile.close()

print_two("One", "Two")
print_two_again("One", "TwoTwo")
answer = add_two(2, 3)
print answer

if 2 >1:
	print "And the If Clause is True"

if 1 > 2:
	print "Wrong Answer"
elif 3 > 2:
	print "Else if for Python is elif."
else:
	print "Wrong answer"

if 2 > 5:
	print "WRong Answer"
else:
	print "Right Answer"

hairs = ['blonde', 'brown', 'red']

for hair in hairs:
	print "And her hair is: %s" % hair

elements = []

for i in range (0,6):
	print "Add %d to the list." % i
	elements.append(i)

for i in elements:
	print "Element was: %d" % i

elementsTwo = range(0,6)

for i in elementsTwo:
	print "Testing: %d" % i
