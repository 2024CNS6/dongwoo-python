n,m=map(int,input().split())
same=[]
for i in range(1,n+1):
    if n%i==0 and m%i==0:
        same.append(i)

print(max(same))
print(int((n*m)/max(same)))