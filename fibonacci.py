def fib(n):
    n1=0
    n2=1
    if n<0:
        print("Not valid")
    elif n==0:
        print(0)
    elif n==1:
        print(0)
        print(1)
    else:
        for i in range(0,n):
            print(i)
            i+=1
n=int(input("Enter the no. "))
fib(n)
