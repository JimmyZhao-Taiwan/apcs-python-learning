x=[]
x=list(input())
a=0
b=0
for i in range(len(x)):
    if i%2 == 0:
        b=b+int(x[i])
    else:
        a=a+int(x[i])

if a>b:
    print(a-b)
elif a<b:
    print(b-a)
else:
    print(a-b)