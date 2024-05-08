s=list(input())
li=[]
u=0
x=True
for i in s:
    li.append(i.upper())
en=[0 for i in range(27)]
for j in li:
    if j=="A":
        en[0]+=1
    elif j=="B":
        en[1]+=1
    elif j=="C":
        en[2]+=1
    elif j=="D":
        en[3]+=1
    elif j=="E":
        en[4]+=1
    elif j=="F":
        en[5]+=1
    elif j=="G":
        en[6]+=1
    elif j=="H":
        en[7]+=1
    elif j=="I":
        en[8]+=1
    elif j=="J":
        en[9]+=1
    elif j=="K":
        en[10]+=1
    elif j=="L":
        en[11]+=1
    elif j=="M":
        en[12]+=1
    elif j=="N":
        en[13]+=1
    elif j=="O":
        en[14]+=1
    elif j=="P":
        en[15]+=1
    elif j=="Q":
        en[16]+=1
    elif j=="R":
        en[17]+=1
    elif j=="S":
        en[18]+=1
    elif j=="T":
        en[19]+=1
    elif j=="U":
        en[20]+=1
    elif j=="V":
        en[21]+=1
    elif j=="W":
        en[22]+=1
    elif j=="X":
        en[23]+=1
    elif j=="Y":
        en[24]+=1
    elif j=="Z":
        en[25]+=1
for p in en:
    if max(en)==p:
        if en.index(max(en))==u:
            pass
        else:
            print("?")
            x=False
            break
    u+=1
if x==True:
    print(chr(65+(en.index(max(en)))))