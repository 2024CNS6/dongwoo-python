import sys
n = int(sys.stdin.readline())
a = set()
for _ in range(n):
    a.add(sys.stdin.readline().strip())
a = sorted(a)
p = 1
while a:
    to_remove = []
    for s in a:
        if len(s) < p:
            print(s)
            to_remove.append(s)
    for s in to_remove:
        a.remove(s)
    p += 1
