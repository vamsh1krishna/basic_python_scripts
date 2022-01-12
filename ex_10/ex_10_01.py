fhand = open('mboxshort.txt')
lst = list()
for line in fhand:
    line = line.split()
    if len(line) < 3 :
        continue
    if line[0] == 'From':
        lst.append(line[1])
#print(lst)
counts = {}
for c in lst:
    counts[c] = counts.get(c,0) + 1
#print(counts)
fl = sorted([(v,k) for k,v in counts.items()], reverse=True)
for val,key in fl[:1]:
    print(key,val)
