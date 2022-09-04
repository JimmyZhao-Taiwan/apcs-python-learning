numbers=input()
a=[]
d=0
j=0
for i in range(numbers):
    a[i]=input()
for e in a:
    f,g=a[e].split(" ")
    for h in range(numbers):
        if g==a[h].split(" ")[1]:
            j=j+1
