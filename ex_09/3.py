fhand = open('mboxshort.txt')
lis = list()
di = {}
ln = list()
for line in fhand:
    lrs = line.rstrip()
    wds = lrs.split()
    #print(wds) in a compound statement
    #guardian
    if len(wds) < 3 or wds[0] !='From':
        continue
    lis.append(wds[1])
for wd in lis:
    wds = wd.split('@')
    ln.append(wds[1])
di2 ={}
for ad in ln:
    di2[ad] = di2.get(ad,0) + 1
print(di2)
