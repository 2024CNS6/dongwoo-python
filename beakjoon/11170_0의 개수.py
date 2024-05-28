tc=int(input())

for _ in range(tc):
    n,m=map(int,input().split())
    sum = 0
    for i in range(n,m+1):
        i=list(str(i))
        for k in i:
            if k=="0":
                sum+=1
    print(sum)