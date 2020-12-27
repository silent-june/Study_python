# 더하기 싸이클
# N = 0이상 99이하의 정수
# 똑같은 수가 나올 때까지 반복

number = N = input("0이상 99이하의 정수를 입력해주세요! ")
cnt = 0

while True:
    if len(number) == 1:
        number = "0" + number
        N = "0" + N
    number = number[-1] + str(int(number[0]) + int(number[-1]))[-1]
    cnt += 1
    if number == N:
        break

print(cnt)