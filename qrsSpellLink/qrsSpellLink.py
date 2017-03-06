#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys

# synchronize folder
src = ""
# Default Domain Name
name = ""
param = sys.argv[1]

temp = param[(len(src)+1)+1:]
temp = temp.replace('\\', '/')
print (name+temp)