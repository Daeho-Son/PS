"""
# 시도2. (성공) 메모리 39768KB, 시간 4200ms
## 방법
  - 시도 1에서 했던 dict 대신 heapq만 사용해서 구현
"""
from heapq import heappush, heappop


def solution():
    n, x = map(int, input().split())
    taste = 0
    amount_of_change_taste = []
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            x -= 5000
            taste += a
            heappush(amount_of_change_taste, (-(b - a), b - a))
        else:
            x -= 1000
            taste += b
    while x < 0:
        x += 4000
        taste += heappop(amount_of_change_taste)[1]
    return taste


print(solution())

"""
# 시도 1. (성공) 메모리 46348KB, 시간 4316ms
## 방법
  1. 가격을 신경쓰지 않고 맛이 최대가 될 수 있는 선택을 한다.
    이때, 남은 돈의 변화에 따른 맛의 변화를 저장한다. (change_taste_to_the_amount_money)
  2. 남은 돈이 음수(-)인 경우, 남은 돈이 양수(+)가 될 때까지 맛의 변화가 적은 값을 더한다. 
"""
# from heapq import heappush, heappop
#
# def solution():
#     n, x = map(int, input().split())
#     taste = 0
#     change_taste_to_the_amount_money = dict()
#     for _ in range(n):
#         a, b = map(int, input().split())
#         if a > b:
#             x -= 5000
#             taste += a
#             heappush(change_taste_to_the_amount_money.setdefault(4000, []), (-(b - a), b - a))
#         else:
#             x -= 1000
#             taste += b
#             heappush(change_taste_to_the_amount_money.setdefault(-4000, []), (-(a - b), (a - b)))
#     while x < 0:
#         x += 4000
#         taste += heappop(change_taste_to_the_amount_money[4000])[1]
#     return taste
