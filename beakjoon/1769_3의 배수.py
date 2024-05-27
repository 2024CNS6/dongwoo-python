n = input()
sum_digits = sum(int(i) for i in n)  # 처음 입력된 숫자들의 합
trys = 1 if len(n) > 1 else 0  # 입력값의 길이에 따라 초기 트라이 횟수를 설정

while sum_digits >= 10:  # sum이 10 이상인 동안 계속 반복
    sum_digits = sum(int(i) for i in str(sum_digits))  # sum을 문자열로 변환한 뒤 각 자릿수 합 계산
    trys += 1

if sum_digits % 3 == 0:
    print(trys)
    print("YES")
else:
    print(trys)
    print("NO")
