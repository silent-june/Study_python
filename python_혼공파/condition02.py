#입력을 받습니다.
number = input("정수 입력> ")
last_character = number[-1]

#짝수 조건
if last_character in "02486": #in은 str를 글자 별로 쪼개는 것이 가능한 듯
    print("짝수입니다")

#홀수 조건
if last_character in "13579":
    print("홀수입니다")

