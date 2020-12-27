def mul(*values):
    multiply = 1
    for value in values:
        multiply = multiply * value
    return multiply # 리턴값이 def에 들여쓰기 되어있어야 함!!!!!!!

# 함수를 호출합니다.
print(mul(5, 7, 9, 10))
