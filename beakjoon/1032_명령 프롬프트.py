n = int(input())
st = input()
po = list(st)

for _ in range(n - 1):
    s = input()
    for i in range(len(s)):
        if po[i] != s[i]:
            po[i] = '?'

print(''.join(po))