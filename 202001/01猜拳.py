first=input()
numbers=input()
sister=input().split(" ")
for i in range(0,int(numbers)):
    if first==2 and sister[i]==5:
        print(first, ":Won at round", i)
    elif first==0 and sister[i]==2:
        print(first, "Won at round", i)
    elif first==5 and sister[i]==0:
        print(first, "Won at round", i)
    elif first==2 and sister[i]==0:
        print(first, "Lost at round", i)
    elif first==0 and sister[i]==5:
        print(first, "Lost at round", i)
    elif first==5 and sister[i]==2:
        print(first, "Lost at round", i)
