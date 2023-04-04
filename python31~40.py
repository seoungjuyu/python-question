# 31 (문자열 합치기)

a = "3"
b = "4"
print(a + b)  #34

# 32 (문자열 곱하기)

# 실행 결과를 예상해보기
print("Hi" * 3)    #HiHiHi

# 33 (문자열 곱하기)

# - 를 80개 출력
print("-" * 80)  #--------------------------------------------------------------------------------

# 34 (문자열 곱하기)

# 문자열 + 문자열 곱하기 출력
t1 = 'python'
t2 = 'java'
p = t1 + ' ' + t2 + ' '

print(p * 4) #python java python java python java python java

# 35

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 36
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름 : {}, 나이 : {}".format(name1, age1))
print("이름 : {} 나이 : {}".format(name2, age2))
# 37
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print(f'이름 : {name1}, 나이: {age1}')
print(f'이름 : {name2}, 나이: {age2}')



# f-string -> 문자열 앞에 f가 붙은 형태,
# f-string을 사용하면 '{변수}'와 같은 형태로 문자열 사이에 타입과 상관없이 값을 출력가능


# 38 
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",", "")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))

#39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

#40
data = "   삼성전자    "
data1 = data.strip()
print(data1)