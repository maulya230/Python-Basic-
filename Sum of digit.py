'''
Accept a number. display the sum of the digits of that number
IP: 23579
OP: 2+3+5+7+9
'''
n=int(input("enter the no.: "))
t=n
sum=0
while n>0:
    digit=n%10
    n=int(n/10)
    sum=sum+digit
print("Sum of {} is: {}".format(t,sum))
    
# Output
#enter the no.: 23579
# Sum of 23579 is: 26
