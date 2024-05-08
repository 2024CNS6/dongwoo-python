s=list(input())
sum=0
for i in s:
    if 65<=ord(i)<=67:
        sum+=3
    elif 68<=ord(i)<=70:
        sum+=4
    elif 71<=ord(i)<=73:
        sum+=5
    elif 74<=ord(i)<=76:
        sum+=6
    elif 77<=ord(i)<=79:
        sum+=7
    elif 80<=ord(i)<=83:
        sum+=8
    elif 84<=ord(i)<=86:
        sum+=9
    elif 87<=ord(i)<=90:
        sum+=10
    elif i in " ":
        sum+=2
print(sum)