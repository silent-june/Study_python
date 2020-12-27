# 조건1. 예외 처리가 필요한 곳을 찾아, 3가지의 예외 처리 구문을 코드에 포함해주세요.
# 조건2. 계산기는 덧셈, 뺄셈, 곱셈, 나눗셈을 지원하며 이는 함수를 따로 만들어서 구현해주세요.

#더하기 함수
def add(a,b) :
    name = "더하기"
    result = int(a)+int(b)
    return name,result

#빼기 함수
def sub(a,b) :
    name = "빼기"
    result = int(a)-int(b)
    return name,result

#곱하기 함수
def mul(a,b) :
    name = "곱하기"
    result = int(a)*int(b)
    return name,result

#나누기 함수
def div(a,b) :
    name = "나누기"
    try :
        result = int(a)/int(b)
        return name,result
    except ZeroDivisionError as e :
        return name, None
        print("0으로는 나눌 수 없습니다! ErrorMessage : %s" %e)


try :
    print("아래에서 사칙연산을 선택해주세요!")
    exp = int(input("1.더하기\n2.빼기\n3.곱하기\n4.나누기\n"))
    if(exp > 4 or exp<0) :
        raise Exception('1~4 중에서 선택해주세요.')

    inputA = input("A변수를 입력해주세요. ")
    inputB = input("B변수를 입력해주세요. ")
    print("userInputA :",inputA,", userInputB :",inputB)

except ValueError as e:
    print("숫자를 입력해주세요. ErrorMessage : %s" %e)
    exit()

except Exception as e:
    print("ErrorMessage : %s" %e)
    exit()

if(exp==1) :
    name,res = add(inputA,inputB)
elif (exp==2) :
    name, res = sub(inputA, inputB)
elif (exp==3) :
    name, res = mul(inputA, inputB)
elif (exp==4) :
    name, res = div(inputA, inputB)

print("{} 결과는 {} 입니다".format(name,res))

