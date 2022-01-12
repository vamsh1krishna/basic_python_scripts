fhand = open('mboxshort.txt')
count = 0
for line in fhand:
    line = line.split()
    #print(line)
    if line != [] and line[0] == 'From':
        count = count + 1
        print(line[1])
print("There were",count,"lines in the file with From as the first word")
