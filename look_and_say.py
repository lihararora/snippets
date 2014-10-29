#!/usr/bin/python

import sys

def seq(s):
	freq = 1
	o = ''
	for i in range(len(s)):
		try: 
			if s[i] == s[i+1]:
				freq += 1
			else:
				o = o + str(freq) + s[i]
				freq = 1
		except IndexError:
				o = o + str(freq) + s[i]
				break
	return o

if __name__ == '__main__':
	print '1'
	n = seq('1')
	print n
	for i in range(3,10):
		n = seq(n)
		print n
        