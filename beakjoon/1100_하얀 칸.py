chess=[]
s=0
for i in range(8):
    chess.append(list(input()))
for k in range(8):
    for q in range(8):
        if (k%2!=0 and q%2!=0) or (k%2==0 and q%2==0):
            if chess[k][q]=="F":
                s+=1
print(s)