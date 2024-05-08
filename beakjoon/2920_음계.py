a=list(map(int,input().split()))
b=list(a)
c=list(a)
a.sort(reverse=True)
if b==a:
    print("descending")
a.sort()
if b==a:
    print("ascending")
c.sort(reverse=True)
if b!=a and b!=c:
    print("mixed")
