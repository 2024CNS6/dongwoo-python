n=int(input())
for i in range(n):
    s=list(input().split())
    for k in range(len(s)):
        rv = ''
        for j in s[k]:
            rv=j+rv
        print(rv,end=" ")