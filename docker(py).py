#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()

osname = form.getvalue("x")
osimage = form.getvalue("i")
print(f"{osname},{osimage}")

cmd = "sudo docker run -dit --name {} {}".format(osname,osimage)

output = sp.getstatusoutput(cmd)

status = output[0]
out_put = output[1]
if status == 0:
	print("os lunched succesfully {}..".format(osname))
else:
	print("some error : {}".format(out_put))
