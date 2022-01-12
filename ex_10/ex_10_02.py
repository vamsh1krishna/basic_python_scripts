fhand = open('mboxshort.txt')
lst = list()
for line in fhand:
    line = line.split()
    if len(line) < 3 :
        continue
    if line[0] == 'From':
        lst.append(line[5])
dn = dict()
for a in lst:
    a = a.split(':')
    dn[a[0]] = dn.get(a[0],0) + 1
db = sorted([(k,v) for k,v in dn.items() ])
for b,c in db[:]:
    print(b,c)
