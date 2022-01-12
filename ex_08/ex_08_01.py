inp = input('Enter the file name: ')
file = open(inp)
llst = []
for line in file :
    lst = line.split()
    #print(lst)
    for x in lst :
        #print(x)
        if x not in llst:
            llst.append(x)
#print(llst)
llst.sort()
print(llst)
