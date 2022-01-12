import json
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

inp = input('Enter a url: ')
html = urllib.request.urlopen(inp, context=ctx).read()

count = 0
link = json.loads(html)
#print(type(link))
#print(link)
for b in link:
    #print(len(link[b]))
    if len(link[b]) != 50:
        continue
    else:
        x = link[b]
        #print(x)
    for i in x :
        #print('Name:',i['name'])
        count = count + int(i['count'])
    print(count)
