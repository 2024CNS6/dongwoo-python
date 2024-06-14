en=[0]*26
while 1:
    try:
        st=input()
        for i in st:
            if i != ' ':
                en[ord(i)-97]+=1
    except:
        break
ma=max(en)
for l in range(len(en)):
    if en[l]==ma:
        print(chr(l+97),end="")
    en[l]=0
