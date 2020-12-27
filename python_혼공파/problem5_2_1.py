def flatten(data):
    output = []
    for item in data:
        if type(item) == list: # 계속해서 변하는 값에는 is를 사용할 수 없음..!
            output += flatten(item)
        else:
            output.append(item)
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))
