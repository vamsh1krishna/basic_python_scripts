fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:',count)
fhand = open('mbox.txt')
inp = fhand.read()
x = len(inp)
print(x)
