s=list(input())
for i in range(len(s)):
    if s[i] not in "0123456789":
        if s[i]==" ":
            print(" ",end="")
        if 65<=ord(s[i])<=90:
            if ord(s[i]) + 13 > 90:
                print(chr(((ord(s[i])) + 13) - 26), end="")
            else:
                print(chr((ord(s[i])) + 13), end="")

        elif 97<=ord(s[i])<=122:
            if ord(s[i]) + 13 > 122:
                print(chr(((ord(s[i])) + 13) - 26), end="")
            else:
                print(chr((ord(s[i])) + 13), end="")
    else:
        print(s[i],end="")