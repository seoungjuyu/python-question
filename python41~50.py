#41
ticker = "btc_krw"
Upper = ticker.upper() #upper을 사용해서 대문자로 변경
print(Upper)

#42
ticker = "BTC_KRW"
ticker1 = ticker.lower() #lower를 사용해서 소문자로 변경
print(ticker1)

#43
text = 'hello'
text1 = text.capitalize() #capitalize를 사용해 앞'h'를 대문자'H'로 번경
print(text1)

#44
file_name = "보고서.xlsx"
name = file_name.endswith("xlsx") #문자가 맞게끝나는지 확인
print(name)

#45
file_name = "보고서.xlsx"
name1 = file_name.endswith("xls,xlsx") #튜플을 적고 여려패턴을 적어주면 됨
print(name1)