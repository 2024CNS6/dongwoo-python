n=int(input())
m=10
while 1:
    if n>m:
        n = m * ((n + m // 2) // m)
    else:
        break
    m *= 10
print(n)