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