a=int(input())
b=int(input())
c=int(input())
slist=[0]*10
f=list(str(a*b*c))
for i in f:
    if int(i)==0:
        slist[int(i)]+=1
    else:
        slist[int(i)]+=1
for j in slist:
    print(j)