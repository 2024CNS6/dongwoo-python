h=-1
n=int(input())
for i in range(n):
    h+=2
    print(' '*(n-i-1)+"*"*h)
   
for i in range(n):
    h-=2
    print(' '*(i+1)+"*"*h)