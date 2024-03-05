# from collections import deque
#
#
# def solution(priorities, location):
#     answer = list()
#     queue = deque(priorities)
#     order = deque(range(len(priorities)))
#     while queue:
#         order_target = order.popleft()
#         target = queue.popleft()
#         if queue and target < max(queue):
#             queue.append(target)
#             order.append(order_target)
#         else:
#             answer.append(order_target)
#     return answer.index(location) + 1


from collections import deque


def solution(priorities, location):
    answer = list()
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    while queue:
        target_tuple = queue.popleft()
        if any(target_tuple[1] < t[1] for t in queue):
            queue.append(target_tuple)
        else:
            answer.append(target_tuple[0])
    return answer.index(location) + 1