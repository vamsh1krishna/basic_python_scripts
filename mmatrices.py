from numpy import*
import numpy

def inparr(x,y):
    z= array([])
    for i in range(x*y):
        uc=array([int(input('Enter value: '))])
        z=concatenate([z,uc])
    z=z.reshape(x,y)
    return z


a,b = input('Enter the matrix 1 dimensions: ').split( )
a=int(a)
b=int(b)
m1= inparr(a,b)
c,d = input('Enter the matrix 2 dimensions: ').split( )
c=int(c)
d=int(d)
m2 = inparr(c,d)



if m1.shape[1] != m2.shape[0] or m2.shape[1]!=m1.shape[0]:
    print('Given Matrices dimension cannot be multiplied')
    quit()


arr=array([])
for i in range(m1.shape[0]):
    m3= m1[i]
    for e in range(m2.shape[1]):
        m4 = m2[:,[e]]
        #print(m3)
        #print(m4)
        ad=0
        for j in range(m1.shape[1]):
            m5=m3[j]
            m6=m4[j]
            #print(m5)
            #print(m6)
            hi=m5*m6
            ad=ad+hi
        #print(ad)
        arr=concatenate([arr,ad])
       
print(arr.reshape(m1.shape[0],m2.shape[1]))






