a=[]
y=[]
z=[]
b=float(input("ENTER HOW MANY NUMBERS YOU WANT TO ENTER IN THE PARTICULAR LIST"))
c=1
while(c<=b):
    d=float(input("ENTER THE PARTICULAR NUMBER"))
    a.append(d)
    c+=1
print(a)
for x in a:
    if(x>=0):
        y.append(x)
        print("THE POSITIVE NUMBERS ARE",x)
    else:
        z.append(x)
        print("THE NEGATIVE NUMBERS ARE",x)
print("THE POSITIVE LIST:",y)
print("THE NEGATIVE LIST:",z)

