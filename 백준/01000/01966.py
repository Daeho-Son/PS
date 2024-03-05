from collections import deque


tc = int(input())
for _ in range(tc):
    n, m = list(map(int, input().split()))
    indices = [i for i in range(n)]
    priorities = list(map(int, input().split()))
    sorted_priorities = sorted(priorities)
    priority_index = deque([(p, i) for p, i in zip(priorities, indices)])
    print_order = 0
    while priority_index:
        target = priority_index.popleft()
        priority, index = target
        if priority == sorted_priorities[-1]:
            sorted_priorities.pop()
            print_order += 1
            if index == m:
                break
        else:
            priority_index.append(target)
    print(print_order)


# import heapq
# from collections import deque
#
# tc = int(input())
# for _ in range(tc):
#     n, m = list(map(int, input().split()))
#     indices = [i for i in range(n)]
#     priorities = list(map(int, input().split()))
#     heap = []
#     priority_index = deque()
#     for index, priority in zip(indices, priorities):
#         priority_index.append((priority, index))
#         heapq.heappush(heap, (-priority, (priority, index)))
#     print_order = 1
#     while priority_index:
#         max_index_priority = heapq.heappop(heap)[1]
#         max_priority = max_index_priority[0]
#         target = priority_index.popleft()
#         target_priority = target[0]
#         if target_priority == max_priority:
#             if target[1] == m:
#                 break
#             print_order += 1
#         else:
#             max_priority = max_index_priority[0]
#             heapq.heappush(heap, (-max_priority, max_index_priority))
#             priority_index.append(target)
#     print(print_order)