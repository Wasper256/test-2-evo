#!/usr/bin/python
import os
import cgi
import cgitb
cgitb.enable()

num = 0
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head><title>My First CGI Program</title></head>'
print '<body>'
print '<h1>Hello Program!</h1>'
form = cgi.FieldStorage()
print '<form method="get" action="hello.py">'
print '<p>Name: <input type="text" name="name"/></p>'
print '<input type="submit" value="Submit" />'
print '</form>'
if form.getvalue("name"):
    name = form.getvalue("name")
    print '<h1>Hello ' + name + '</h1>'
    with open("db.txt") as f:
        pdb = f.read()
        print(str(pdb))
    num = num + 1
    cdb = pdb + name + str(num) + " \n"
    with open("db.txt", 'w+') as f:
            f.write(cdb)
print '</body>'
print '</html>'
