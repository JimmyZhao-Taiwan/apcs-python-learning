a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
if a<=b<=c:
    max=c
    mid=b
    min=a
    print(a,b,c)
elif a<=c<=b:
    max=b
    mid=c
    min=a
    print(a,c,b)
elif b<=a<=c:
    max=c
    mid=a
    min=b
    print(b,a,c)
elif b<=c<=a:
    max=a
    mid=c
    min=b
    print(b,c,a)
elif c<=a<=b:
    max=b
    mid=a
    min=c
    print(c,a,b)
elif c<=b<=a:
    max=a
    mid=b
    min=c
    print(c,b,a)

if min + mid <= max:
    print("No")
elif min * min + mid * mid < max * max:
    print("Obtuse")
elif min * min + mid * mid == max * max:
    print("Right")
elif min * min + mid * mid > max * max:
    print("Acute")
