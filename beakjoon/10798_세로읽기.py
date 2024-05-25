li = []
for i in range(5):
    li.append(list(input()))

max_len = max(len(sublist) for sublist in li)

for k in range(max_len):
    for l in range(len(li)):
        if k < len(li[l]):
            print(li[l][k], end='')
