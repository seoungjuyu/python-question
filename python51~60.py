#51
movie = ["닥터 스레인지","스플릿","럭키"]

#52
movie = ["닥터 스레인지","스플릿","럭키"]
movie.append("배트맨")
print(movie)

#53
movie = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie.insert(1,"슈퍼맨")   #list의 'inset(인덱스, 원소)' 특정위치게 값을 끼워넣을수 있음
print(movie)

#54
movie = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie[3]
print(movie)

#55
# del을 이용해서 원소를 삭제할수는 있지만 리스트에서 어떤 값을 삭제하면 남은 값들을 새로 인덱싱이 됨.
movie = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie[2]
del movie[2]  
print(movie)

#56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

#57
nums = [1, 2, 3, 4, 5, 6, 7]
#최대값 max
# nums.index(max(nums))
#최소값 min
# nums.index(max(nums))

print("max: ", max(nums))
print("min: ", min(nums))

#58
nums = [1, 2, 3, 4, 5]
sum_nums = sum(nums)
print(sum_nums)