# 리스트에 값을 하나씩 더해서 새로운 리스트를 만드는 작업
myList = [1, 2, 3, 4, 5]

# map 함수 이용
result2 = ''.join(map(lambda n: str(n + 1), myList))  # map반환을 list 로 변환
print(f'result2 : {result2}')
