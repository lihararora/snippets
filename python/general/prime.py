#!/usr/bin/python

'''
@author: Rahil Arora
@contact: rahil@jhu.edu
'''

def is_prime(num):
    for j in range(2,num):
        if (num % j) == 0:
            return False
    return True

if __name__ == "__main__":
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    for i in range(low,high):
        if is_prime(i):
            print(i)


