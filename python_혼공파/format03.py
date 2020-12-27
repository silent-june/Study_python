#기호와 함께 출력하기
output_f = "{:+d}".format(52) #format 안쪽이 양수일 경우 + 추가
output_g = "{:+d}".format(-52) #format 안쪽이 음수여서 변화없음
output_h = "{: d}".format(52) #format 안쪽이 양수일 경우 공백
output_i = "{: d}".format(-52) #format 안쪽이 음수여서 변화없음

print(output_f)
print(output_g)
print(output_h)
print(output_i)
