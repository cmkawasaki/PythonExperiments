#This was written for Python 2.7
#Covers interest parts of exercises 1-12 from http://learnpythonthehardway.org/book/
print "Hello World!"

print "2 + 2", 2+2
print "2 - 2", 2-2
print "2 * 2", 2*2
print "2/2", 2/2
print "Is 2 < 3?", 2 < 3
print "Is 2 > 3?", 2 > 3
print " 3 % 2", 3 % 2
print " 5 / 2", 5 / 2
print " 5.0 / 2", 5.0/ 2

cars = 100

print "Number of Cars divided by 4:", cars / 4

char_name = "Shizuka"
char_age = 21
char_height = 74 #inches
char_weight = 180 #lbs
char_eyes = 'Brown'
char_hair = 'Black'

# %s is a string formatter
print "Let's talk about %s." % char_name
print "She's got %s eyes and %s hair." % (char_eyes, char_hair)
print "If I add %d, %d, and %d, I get %d." % (char_age, char_height, char_weight, char_age + char_height + char_weight)

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print x
print y

# %r puts quotes around my string
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
print w + "\n" + e
multi_string = """
NewLine 1
\tNew Line 2
New Line 3"""
print multi_string

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?"
weight = raw_input()
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
