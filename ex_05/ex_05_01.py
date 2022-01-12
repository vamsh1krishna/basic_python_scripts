num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try :
        fval = float(sval)
        #print(fval)
        num = num + 1
        tot = tot + fval
    except:
        print('Enter a numerical value')
#print('All Done')
print(num,tot,tot/num)
