# 리스트의 원소에 대해 제곱
nums = [1, 2, 3, 4, 5]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)

# 리스트 내포를 이용한 제곱
nums = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in nums]
print(squares)

# 리스트에서 조건에 맞는 원소만 제곱
nums = [1, 2, 3, 4, 5]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)
