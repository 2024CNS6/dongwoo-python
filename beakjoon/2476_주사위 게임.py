n = int(input())

max_reward = 0
for _ in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        reward = 10000 + a * 1000
    elif a == b or a == c:
        reward = 1000 + a * 100
    elif b == c:
        reward = 1000 + b * 100
    else:
        reward = max(a, b, c) * 100

    if reward > max_reward:
        max_reward = reward

print(max_reward)
