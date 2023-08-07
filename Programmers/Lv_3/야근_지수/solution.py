from heapq import heapify, heappush, heappop


def solution(n, works):
    heapify(heap := [-work for work in works])
    for i in range(n):
        heappush(heap, heappop(heap) + 1)
    return sum([num * num for num in heap if num < 0])

# from heapq import heappush, heappop
#
#
# def solution(n, works):
#     heap = list()
#
#     for work in works:
#         heappush(heap, (-work, work))
#     for i in range(n):
#         max_num = heappop(heap)[1] - 1
#         heappush(heap, (-max_num, max_num))
#
#     return sum([num[1] ** 2 for num in heap if num[1] >= 1])


# 시간초과
# def solution(n, works):
#     for i in range(n):
#         max_work = max(works)
#         if max_work == 0:
#             break
#         max_index = works.index(max_work)
#         works[max_index] -= 1
#     return sum(map(lambda x: x ** 2 if x >= 1 else 0, works))
