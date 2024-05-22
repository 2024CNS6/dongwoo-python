n=int(input())
s=list(map(int,input().split()))
sosu=int(n)
for i in range(n):
    if s[i]==1:
        sosu-=1
    else:
        for k in range(2,s[i]):
            if s[i]%k==0:
                sosu-=1
                break
print(sosu)