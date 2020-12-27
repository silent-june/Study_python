#숫자는 무작위로 입력해도 상관 없습니다.
numbers = [1,2,5,3,5,7,8,6,4,8,9,6,4,2,4,9,5,3,1,3]
counter = {}

for number in numbers:
    #여기서부터 답안
    if number in counter: # counter 안에 number가 존재하는가? --> 여기서의 number는 "키"가 존재하는가임.
                          # 즉, 키와 연결된 값은 상관없이 키만 존재하는지 확인하는 작업
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1


#최종출력
print(counter)

#1 > number = 1
#2 > if 1 in counter = False
#3 > counter[1] = 1
#4 > counter = {1: 1}
#5 > number = 2
#6 > if 2 in counter = False
#7 > counter[2] = 1
#8 > counter = {1: 1, 2: 1}
#9 > number = 5
#10 > if 5 in counter = False
#11 > counter[5] = 1
#12 > counter = {1: 1, 2: 1, 5: 1}
#13 > number = 3
#14 > if 3 in counter = False
#15 > counter[3] = 1
#16 > counter = {1: 1, 2: 1, 5: 1, 3: 1}
#17 > number = 5
#18 > if 5 in counter = True
#19 > counter[5] = counter[5] + 1
#20 > counter = {1: 1, 2: 1, 5: 2, 3: 1}
#21 > number = 7
#22 > if 7 in counter = False
#23 > counter[7] = 1
#24 > counter = {1: 1, 2: 1, 5: 2, 3: 1, 7: 1}
#25 > number = 8
#26 > if 8 in counter = False
#27 > counter[8] = 1
#28 > counter = {1: 1, 2: 1, 5: 2, 3: 1, 7: 1, 8: 1}
#29 > number = 6
#30 > if 6 in counter = False
#31 > counter[6] = 1
#32 > counter = {1: 1, 2: 1, 5: 2, 3: 1, 7: 1, 8: 1, 6: 1}
#33 > number = 4
#34 > if 4 in counter = False
#35 > counter[4] = 1
#36 > counter = {1: 1, 2: 1, 5: 2, 3: 1, 7: 1, 8: 1, 6: 1, 4: 1}
#37 > number = 8
#38 > if 8 in counter = True
#39 > counter[8] = counter[8] + 1
#40 > counter = {1: 1, 2: 1, 5: 2, 3: 1, 7: 1, 8: 2, 6: 1, 4: 1}
#41 > number = 9
#42 > if 9 in counter = False
#43 > counter[9] = 1
#44 > counter = {1: 1, 2: 1, 5: 2, 3: 1, 7: 1, 8: 2, 6: 1, 4: 1, 9: 1}
#45 > number = 6
#46 > if 6 in counter = True
#47 > counter[6] = counter[6] + 1
#48 > counter = {1: 1, 2: 1, 5: 2, 3: 1, 7: 1, 8: 2, 6: 2, 4: 1, 9: 1}
#49 > number = 4
#50 > if 4 in counter = True
#51 > counter[4] = counter[4] + 1
#52 > counter = {1: 1, 2: 1, 5: 2, 3: 1, 7: 1, 8: 2, 6: 2, 4: 2, 9: 1}
#53 > number = 2
#54 > if 2 in counter = True
#55 > counter[2] = counter[2] + 1
#56 > counter = {1: 1, 2: 2, 5: 2, 3: 1, 7: 1, 8: 2, 6: 2, 4: 2, 9: 1}
#57 > number = 4
#58 > if 4 in counter = True
#59 > counter[4] = counter[4] + 1
#60 > counter = {1: 1, 2: 2, 5: 2, 3: 1, 7: 1, 8: 2, 6: 2, 4: 3, 9: 1}
#61 > number = 9
#62 > if 9 in counter = True
#63 > counter[9] = counter[9] + 1
#64 > counter = {1: 1, 2: 2, 5: 2, 3: 1, 7: 1, 8: 2, 6: 2, 4: 3, 9: 2}
#65 > number = 5
#65 > if 5 in counter = True
#66 > counter[5] = counter[5] + 1
#67 > counter = {1: 1, 2: 2, 5: 3, 3: 1, 7: 1, 8: 2, 6: 2, 4: 3, 9: 2}
#68 > number = 3
#69 > if 3 in counter = True
#70 > counter[3] = counter[3] + 1
#71 > counter = {1: 1, 2: 2, 5: 3, 3: 2, 7: 1, 8: 2, 6: 2, 4: 3, 9: 2}
#72 > number = 1
#73 > if 1 in counter = True
#74 > counter[1] = counter[1] + 1
#75 > counter = {1: 2, 2: 2, 5: 3, 3: 2, 7: 1, 8: 2, 6: 2, 4: 3, 9: 2}
#76 > number = 3
#77 > if 3 in counter = True
#78 > counter[3] = counter[3] + 1
#79 > counter = {1: 2, 2: 2, 5: 3, 3: 3, 7: 1, 8: 2, 6: 2, 4: 3, 9: 2}