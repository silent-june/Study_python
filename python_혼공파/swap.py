a = input("문자열 입력> ")
b = input("문자열 입력> ")

print(a, b)

c = a
a = b
b = c

print(a, b)
#물론 print(b,a)로도 간단하게 바꿀 수 있음