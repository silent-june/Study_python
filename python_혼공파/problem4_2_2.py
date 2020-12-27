#딕셔너리의 리스트를 선언합니다.
pets = [
    {"name" : "구름", "age" : 5},
    {"name" : "코코", "age" : 3},
    {"name" : "아지", "age" : 1},
    {"name" : "호랑이", "age" : 1}
]

print("# 우리 동네 애완 동물들")
for pet in pets:
    print("{} {}살".format(pet["name"], pet["age"]))

#1 > pet = {"name" : "구름", "age" : 5} #pet이라는 변수는 계속해서 새로운 딕셔너리로 정의됨
#2 > pet["name"] = "구름", pet["age"] = 5
#3 > print("{구름} {5}살")
#4 > pet = {"name" : "코코", "age" : 3}
#5 > pet["name"] = 코코, pet["age"] = 3
#6 > print("{코코} {3}살")
#7 > pet = {"name" : "아지", "age" : 1}
#8 > pet["name"] = "아지", pet["age"] = 1
#9 > print("{아지} {1}살")
#10 > pet = {"name" : "호랑이", "age" : 1}
#11 > pet["name"] = 호랑이, pet["age"] = 1
#12 > print("{호랑이} {1}살")