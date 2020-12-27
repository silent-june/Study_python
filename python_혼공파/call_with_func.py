# 함수를 선언합니다.
def power(item):
    return item * item
def under_3(item):
    return item > 3

# 변수를 선언합니다.
list_input_a = [1, 2, 3, 4, 5]

# map() 함수를 사용합니다.
output_a = map(power, list_input_a) # map(사용할 함수, 그 함수를 적용할 리스트) --> 해당 결과에 맞는 리스트 생성
# map() 함수는 리스트 요소의 개수가 바뀌지 않음!
print(" # map() 함수의 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

# filter() 함수를 사용합니다.
# filter() 함수의 경우 상황에 따라 리스트 요소의 개수가 바뀜!
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))
