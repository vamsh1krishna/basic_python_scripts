fhand = open('mboxshort.txt')
for line in fhand:
    lrs = line.rstrip()
    #print(lrs)
    wds = lrs.split()
    #print(wds) in a compound statement
    #guardian
    if len(wds) < 3 or wds[0] !='From':
        continue
    print(wds[2])
