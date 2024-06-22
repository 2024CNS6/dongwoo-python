n,m=map(int,input().split())
li=[]
for i in range(1,n+1):
    if n%i==0:
        li.append(i)
try:
    print(li[m-1])
except:
    print(0)