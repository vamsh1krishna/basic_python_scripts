lnu = []


while True:
    num = input('Enter a value: ')
    if num == 'done':
        break
    else:
        try:
           fval = float(num)
           lnu.append(fval)
        except :
           print('Enter a numeric value')
x = max(lnu)
y = min(lnu)
print('Max:',x)
print('Min:',y)
quit()
