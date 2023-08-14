def solution(numbers):
    stack = list()
    answer = [-1] * len(numbers)
    for i, n in enumerate(numbers):
        while stack and numbers[stack[-1]] < n:
            answer[stack.pop()] = n
        stack.append(i)
    return answer



# 실패. 시간초과
# def solution(numbers):
#     answer = list()
#     for i, n in enumerate(numbers):
#         bigger_ns = list(filter(lambda x: x > n, numbers[i+1:]))
#         if not bigger_ns:
#             answer.append(-1)
#         else:
#             answer.append(bigger_ns[0])
#     return answer
