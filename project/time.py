week = {'sunday': 1,'monday':2,'tuesday':3,'wednesday':4,'thursday':5,'friday':6,'saturday':7}
def get_key(val):
    for i1, i2 in week.items():
        if i2 == val:
            return i1


def add_time(given_time, atime, day=True):
    ct = given_time.split()
    at = atime.split()
    c = ct[0].split(':')
    a = atime.split(':')
    h1 = int(c[0])
    m1 = int(c[1])
    h2 = int(a[0])
    m2 = int(a[1])
    m = m1 + m2
    hu = h1 + h2
    h = hu%12
    d = hu//12
    if d%2 == 0 and h == 0:
        md = ct[1]
    else:
        if ct[1] == 'PM':
            md = 'AM'
        else:
            md = 'PM'
    if m >= 60:
        h = h + 1
        m = m - 60
        mf = str(m)
    else:
        mf = str(m)
    if len(mf) == 1:
        mf = '0' + mf
    hf = str(h)
    d1 = int(hu%24)
    d2 = hu//12
    d4 = hu//24
    if ct[1] == 'PM' and (h1+d1)>=12:
        z = d4 + 1
    else:
        z = d4
    d3 = str(z)
    if ct[1] == 'AM' and h2<12:
        x = ''
    elif ct[1] == 'PM' and hu>=12 and hu<=24:
        x = '(next day)'
    elif ct[1] == 'PM' and hu<12:
        x =''
    else:
        x = '('+d3+' '+'days later'+')'

    if day!= True:
        u = day.lower()
        v = (week[u]+z)%7
        y = get_key(v)
        wd = y.capitalize()
        k = hf+':'+mf+' '+md+' '+wd+' '+x
    else:
        k = hf+':'+mf+' '+md+' '+x
    print(k)

add_time("3:00 PM", "3:10")

add_time("11:30 AM", "2:32", "Monday")

add_time("11:43 AM", "00:20")

add_time("10:10 PM", "3:30")

add_time("11:43 PM", "24:20", "tueSday")

add_time("6:30 PM", "205:12")
