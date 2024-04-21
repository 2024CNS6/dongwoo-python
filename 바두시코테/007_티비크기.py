import math
d,h,w=map(int,input().split())
j=((d**2/(h**2+w**2))**(1/2))
print(f"{math.trunc(h*j)} {math.trunc(w*j)}")