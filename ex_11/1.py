fhand = open('mboxshort.txt')
import re
x = re.findall('([0-9.]*)',fhand)
print(x)