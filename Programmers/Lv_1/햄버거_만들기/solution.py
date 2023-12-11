# 시도 3 - 통과
def solution(ingredient):
    answer = 0
    stack = list()
    for n in ingredient:
        stack.append(n)
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                stack.pop()
    return answer


# # 시도 2 - 테스트 5 시간 초과
# def solution(ingredient):
#     answer = 0
#     stack = list()
#     for n in ingredient:
#         stack.append(n)
#         if stack[-4:] == [1, 2, 3, 1]:
#             answer += 1
#             stack = stack[:-4]
#     return answer

# # 시도 1 - 시간 초과
# def solution(ingredient):
#     answer = 0
#     index = 0
#     while index < len(ingredient) - 3:
#         if ingredient[index:index+4] == [1, 2, 3, 1]:
#             ingredient = ingredient[:index] + ingredient[index+4:]
#             index = 0
#             answer += 1
#         else:
#             index += 1
#
#     return answer
