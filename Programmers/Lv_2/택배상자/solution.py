# 풀이 2
def solution(order):
    answer = 0
    order.reverse()
    storage = list()
    for i in range(1, len(order) + 1):
        storage.append(i)
        while storage and storage[-1] == order[-1]:
            storage.pop()
            order.pop()
            answer += 1
    return answer

# 풀이 1
# def solution(order):
#     answer = 0
#     main_belt = [i for i in range(len(order), 0, -1)]
#     sub_belt = list()
#
#     order.reverse()
#     while order:
#         if not main_belt and not sub_belt:
#             break
#         if not main_belt and sub_belt[-1] != order[-1]:
#             break
#         if main_belt and main_belt[-1] == order[-1]:
#             order.pop()
#             main_belt.pop()
#             answer += 1
#         elif main_belt and main_belt[-1] != order[-1]:
#             sub_belt.append(main_belt.pop())
#         if sub_belt and sub_belt[-1] == order[-1]:
#             order.pop()
#             sub_belt.pop()
#             answer += 1
#     return answer
