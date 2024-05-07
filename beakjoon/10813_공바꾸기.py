n,m=map(int,input().split())
li=[0 for i in range(n)]
for r in range(n):
    li[r]+=r+1
co=list(li)
for p in range(m):
    i,j=map(int,input().split())
    li[i-1]=co[j-1]
    li[j-1]=co[i-1]
    co=list(li)
print(*li)