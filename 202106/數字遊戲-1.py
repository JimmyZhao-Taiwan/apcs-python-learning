#https://zerojudge.tw/ShowProblem?problemid=i399
a, b, c = input().split(" ")
if a == b == c:
    print('3', a)
elif a == b:
    if a > c:
        print('2', a, c)
    elif c > a:
        print('2', c, a)
elif a == c:
    if a > b:
        print('2', a, b)
    elif b > a:
        print('2', b, a)
elif b == c:
    if a > b:
        print('2', a, b)
    elif b > a:
        print('2', b, a)
else:
    if a > b > c:
        print('1', a, b, c)
    elif a > c > b:
        print('1', a, c, b)
    elif b > a > c:
        print('1', b, a, c)
    elif b > c > a:
        print('1', b, c, a)
    elif c > a > b:
        print('1', c, a, b)
    elif c > b > a:
        print('1', c, b, a)
