n,m=map(int,input().split())
n1,m1=n,m
while 1:
    if n==m:
        break
    elif n<m:
        n+=n1
    elif n>m:
        m+=m1
print(m)