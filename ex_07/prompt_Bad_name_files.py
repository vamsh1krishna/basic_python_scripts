fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File',fname,'cannot be opened or not found')
    quit()
count = 0
sum = 0
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    #print(line)
    pos = line.find(':')
    #print(pos)
    num = line[pos+1:]
    fnum = float(num)
    #print(fnum)
    sum = sum + fnum
    #print(sum)
print(sum/count)
