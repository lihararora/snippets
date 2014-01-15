import sys
alist = ["Rahil", "is", 22, "years", "old"]
print(alist)
alist.reverse()
print(alist)
adict = {1:"uno", 2:"dos", 3:"tres"}
print(adict)
adict[5] = alist
print(adict)
for i in alist:
    print(type(i))
print(sys.path)
