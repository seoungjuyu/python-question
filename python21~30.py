#21
letters = 'python' #1번쨰 3번쨰 문자를 출력하시오

print(letters[0],letters[2])
#22
license_plate = "24가 2210"

print(license_plate[-4:])
#23
string = "홀짝홀짝홀짝"
print(string[::2])
#24
string = "PYTHON"
print(string[::-1])
#25
phone_number = "010-1111-2222"
new_number = phone_number.replace('-', '')
print(new_number)
#26
phone_number = "010-1111-2222"
new_number = phone_number.replace('-', '')
print(new_number)

#27
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])
#28
lang = 'python'
lang [0] = 'p'
print(lang)

# >>>TypeError: 'str' object does not support item assignment
# 문자열은 수정할 수 없음. 

#29
string = 'abcdfe2a354a32a'
string1 = string.replace('a', 'A')
print(string1)

#30
# replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.

# string = 'abcd'
# string.replace('b', 'B')
#  print(string)

# `abcd`가 그대로 출력 -> 문자열은 변경할 수  없는 자형 이기 때문