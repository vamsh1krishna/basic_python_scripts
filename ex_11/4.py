import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://http://info.cern.ch/hypertext/WWW/Bugs.html')
for line in fhand:
    print(line.decode().strip())
