n=int(input())
li=list(map(int,input().split()))
m=0
s=1
for i in li:
    if i==1:
        m+=s
        s+=1
    else:
        s=1
print(m)