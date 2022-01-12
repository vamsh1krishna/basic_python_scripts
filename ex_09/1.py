fhand = open('mboxshort.txt')
lis = list()
di = {}
for line in fhand:
    lrs = line.rstrip()
    #print(lrs)
    wds = lrs.split()
    #print(wds) in a compound statement
    #guardian
    if len(wds) < 3 or wds[0] !='From':
        continue
    lis.append(wds[1])
#print(lis)

for a in lis:
    di[a] = di.get(a,0) + 1
#print(di)
count = 0
for k,v in di.items():
    if v > count:
        count = v
        rep = k
print(rep,count)
