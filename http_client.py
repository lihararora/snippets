#!/usr/bin/python

import http.client
files = ['/lihararora', '/anksharma90']
h = http.client.HTTPConnection('graph.facebook.com')
h.connect()

for f in files:
    h.request('GET',f)
    r = h.getresponse()
    if r.status == http.client.OK:
        data = r.read()
        print(data)

h.close()
