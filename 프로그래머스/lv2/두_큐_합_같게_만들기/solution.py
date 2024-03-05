# 풀이 2
def solution(queue1, queue2):
    answer = 0
    queue = queue1 + queue2
    len_of_queue = len(queue)
    sum_of_queue = sum(queue)
    if sum_of_queue % 2 != 0:
        return -1
    goal_number = sum_of_queue // 2
    start, end = 0, len(queue2) - 1
    sum_of_range = sum(queue1)
    while start < len_of_queue and end < len_of_queue:
        if sum_of_range == goal_number:
            return answer
        if sum_of_range < goal_number and end < len_of_queue - 1:
            end += 1
            sum_of_range += queue[end]
        else:
            sum_of_range -= queue[start]
            start += 1
        answer += 1
    return -1

# 풀이 1
# from collections import deque
#
# def solution(queue1, queue2):
#     answer = 0
#
#     dequeue1 = deque(queue1)
#     dequeue2 = deque(queue2)
#     sum_of_dequeue1 = sum(queue1)
#     sum_of_dequeue2 = sum(queue2)
#     total_sum = sum_of_dequeue1 + sum_of_dequeue2
#
#     if total_sum % 2 != 0:
#         return -1
#     goal_number = total_sum // 2
#     max_operations = len(queue1 + queue2) * 2
#
#     while answer < max_operations:
#         if sum_of_dequeue1 == sum_of_dequeue2:
#             return answer
#         if sum_of_dequeue1 < sum_of_dequeue2:
#             number = dequeue2.popleft()
#             sum_of_dequeue2 -= number
#             dequeue1.append(number)
#             sum_of_dequeue1 += number
#         else:
#             number = dequeue1.popleft()
#             sum_of_dequeue1 -= number
#             dequeue2.append(number)
#             sum_of_dequeue2 += number
#         answer += 1
#
#     return -1
