a=input()
b=[None]*100000
for i in range(0,int(a)):
    c=input()
    d,e=c.split(" ")
    f=int(e)-int(d)
    for g in range(f):
        b[int(d)+int(g)]=("yes")
print(b.count("yes"))
