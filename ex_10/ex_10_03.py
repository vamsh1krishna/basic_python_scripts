finp = input('Enter file name: ')
if len(finp) < 0:
    quit()
else:
    fhand = open(finp)

#def splitstring(str):
#    aplha = ''
#    special = ''
#        if s

di = {}
#li = list['a','q','w','e','r','t','y','u','i','o','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
for line in fhand:
    line = line.rstrip()
#    print(line[0])
    if len(line) < 3:
        continue
    else:
        wds = line.split()
        #print(wds)
        for wd in wds:
            wd = wd.lower()
            #print(wd)
            for let in wd:
                #print(type(wd))
                di[let] = di.get(let,0) + 1
                #print(let)
#print(di)
fnl = dict()
for k,v in di.items():
    if not (k.isalpha()):
        continue
    else:
        fnl[k] = v
count = 0
for i in sorted(fnl.keys()):
    count = count + fnl[i]
    #print(i,fnl[i])
for i in sorted(fnl.keys()):
    print(i,fnl[i],fnl[i]/count*100)
#print(count)
