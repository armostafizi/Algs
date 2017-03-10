n = input()
values = []

def fib(n):
	global values
	if len(values) > n :
		#print 'Exists'
		return values[n]

	if n == 0:
		values.append(0)
		return 0
	elif n == 1:
		values.append(1)
		return 1
	else:	
		f = fib(n-1) + fib(n-2)
		values.append(f)
		return f


def all_fibs(n):
	global values
	for i in range(0, n+1):
		print '%d: %d' % (i, fib(i))


all_fibs(n)
