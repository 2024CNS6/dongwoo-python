n,s=input().split()
rv_n=' '
rv_s=' '
for i in n:
    rv_n=i+rv_n
for i in s:
    rv_s=i+rv_s
if rv_s>rv_n:
    print(rv_s)
else:
    print(rv_n)