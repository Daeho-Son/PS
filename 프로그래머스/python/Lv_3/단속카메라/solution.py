# 풀이 2
def solution(routes):
    answer = 0
    camera = -30001
    routes.sort(key=lambda x: x[1])
    for entry_point, exit_point in routes:
        if camera < entry_point:
            camera = exit_point
            answer += 1
    return answer

# 풀이 1
# def solution(routes):
#     answer = 0
#     routes.sort(key=lambda x: x[1])
#     checked = [False] * len(routes)
#     for i in range(len(routes)):
#         if checked[i]:
#             continue
#         camera = -1
#         if not checked[i]:
#             camera = routes[i][1]
#             answer += 1
#         for j in range(i + 1, len(routes)):
#             if routes[j][0] <= camera <= routes[j][1] and not checked[j]:
#                 checked[j] = True
#     return answer
