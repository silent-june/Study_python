print("#if 조건문에 0 넣기")
if 0:
    print("0은 True로 변환됩니다")
else:
    print("0은 False로 변환됩니다")
print()

print("#if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 True로 변환됩니다")
else:
    print("빈 문자열은 False로 변환됩니다")
#그러면 이러한 False값을 사용하는 이유는..? --> 해당 문장을 끝내고 다음 열로 넘어가기 위함? False가 등장하는 순간 해당 조건은 더 이상 의미가 없는 것
