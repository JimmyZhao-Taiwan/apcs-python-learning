brother=int(input())
numbers=int(input())
sister=input().split(" ")
brothers=[]
brothers.append(brother)

for i in range(1,int(numbers)):
    if int(sister[i]) == int(sister[i-1]) == 0:
        brothers.append('5')
    elif int(sister[i]) == int(sister[i-1]) == 2:
        brothers.append('0')
    elif int(sister[i]) == int(sister[i-1]) == 5:
        brothers.append('2')
    else:
        brothers.append(sister[i])
drew=()
for a in range(len(brothers)):
    if int(brothers[a])==2 and int(sister[a])==5:
        print(drew, brothers[a], ": Won at round", a+1)
    elif int(brothers[a])==0 and int(sister[a])==2:
        print(drew, brothers[a], ": Won at round", a+1)
    elif int(brothers[a])==5 and int(sister[a])==0:
        print(drew, brothers[a], ": Won at round", a+1)
    elif int(brothers[a])==2 and int(sister[a])==0:
        print(drew, brothers[a], ": Lost at round", a+1)
    elif int(brothers[a])==0 and int(sister[a])==5:
        print(drew, brothers[a], ": Lost at round", a+1)
    elif int(brothers[a])==5 and int(sister[a])==2:
        print(drew, brothers[a], ": Lost at round", a+1)
    if int(brothers[a])==int(sister[a]) and a+1<numbers:
        drew
        