dic={}
n=int(input())
for i in range(n):
    name,score=input().split()
    score=int(score)
    dic[name]=score

dic = sorted(dic.items(), key= lambda item:item[1], reverse=True)
for j in range(n):
    if dic[j][1] >= 90:
        dic[j] = (dic[j][0], "A")
    elif dic[j][1] >= 80:
        dic[j] = (dic[j][0], "B")
    elif dic[j][1] >= 70:
        dic[j] = (dic[j][0], "C")
    elif dic[j][1] >= 60:
        dic[j] = (dic[j][0], "D")
    else:
        dic[j] = (dic[j][0], "F")
    print(f"{dic[j][0]} {dic[j][1]}")