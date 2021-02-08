# -*- coding: utf-8 -*-

# pandas 불러오기
import pandas as pd

# key:value 쌍으로 딕셔너리를 만들고, 변수 dict_data에 저장
# 딕셔너리 key는 숫자로 자동변환이 될 줄 알았는데, key명이 그대로 인덱스로 들어감!!
# 숫자로 자동변환이 아니라, 정수형 위치 인덱스는 항상 존재함! 인덱스 이름을 추가로 정하느냐 마느냐가 optional
dict_data = {"a": 1, "b": 2, "c": 3 }

 # 판다스 Series() 함수로 dictionary를 Series로 변환. 변수 sr에 저장
sr = pd.Series(dict_data)

 # sr의 자료형 출력
print(type(sr))
print('\n')
 # 변수 sr에 저장되어 있는 시리즈 객체를 출력
print(sr)