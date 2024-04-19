x,y,w,h=map(int,input().split())
if x>w-x:
    x_min=(w-x)
else : 
    x_min=x
if y>h-y:
    y_min=h-y
else:
    y_min=y

if y_min<x_min:
    print(y_min)
else:
    print(x_min)