import urllib2
import urllib
import json
import sys
import timeit
import random
import string

URL="www.example.com"
def testemail(email, n):
    params = {"u":email+"@example.com",
            "password":"AA" * n, "mfacode":"756218"}
    data = urllib.urlencode(params)
    resp = urllib2.Request(URL, data)
for i in range(1,10):
    n = 10**i
    print("Real - %d: %f" % (i, timeit.timeit(stmt='testemail("' + "test" + '", ' + str(n) +')', setup='from __main__ import testemail', number=2)))

