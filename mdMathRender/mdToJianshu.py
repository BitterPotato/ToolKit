import re
import codecs
import sys

rpath = sys.argv[1]
index = rpath.find(".md")
wpath = rpath[:index] + "_js" + rpath[index:]

file = codecs.open(rpath, "r", "utf-8")
wfile = codecs.open(wpath, 'w', "utf-8")

count = 0

while 1:
    line = file.readline()
    if not line:
        break
    
    if line.count('$$') == 1:
        line = line.replace('$$', '![](http://latex.codecogs.com/svg.latex?', 1)
        
        bline = file.readline()
        while bline.count('$$') != 1:
            line = line.rstrip()
            line += bline
            bline = file.readline()
        line = line.rstrip()
        line += bline
        line = line.replace('$$', ')', 1)

    else:
        while line.find('$$', 0, len(line)) != -1:
            count += 1
            if count % 2 == 1:
                line = line.replace('$$', '![](http://latex.codecogs.com/svg.latex?', 1)
            else:
                line = line.replace('$$', ')', 1)

    wfile.write(line)
    