s = input()
n = 0
o = len(s)
time = 0

for i in range(len(s)):
    if time != 0:
        time -= 1
    else:
        if i < len(s) - 2:
            if s[i] == "d" and s[i+1] == "z" and s[i+2] == "=":
                n += 1
                o -= 3
                time += 2
        if i < len(s) - 1:
            if s[i:i+2] in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
                n += 1
                o -= 1
                time += 1

print(n + o)