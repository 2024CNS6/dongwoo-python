s=int(input())
for i in range(s):
    n,m=map(int,input().split())
    same = []
    for j in range(1, n + 1):
        if n % j == 0 and m % j == 0:
            same.append(j)

    print(int((n*m)/max(same)))