p=0
s=0
for i in range(4):
    n,m=map(int,input().split())
    p-=n
    p+=m
    if p>s:
        s=p
print(s)