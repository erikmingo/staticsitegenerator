#!/usr/bin/python

import os
import sys

i = 0
while i < 10:
    f = open("%s.html" % i, 'w')  
    f.write("<html><body><h1>HEY MY page num is %s </h1></body></html>" % i)
    f.close
    i = i + 1


