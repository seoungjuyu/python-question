#setattr() 함수구문 -> setattr(객체, 속성, newValue)

#세가지 메개변수가 모두 필요함. setattr()함수는 어떤 값도 반환하지 않거나 None을 반환한다.
#이 함수는 지정된 속성의 새 값을 지정된 개체에만 설정한다.


class TestCodes:
    이름 = "jvely"
    과정 = "음악"
    도서 = "바이엘"
    
ob = TestCodes()
print ("하나의 값 수정")
print ("1. 이름")
print ("2. 과정")
print ("3.도서")
print ("")