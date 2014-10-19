#This was written for Python 2.7

def get_repeat_remain(n,d):
	try:
		int(n)
		int(d)
	except ValueError:
		print "Not a valid number"
		raise
	if n <= 0:
		print "Not Supported"
		return #raise TypeError('Invalid')
	if d <= 0:
		print "Not Supported"
		return

	total = n/d
	remainder = n%d
	lookuptable = {}
	cycle = 0
	retval = []
	retval.append(str(total))
	retval.append('.')
	while not remainder in lookuptable:
		lookuptable[remainder] = cycle
		total = (remainder * 10) / d
		remainder = (remainder * 10) % d
		cycle += 1
		retval.append(str(total))
	retval.append(')')
	retval.insert(lookuptable[remainder]+2, '(')
	return ''.join(retval)

print get_repeat_remain(12, 3)
print get_repeat_remain(1, 3)
print get_repeat_remain(1, 2)
print get_repeat_remain(1, 7)
print get_repeat_remain(1, 8)
print get_repeat_remain(3.5, 2)