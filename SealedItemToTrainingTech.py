#This was written for Python 2.7
from sys import argv
from os.path import exists
from SealedItem import *
import re # Regular Expression Handler
script, inputFileName = argv

if exists(inputFileName) == False:
	print "File does not exist. Exitting."
	exit(10)

inputFile = open(inputFileName)

listOfSealedItemBlocks = []

line = inputFile.readline()
technique = ""
while line != "":
	#If line returned is just a newline character, then that is the end of the technique.
	blankStringPattern = re.compile(r'\s*\n')
	if blankStringPattern.match(line):
		#Handle by taking the previous lines of text if any and making a technique
		if technique != "":
			listOfSealedItemBlocks.append(technique)
			technique = ""
	else:
		technique += line
	line = inputFile.readline()

if technique != "":
	listOfSealedItemBlocks.append(technique)

print "Number of Techniques in file: %d" % len(listOfSealedItemBlocks)

#Begin processing each technique, creating the formatted list of sub-techniques that we will need to create
for sealedItemBlock in listOfSealedItemBlocks:
	sealedItemObj = SealedItem(sealedItemBlock)
	#print sealedItemObj.Title
	#print sealedItemObj.Type
	#print sealedItemObj.LevelPatternDictionary

	previousItem = None

	for item in range(0,5):
		if sealedItemObj.LevelPatternDictionary[SealedItemEnum[item]] != -1:
			#Create Item Statblock Here
			if sealedItemObj.Type == 'Sealed Item':
				title = 'Craft ' + SealedItemEnum[item] + ' ' + sealedItemObj.Title
			else:
				title = 'Craft ' + SealedItemEnum[item] + ' ' + sealedItemObj.Title + ' ' + sealedItemObj.Type
			print title
			previousItem = title


