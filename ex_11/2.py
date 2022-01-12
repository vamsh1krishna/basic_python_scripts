import re
count = 0
sum = 0
fhand = open('mboxshort.txt')
lst = list()
for i in fhand:
    i = i.rstrip()
    x = re.findall('([0-9])',i)
    #print(x)
    if len(x) > 0:
        #print(x)
        for i in x:
            y = int(i)
            sum = sum + y
            count = count + 1
print(sum,count,sum/count)
