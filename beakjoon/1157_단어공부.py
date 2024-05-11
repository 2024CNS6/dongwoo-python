s=list(input())
li=[]
u=0
x=True
for i in s:
    li.append(i.upper())
en=[0 for i in range(27)]
for j in li:
    en[ord(j)-65]+=1
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
