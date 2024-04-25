n=int(input())
for i in range(n):
    a,b=(input().split())
    a=int(a)
    for k in b:
            print(k*a, end='')
    print()