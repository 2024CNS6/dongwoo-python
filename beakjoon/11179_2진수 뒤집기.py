ten = int(input())
two = bin(ten)[2:]
two_rv=""
for i in two:
    two_rv=i+two_rv
print(int(two_rv,2))