n=int(input("Enter the no. "))
sum=0

a=n
while a>0:
    b=a%10
    sum+=b**3
    a//=10

if n==sum:
    print("Armstrong")
else:
    print("Not Armstrong")
