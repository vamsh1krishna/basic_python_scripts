pos = 0
def search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True



l=[9,8,7,6,5,4,3,2,1]

if search(l,4):
    print("Found at pos", pos+1)
else:
    print('not found')