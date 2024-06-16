import math
l=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if math.ceil(b/d)<math.ceil(a/c):
    print(l-math.ceil(a/c))
else:
    print(l-math.ceil(b/d))