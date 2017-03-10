#!/usr/bin/python

str = 'abcde'
cnt = 0

def permutate(base, rem):
	global cnt
	if len(rem) == 0:
		print base
		cnt += 1
		return

	for i in range(len(rem)):
		new_rem = rem[:i] + rem[i+1:]
		permutate(base + rem[i], new_rem)


permutate('', str)
print cnt

