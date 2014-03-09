#!/usr/bin/python

import urllib.request
import os

wp = urllib.request.urlopen('https://google.com')
print(wp.info())

