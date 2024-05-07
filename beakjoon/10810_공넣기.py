n,m=map(int,input().split())
li=[0 for i in range(n)]
for o in range(m):
    i,j,k=map(int,input().split())
    for y in range(i,j+1):
        li[y-1]=k
print(*li)