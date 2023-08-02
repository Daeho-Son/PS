# 시간 초과
# def solution(n, m, section):
#     answer = 0
#     index = 1
#
#     while index <= n:
#         if index in section: // 추측. 이 과정에서 이 중 for 문이 되는 듯
#             index += m
#             answer += 1
#         else:
#             index += 1
#     return answer


def solution(n, m, section):
    answer = 0

    wall = [False] * n
    for s in section:
        wall[s - 1] = True

    index = 0
    while index < n:
        print(index)
        if wall[index]:
            wall[index:index + m] = [False] * m
            index += m
            answer += 1
        else:
            index += 1
    return answer
