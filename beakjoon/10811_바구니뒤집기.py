n, m = map(int, input().split())
li = [0 for i in range(n)]
for r in range(n):
    li[r] += r + 1
co = list(li)
for p in range(m):
    i, j = map(int, input().split())
    for k in range((j - i + 1) // 2):
        li[i + k - 1], li[j - k - 1] = li[j - k - 1], li[i + k - 1]
    co = list(li)
print(*li)