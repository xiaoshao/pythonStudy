#!/usr/bin/python

import socket
import struct
import sys
import os
import time

RUN_PATH=u'/Applications/RubyMine.app/Contents/MacOS/rubymine'
CONFIG_PATH=u'/Users/zwshao/Library/Preferences/RubyMine70'

args=[]
skip_next=False

for i, arg in enumerate(sys.argv[1:]):
	print i 
	print arg