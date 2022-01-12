fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('Fie cannot be opened')
    quit()
words = dict()
for line in fhand :
    strings = line.split()
    for sword in strings:
        if sword not in words :
            words[sword] = 1
        else:
            words[sword] = words[sword] + 1

print(words)
