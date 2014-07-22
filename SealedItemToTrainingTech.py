#This was written for Python 2.7
from sys import argv
from os.path import exists
from SealedItem import *
from RTFWriter import *
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
listOfTechniquesToMake = []
dictOfTechniquesToMake = {}

for sealedItemBlock in listOfSealedItemBlocks:
	sealedItemObj = SealedItem(sealedItemBlock)
	#print sealedItemObj.Title
	#print sealedItemObj.Type
	#print sealedItemObj.LevelPatternDictionary

	previousItem = None

	for item in range(0,5):
		if sealedItemObj.LevelPatternDictionary[SealedItemEnum[item]] != -1:
			title = sealedItemObj.GenerateTitle(item)
			listOfTechniquesToMake.append(title)
			dictOfTechniquesToMake[title] = sealedItemObj.GenerateItem(item, previousItem)
			previousItem = title

#After For Loop completes, there should be a list of techniques and a dictionary with their loaded data.
#Sort the Loop to determine printing order
listOfTechniquesToMake.sort()

writer = RTFWriter('.\\Output.rtf')

for techTitle in listOfTechniquesToMake:
	title, requireString, rank, jutsuClass, learnDC, successesNeeded, itemTitle, price = dictOfTechniquesToMake[techTitle]
	#Print the Techniques using an RTF Writer in the Sorted Order
	writer.WriteBold(title)
	writer.InsertReturn()
	writer.WriteItalics(requireString)
	writer.InsertReturn()
	writer.WriteBold('Rank: ')
	writer.Write(str(rank) + ' (' + jutsuClass + '); ')
	writer.WriteBold('Learn DC: ')
	writer.Write(str(learnDC) + ', ' + str(successesNeeded) + ' successes; ')
	writer.WriteBold('Components:')
	writer.Writeline(' X, Mas')
	writer.Write('The user gains the knowledge required to craft a ')
	writer.WriteItalics(itemTitle)
	writer.Writeline('. See Ninja Tools section for details. The subtype is either Ninjutsu if learned with Craft (calligraphy) or Fuinjutsu if learned with Fuinjutsu. ')
	writer.InsertReturn()
	writer.WriteItalics('Mastery')
	writer.InsertReturn()
	writer.Writeline('TO BE WRITTEN')
	writer.WriteBold('Expendable Components: ')
	writer.Write('Arcane crystals sufficient required to make a couple sample seals (%s Ryo)' % ("{:,}".format(price)))
	writer.InsertReturn()
	writer.InsertReturn()
writer.Close()
