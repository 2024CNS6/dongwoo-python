for i in range(int(input())):
    two1,two2=input().split()
    print(bin(int(two1,2)+int(two2,2))[2:])