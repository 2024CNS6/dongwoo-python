import sys
for i in range(3):
    n = int(sys.stdin.readline())
    li=[int(sys.stdin.readline()) for i in range(n)]
    if sum(li)==0:
        print(0)
    elif sum(li)>0:
        print("+")
    else:
        print("-")