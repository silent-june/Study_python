# <문제>.sort() 함수와 같은 동작을 하는 sort(List) 함수를 정의하시오. 
# <조건> 기존의 내장 함수 sort()는 사용 금지. 없다고 생각하고 직접 정의해보세요^^~

def sort_made(List):
    small = []
    same = []
    big = []
    if len(List) > 1:
        std = List[0]
        for i in List:
            if i < std:
                small.append(i)
            elif i == std:
                same.append(i)
            elif i > std:
                big.append(i)
        return sort_made(small) + sort_made(same) + sort_made(big)
    else:
        return List

a = [3, 14, 43, 456, 354, 23, 1]

print(sort_made(a))