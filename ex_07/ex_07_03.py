fname = input('Enter the file name: ')
count = 0
try:
    fhand = open(fname)
except:
    print(fname)
    quit()
for line in fhand:
    count = count + 1
print('Line Count:',count)
