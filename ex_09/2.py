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
    lis.append(wds[2])
#print(lis)

for wd in lis:
    di[wd] = di.get(wd,0) + 1
print(di)
