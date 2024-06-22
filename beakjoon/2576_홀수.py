li=[]
for i in range(7):
    n=int(input())
    if n%2!=0:
        li.append(n)
if len(li)!=0:
    print(sum(li))
    print(min(li))
else:
    print(-1)