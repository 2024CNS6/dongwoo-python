while 1:
    n=str(input())
    re=''
    if int(n)==0:
        break
    else:
        for i in n:
            re=i+re

        if int(re)==int(n):
            print("yes")
        else:
            print("no")