#!/usr/bin/env python
import cgi
import random

# dict of words
pre = ("nice ", "lucky ", "rich ", "good ", "big ", "strong ", "long ", "fat ", "funny ", "serious ", "awersome ", "unreal ", "fast ", "slow ", "tall ")
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head><title>CGI Program</title></head>'
print '<body>'
form = cgi.FieldStorage()
print '<form method="get" action="hello.py">'  # input data form
print '<p>Name: <input type="text" name="name"/></p>'
print '<input type="submit" value="Submit" />'
print '</form>'
if form.getvalue("name"):
    name = form.getvalue("name")
    with open("db.txt") as f:  # reading database
        prevdb = f.read()
    fp = prevdb.split(" ")
    name = str(name)
    if fp.count(name):  # if not new name input
        n = fp[fp.index(name) + 1]
        n = int(n)
        print '<h1>Nice to see you again ' + pre[n] + name + '</h1>'
    else:  # if new name input
        str(prevdb)
        r = random.randrange(0, 14, 1)
        cdb = prevdb + name + " " + str(r) + " "
        with open("db.txt", 'w+') as f:
                f.write(cdb)
        print '<h1>Nice to see you {} {} </h1>'.format(pre[r], name)
print '</body>'
print '</html>'
