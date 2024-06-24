n=int(input())
yl=list(map(int,input().split()))
yl.sort()
print(yl[0]*yl[-1])