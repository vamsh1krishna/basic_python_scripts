def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(0,n):
            c=a+b
            a=b
            b=c
            if c<100:
                print(c)
            else:
                quit()


x=int(input("How many fibonacci number: "))

fib(x)

