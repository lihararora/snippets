#!/usr/bin/python

import os
for k,v in os.environ.items():
    print("{0} = {1}".format(k,v))
