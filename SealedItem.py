#This was written for Python 2.7
import re # Regular Expression Handler

class SealedItem(object):
	def __init__(self, sealedItemBlock):
		titleBlockPattern = re.compile(r'(?P<Title>.*)\[(?P<Type>.*)\]\n')
		titleMatch = titleBlockPattern.search(sealedItemBlock)
		levelMatchPattern = re.compile(r'(?P<Type>Minor|Superior|Greater|Epic|Legendary) \(Lv (?P<Level>\d+)\)')
		if titleMatch == None:
			print "No Title Section found.  Aborting."
			return
		self.Title = titleMatch.group('Title').strip(' \t\n\r')
		print "%r" % titleMatch.group('Type')
		if 'Sealed Item' in titleMatch.group('Type'):
			self.Type = "Sealed Item"
		elif 'Armor' in titleMatch.group('Type'):
			self.Type = "Armor"
		else:
			self.Type = "Weapon"

		self.LevelPatternDictionary = {'Minor':-1, 'Superior':-1, 'Greater':-1,'Epic':-1,'Legendary':-1}

		levelMatches = levelMatchPattern.findall(sealedItemBlock)
		if levelMatches == None:
			print "No Item levels found.  Aborting."
			return
		for levelMatch in levelMatches:
			self.LevelPatternDictionary[levelMatch[0]] = int(levelMatch[1])


SealedItemEnum = ['Minor', 'Superior', 'Greater', 'Epic', 'Legendary']
