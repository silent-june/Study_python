# 더하기 싸이클
# N = 0이상 99이하의 정수
# 똑같은 수가 나올 때까지 반복

number = N = int(input("0이상 99이하의 정수를 입력해주세요! "))
cnt = 0

while True:
    cnt += 1
    ten = number // 10
    one = number % 10
    sum = ten + one
    number = (one * 10) + (sum % 10)

    if number == N:
        break
print(cnt)