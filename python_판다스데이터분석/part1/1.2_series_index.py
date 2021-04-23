# -*- coding: utf-8 -*-

import pandas as pd

# 리스트를 시리즈로 변환하여 변수 sr에 저장
list_data = ["2019-01-02", 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

# 결과값을 보면 dtype이 object로 나오는데, 데이터값 중 하나라도 object면 object로 출력되는듯!

# 인덱스 배열은 변수 idx에 저장. 데이터 값 배열은 변수 val에 저장
idx = sr.index # 시리즈sr 의 인덱스 저장
val = sr.values # 시리즈sr 의 데이터값 저장
print(idx) # 인덱스 이름을 가진 것이 아니기 때문에 0부터 5까지 존재한다고만 출력됨
print('\n')
print(val)
