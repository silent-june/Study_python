numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number + 2) % 3].append(number)

print(output)

#1 > number = 1
#2 > output[0].append(1) #output이라는 리스트의 0번째 자리에 1을 추가
#3 > number = 2
#4 > output[1].append(2) #output이라는 리스트의 1번째 자리에 2를 추가
#5 > number = 3
#6 > output[2].append(3) #output이라는 리스트의 2번째 자리에 3을 추가
#7 > number = 4
#8 > output[0].append(4) #output이라는 리스트의 0번째 자리에 4를 추가
#9 > number = 5
#10 > output[1].append(5) #output이라는 리스트의 1번째 자리에 5를 추가
#11 > number = 6 
#12 > output[2].append(6) #output이라는 리스트의 2번째 자리에 6을 추가
#13 > number = 7
#14 > output[0].append(7) #output이라는 리스트의 0번째 자리에 7을 추가
#15 > number = 8
#16 > output[1].append(8) #output이라는 리스트의 1번째 자리에 8을 추가
#17 > number = 9
#18 > output[2].append(9) #output이라는 리스트의 2번째 자리에 9를 추가