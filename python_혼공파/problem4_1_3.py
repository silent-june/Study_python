numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number // 100 >= 1:
        print(number, "는 3 자릿수입니다")
    elif number // 10 >= 1:
        print(number, "는 2 자릿수입니다")
    else:
        print(number, "는 1 자릿수입니다")
    

#답안지
#numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

#for number in numbers:
#   print(number, "는", len(str(number)), "자릿수입니다.")
