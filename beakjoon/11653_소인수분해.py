import sys
n=int(sys.stdin.readline())
for i in range(2,n+1):
    while 1:
        if n%i==0:
            print(i)
            n=n//i
        else:
            break