n = int(input())

for i in range(n):
    li = list(input())
    sum = 0
    streak = 0

    for w in li:
        if w == "O":
            sum += 1
            streak += 1
            sum += max(0, streak - 1)
        else:
            streak = 0
    print(sum)
