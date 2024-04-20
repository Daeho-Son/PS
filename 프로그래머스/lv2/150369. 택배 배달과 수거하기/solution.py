"""
# 시도 2. (성공) 다른 사람 풀이를 이해하고 구현
"""
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveriy_count = 0
    pickup_count = 0
    for i in range(n - 1, -1, - 1):
        deliveriy_count += deliveries[i]
        pickup_count += pickups[i]
        while deliveriy_count > 0 or pickup_count > 0:
            deliveriy_count -= cap
            pickup_count -= cap
            answer += (i + 1) * 2
    return answer


# """
# # 시도 1. (실패) 시간 초과
# ## 방법
#   - 맨 뒷 집부터 delivery, pickup의 개수를 세면서 거리를 줄인다.
# """
# def solution(cap, n, deliveries, pickups):
#     answer = 0
#
#     houses = [[0, 0]]
#     for house in zip(deliveries, pickups):
#         houses.append(list(house))
#     distance = n
#     while distance:
#         delivery_count = 0
#         pickup_count = 0
#         while houses and houses[-1] == [0, 0]:
#             houses.pop()
#             distance -= 1
#         if not houses:
#             break
#         for i in range(distance, 0, -1):
#             if delivery_count == cap and pickup_count == cap:
#                 break
#             if houses[i][0] and houses[i][0] >= cap - delivery_count:
#                 houses[i][0] -= cap - delivery_count
#                 delivery_count = cap
#             else:
#                 delivery_count += houses[i][0]
#                 houses[i][0] = 0
#             if houses[i][1] and houses[i][1] >= cap - pickup_count:
#                 houses[i][1] -= cap - pickup_count
#                 pickup_count = cap
#             else:
#                 pickup_count += houses[i][1]
#                 houses[i][1] = 0
#         answer += (distance * 2)
#     return answer
