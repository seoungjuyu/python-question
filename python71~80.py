# https://wikidocs.net/7027 (python tuple)

#71
my_variable = ()
print(type(my_variable))

#72
movie_rank = ('닥터 스트레인지','스플릿', '럭키')

#73
number = (0,1,2,3,4,)
print(number[1])

#74
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

# -> tuple은 원소의 값을 변경할 수 없음

#75
t = 1, 2, 3, 4
#괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작한다.

#76
t = ('a', 'b', 'c')

#77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
lst = list(interest)

print(lst)
