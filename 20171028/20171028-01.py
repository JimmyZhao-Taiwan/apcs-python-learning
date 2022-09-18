a,b,c=input().split(" ")

if int(a)==0 and int(b)==0 and int(c)==0:
    print("AND")
    print("OR")
    print("XOR")
elif int(a)!=0 and int(b)==0 and int(c)==0:
    print("AND")
elif int(a)==0 and int(b)!=0 and int(c)==0:
    print("AND")
elif int(a)!=0 and int(b)!=0 and int(c)==0:
    print("XOR")
elif int(a)==0 and int(b)==0 and int(c)==1:
    print("IMPOSSIBLE")
elif int(a)!=0 and int(b)==0 and int(c)==1:
    print("OR")
    print("XOR")
elif int(a)==0 and int(b)!=0 and int(c)==1:
    print("OR")
    print("XOR")
elif int(a)!=0 and int(b)!=0 and int(c)==1:
    print("AND")
    print("OR")
