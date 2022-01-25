#python code to check whether even or odd and prime no. check

n=int(input("Enter the number:"))
if n%2==0:
    print("Even No.")
else:
    print("odd no.")
if n==1:
    print("neither prime nor composite")
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print("Not prime")
            break
        else:
            print("prime")
            break
            
