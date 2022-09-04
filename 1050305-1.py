student=int(input())
number=input().split(" ")
newnumber=[]
for i in range(student):
    newnumber.append(int(number[i]))
sortnumber=sorted(newnumber)
for a in sortnumber:
    print(a, end=' ')
print("")

if sortnumber[0]>=60:
    print(sortnumber[0])
    print("best case")

for b in sortnumber:
    if b<60 and b+1>60:
        print(b)


if sortnumber[student-1]<60:
    print(sortnumber[student-1])
    print("worst case")

for c in sortnumber:
    if c>60 and c-1<60:
        print(c)