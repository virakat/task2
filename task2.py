#! /usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

cmd = cgi.FieldStorage()

x = cmd.getvalue("c")


y = subprocess.getoutput("sudo " + x) 

print("<b>Your Command Output Is Here : <b />")


print(y)

print("<br />")
print("<br />")

print("<b>For more command back to my html page & type some more command <b />")
print("<br />")
print("<br />")
print("<b> Thanku For Using My Program <b />")
