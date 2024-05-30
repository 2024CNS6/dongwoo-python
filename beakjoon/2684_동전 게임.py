n=int(input())
for k in range(n):
    s=input()
    o=len(s)
    HT_list = [0] * 8
    for i in range(o):
        if i < len(s) - 2:
            if s[i:i+3] in ["TTT", "TTH", "THT", "THH", "HTT", "HTH", "HHT","HHH"]:
                n += 1
                o -= 1
                if s[i:i+3]=="TTT":
                    HT_list[0]+=1
                elif s[i:i+3]=="TTH":
                    HT_list[1]+=1
                elif s[i:i+3]=="THT":
                    HT_list[2]+=1
                elif s[i:i+3]=="THH":
                    HT_list[3]+=1
                elif s[i:i+3]=="HTT":
                    HT_list[4]+=1
                elif s[i:i+3]=="HTH":
                    HT_list[5]+=1
                elif s[i:i+3]=="HHT":
                    HT_list[6]+=1
                elif s[i:i+3]=="HHH":
                    HT_list[7]+=1
    print(*HT_list)