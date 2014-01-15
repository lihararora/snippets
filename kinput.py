lb = int(input("Enter lower bound: "))
ub = int(input("Enter Upper bound: "))

print("You chose {0} as your lower bound and \
        {1} as your upper bound.".format(lb, ub))
verif = input("\nProceed? (y/n)")
response = verif.lower()

if response == 'y':
    for multiplier in range (lb, (ub + 1)):
        for i in range (1, 11):
            print("{0} x {1} = {2}".format(i, multiplier, i*multiplier))
else:
    print("We're done!")

