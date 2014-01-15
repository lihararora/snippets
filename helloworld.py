import sys
alist = ["Rahil", "is", 22, "years", "old"]
alist.remove("old")
print(alist)
alist.reverse()
print(alist)
alist.reverse()
alist.insert(1,"Arora")
alist.insert(5,"old")
print(alist)
adict = {1:"uno", 2:"dos", 3:"tres"}
print(adict)
adict[5] = alist
print(adict)
for i in alist:
    print(type(i))
print(sys.path)
