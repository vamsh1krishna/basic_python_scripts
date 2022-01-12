max = 0
min = None
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try :
        ival = int(sval)
        #print(fval)
        if max < ival:
            max = ival
        if min is None or min > ival:
            min = ival
    except:
        print('Invalid input')
#print('All Done')
print('Maximum is',max)
print('Minimun is',min)
