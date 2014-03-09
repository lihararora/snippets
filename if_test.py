#!/usr/bin/python

while True: 
    s = input('Enter a string of at least 4 characters, or press "q" to quit: ')
    if s == 'q':
        break
    if len(s) < 4:
        print("Value is too small")
        continue
    print("The string you've entered is of sufficient length.")
    raise SystemExit 

