key=[]
for i in range(9):
    key.append(int(input()))

for k in range(9):
    for l in range(k+1,9):
        if sum(key)-100==key[k]+key[l]:
            key[k]=0
            key[l]=0
            break
key.sort()
for o in range(2,len(key)):
    print(key[o])