#program a simple interest calculator for bank


p=int(input("Principal: "))
t= int(input("Time in months:"))
if t<12 and p>100000:
    r=7
elif t<12:
    r=5   
if t>12 and t<=24:
    r=8
elif t>24 and t<36 :
    r=9
elif t>36:
    r=10
s=(p*r*t)/100
print("Simple interest: ",float(s))
