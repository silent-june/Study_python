# <문제> 정수를 2개 이상 입력하면, 정수별 팩토리얼값의 총계/평균/최대/최소값을 출력하는 프로그램을 만들어주세요..
# - 조건1. 입력받는 정수는 5 이상 이어야 합니다.
# - 조건2. 정수를 2개 이상 입력받아야 합니다.
# - 조건3. 출력값에는 세자리수마다 콤마(,)를 찍어주세요
# - 조건4. def는 1회만 사용합니다.

# 입력 예시 : 5, 12, 6
# 출력 예시 : 
# 총계 : 479,002,440
# 평균 : 159,667,480
# 최대 : 479,001,600
# 최소 : 120

def factorial(n):
    output = 1
    if n == 0:
        return output
    elif n == 1:
        return output
    elif n >= 2:
        output = n * factorial(n-1)
    return output

integer = list(map(int, input().split(", ")))
list_fac = []
sum_fac = 0

for i in integer:
    list_fac.append(factorial(i))
    sum_fac += factorial(i)
avg_fac = int(sum_fac / len(integer))
max_fac = max(list_fac)
min_fac = min(list_fac)

print("총계 : ", "{:,}".format(sum_fac))
print("평균 : ", "{:,}".format(avg_fac))
print("최대 : ", "{:,}".format(max_fac))
print("최소 : ", "{:,}".format(min_fac))
