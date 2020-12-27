# Step 1. Cookie 클래스를 정의하세요. 

# 이 클래스는 앞으로 만들 모든 쿠키 객체의 부모 클래스가 됩니다. 자유롭게 코드를 추가해주세요. 


class Cookie :
    count = 0
    
    #쿠키 초기화
    def __init__(self,name,health,player):
        self.name = name  #쿠키 이름
        self.health = health  #쿠키 체력
        self.player = player  #쿠키 플레이어
        self.isDie = False  #쿠키 죽었는지 체크
        Cookie.count +=1

    def run(self):
    #쿠키는 달릴 때 마다 체력이 10 감소합니다. 
    
    def potion(self):
    #쿠키는 물약을 먹으면 체력이 20 증가합니다.
    
    def collide(self):
    #쿠키는 장애물과 충돌하면 체력이 20 감소합니다. 

    def finishCheck(self):
    #쿠기는 체력이 0이 되면 죽습니다. (이미 완성된 함수입니다. 구현에 참고하세요.)
        if (self.health<=0) :
            print("{} 쿠키가 죽었습니다.".format(self.name))
            result[cnt] += self.player
            self.isDie = True

# Step2.  Cookie class를 상속하는 용감한 쿠키, 히어로맛 쿠키, 마법사맛 쿠키 의 클래스를 구현해봅시다. 


class brave(여기에 뭐가 들어가야 할까요?) :
# 용감한 쿠키 클래스.
# 이름은 "용감한", 체력은 50, 사용자가 입력한 player의 이름을 넣어주세요. 

class hero(여기에 뭐가 들어가야 할까요?) :
# 히어로맛 쿠키 클래스.
# 이름은 "히어로", 체력은 80, 사용자가 입력한 player의 이름을 넣어주세요. 

class wizard(여기에 뭐가 들어가야 할까요?) :
# 히어로맛 쿠키 클래스.
# 이름은 "마법사", 체력은 100, 사용자가 입력한 player의 이름을 넣어주세요. 

# Step3. class 정의가 끝났다면, 아래의 코드를 맨 밑에 붙여넣습니다.
# 
# 난이도 조절을 위해 코드를 통째로 드리지만, 정의한 클래스에 맞게 얼마든지 코드를 수정하셔도 됩니다. 
# 
# 대충 결과만 비슷하게 나오게 해주세요. 


import random

#클래스를 이용해 쿠키 3개 생성
c1 = brave("지훈")
c2 = hero("도영")
c3 = wizard("용준")

result =[]  #게임 결과를 저장하는 배열
cnt = 0
cookie = [c1,c2,c3]     #만들어진 쿠키 객체를 저장하는 배열

#쿠키가 모두 죽을 때까지 반복
while not (c1.isDie and c2.isDie and c3.isDie):
    result.append(" ")
    for i in range(len(cookie)):
        if(not cookie[i].isDie):    #쿠키가 죽지 않았다면 다음을 실행합니다.
            cookie[i].run()     #쿠키가 죽지 않았다면 무조건 달립니다.
            if (random.random() < 0.5):     #쿠키는 50%의 확률로 체력 potion을 획득합니다.
                cookie[i].potion()
            if (random.random() < 0.2):     #쿠키는 20%의 확률로 장애물에 부딪힙니다.
                cookie[i].collide()
            cookie[i].finishCheck()     #마지막으로 쿠키의 체력이 남아있는지 확인합니다.
    cnt +=1

#결과 출력
print("\n<게임 결과>")
prize = Cookie.count
for i in range(len(result)) :
    if(result[i] != " ") :
        print("{}등 : {}".format(prize,result[i]))
        prize -=1