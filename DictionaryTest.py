#This was written for Python 2.7

def find_nth_prime(n):
	if n <= 0:
		print 'Invalid Input'
		return None
	print 'Valid Input'

dict = {}
dict['test'] = 3
dict['test2'] = 4
if dict.has_key('test') == True:
	print dict['test']

if dict.has_key('test2') == True:
	print dict['test2']

find_nth_prime(None)