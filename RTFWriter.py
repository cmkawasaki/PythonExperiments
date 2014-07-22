#This was written for Python 2.7

class RTFWriter(object):
	def __init__(self, fileName):
		self.FileHandle = open(fileName, 'w')
		self.FileHandle.write('{\\rtf1\\ansi\\ansicpg1252\\deff0{\\fonttbl{\\f0\\fswiss\\fcharset0 Times New Roman;}}\\n')
		self.FileHandle.write('{\\*\\generator Msftedit 5.41.15.1507;}\\viewkind4\\uc1\\pard\\f0\\fs24 ')
	def Close(self):
		self.FileHandle.write('}')
		self.FileHandle.close()
	def Write(self, stringToWrite):
		self.FileHandle.write(stringToWrite)
	def WriteBold(self, stringToWrite):
		self.FileHandle.write('\\b ' + stringToWrite + '\\b0 ')
	def WriteItalics(self, stringToWrite):
		self.FileHandle.write('\\i ' + stringToWrite + '\\i0 ')
	def Writeline(self, stringToWrite):
		self.FileHandle.write(stringToWrite + '\\par\\n ')
	def InsertReturn(self):
		self.FileHandle.write('\\par\\n ')
