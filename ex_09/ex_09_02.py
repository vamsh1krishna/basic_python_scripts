fname = input('Enter File:')
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)
ddd = dict()
for lin in fhand:
    lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(lin)
    for word in wds:
        ddd[word] = ddd.get(word,0) + 1
        #print(word,ddd[word])

#print(ddd)
Bigcount = 0
Bigword = 0
lw = lis()
for k,v in ddd.items():
    print(len(k))
    if v > Bigcount:
        Bigcount = v
        theword = k



print(theword,'repeated',Bigcount,'times')
