import sys
nums=[]
n=int(sys.stdin.readline())
for i in range(n):
    nums.append(int(sys.stdin.readline()))
for l in sorted(nums):
    print(l)