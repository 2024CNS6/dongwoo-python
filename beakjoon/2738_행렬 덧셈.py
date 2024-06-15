n,m=map(int,input().split())
hang1=[]
hang2=[]
for i in range(n):
    a=list(map(int,input().split()))
    hang1.append(a)
for i in range(n):
    a=list(map(int,input().split()))
    hang2.append(a)
for i in range(n):
    for j in range(m):
        print(hang1[i][j]+hang2[i][j],end=' ')
    print()