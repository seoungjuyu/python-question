#end=
#print문을 이용해 출력을 완료한 뒤 내용을 수정할수 있고, 개행을 없애거나 원하는 문자를 입력할 수 있음

print("1-1","1-2","1-3", end="")   #기본print문

print("1-1","1-2","1-3", end="입니다") #문구를 넣었을때

#sep=
#print문을 이용해 출력문들 사이에 해당하는 애용을 넣을 수 있음, 기본 값으로는 공백 <- 이를 사용해 원하는 문자를 입력

print("1-1", "1-2", "1-3", sep="") #기본 print문

print("1-1", "1-2", "1-3", sep="**이고**") #문구를 넣었을때