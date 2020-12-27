import random

class Cookie :
    count = 0
    def __init__(self,name,health,player):
        self.name = name
        self.health = health
        self.player = player
        self.isDie = False
        print("{} 쿠키가 생성되었습니다.".format(self.name))
        Cookie.count +=1

    def run(self):
        self.health -= 10
        print("{} 쿠키가 달리고 있습니다. 현재 체력 : {}".format(self.name,self.health))

    def potion(self):
        self.health += 20
        print("{} 쿠키가 물약을 먹었습니다. 현재 체력 : {}".format(self.name, self.health))

    def collide(self):
        self.health -= 20
        print("{} 쿠키가 장애물과 충돌했습니다. 현재 체력 : {}".format(self.name, self.health))

    def finishCheck(self):
        if (self.health<=0) :
            print("{} 쿠키가 죽었습니다.".format(self.name))
            result[cnt] += self.player
            self.isDie = True


#오버라이드
class brave(Cookie) :
    def __init__(self,player):
        super(brave,self).__init__("용감한",50,player)

class hero(Cookie) :
    def __init__(self,player) :
        super(hero,self).__init__("히어로",80,player)

class wizard(Cookie) :
    def __init__(self,player):
        super(wizard,self).__init__("마법사",100,player)

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