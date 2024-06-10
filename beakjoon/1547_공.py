cup=[1,0,0]
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    cup[a-1],cup[b-1]=cup[b-1],cup[a-1]
print(cup.index(1)+1)