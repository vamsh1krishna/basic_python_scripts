lnu = []
while True:
    sval = input('Enter a value: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
        lnu.append(fval)
    except:
        print('Enter a valid number')
x = max(lnu)
y = min(lnu)
print('Max:',x)
print('Min:',y)
