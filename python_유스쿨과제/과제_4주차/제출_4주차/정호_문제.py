# 마이리얼트립은 새롭게 호텔 서비스를 런칭하려고 합니다. 이를 위해서는 기본적인 운영 프로그램이 필요한데요. 
# 
# 1) 호텔 상품군을 추가, 삭제하는 기능
# 2) 상품군에 있는 호텔이 현재 예약가능한지 아닌지 확인하는 기능
# 3) 유저가 호텔을 예약하고, 체크아웃하는 기능 
# 
# 조건0. 위의 기능이 하나의 DB[리스트를 활용해주세요]를 바탕으로 서로 상호적으로 작동해야 합니다. 
# 조건1. 클래스 3가지(MyRealTrip, Hotel, User)를 구현해 주세요.
# 조건2. 프로그램 시작 시, 호텔은 5개 정도 가진 상태로 시작해야 합니다. (제주신라호텔, 제주롯데호텔, 라마다 프라자 제주, 엠제이리조트, 신라 스테이 제주)로 넣어주세요.
# 조건3. 어떤 경우든, 에러가 발생할 경우 "문제가 무엇이고, 어떻게 해야 하는지"를 경고문으로 띄워주세요.

class MyRealTrip:
#MyRealtrip 클래스는 add_hotel, remove_hotel 함수가 필수적으로 필요합니다.
#기존에 있는 호텔을 추가(add_hotel)하거나, 없는 호텔을 제거(remove_hotel)하려고 할 때 에러가 아닌 경고문이 떠야 합니다. 

class Hotel:
#Hotel 함수는 is_sold 함수가 필수적으로 필요합니다. 
#is_sold 함수는, 해당 호텔이 예약 불가능한 상태(호텔이 아예 없거나, 예약되었거나)인지 아닌지를 판단해주는 기능입니다.

class User:
#User 함수는 reserve, checkout 함수가 필수적으로 필요합니다. 
#당연히, 예약하고 체크아웃이 안이루어진 호텔은 예약이 불가능한 상태이겠죠?..