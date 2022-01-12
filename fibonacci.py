import sys
sys.setrecursionlimit(1140)

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

i = int(input("Enter a Postive value: "))
print(fibonacci(i))