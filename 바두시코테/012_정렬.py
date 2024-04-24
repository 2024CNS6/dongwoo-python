list=list(map(int,input().split()))
list.sort(reverse=True)
s=0
for i in list:
    print(i,end=' ')
    s+=1
    if s==2:
        s=0
        print()
print("호준이")