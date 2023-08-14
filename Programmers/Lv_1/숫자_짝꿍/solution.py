from collections import Counter


def solution(x, y):
    answer = ''
    x_counter = Counter(x)
    y_counter = Counter(y)
    for i in range(9, -1, -1):
        str_i = str(i)
        answer += (str_i * min(x_counter[str_i], y_counter[str_i]))
    if not answer:
        return "-1"
    if len(answer) == answer.count('0'):
        return "0"
    return answer

# from collections import deque
#
#
# def solution(x, y):
#     answer = ''
#     answer_list = list()
#     queue_x = deque(sorted(x))
#     queue_y = deque(sorted(y))
#
#     while queue_x and queue_y:
#         if queue_x[0] < queue_y[0]:
#             queue_x.popleft()
#         elif queue_x[0] > queue_y[0]:
#             queue_y.popleft()
#         else:
#             answer_list.append(queue_x[0])
#             queue_x.popleft()
#             queue_y.popleft()
#     if not answer_list:
#         return "-1"
#     for n in sorted(answer_list, reverse=True):
#         if answer and answer[0] == '0' and n == '0':
#             continue
#         answer += n
#     return answer
