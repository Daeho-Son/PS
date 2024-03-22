"""
# 시도 2. (성공)
## 방법: 단순하게 모든 공항을 방문하는 경로를 DFS를 통해 전부 찾고, 알파벳순으로 가장 앞에 있는 경로 반환
  1.
"""
import copy

answer = []


def bfs(tickets, visited, start_index, airport_route):
    visited[start_index] = True
    _, current_airport = tickets[start_index]
    airport_route.append(current_airport)
    for i, (departure, arrival) in enumerate(tickets):
        if not visited[i] and current_airport == departure:
            bfs(tickets, copy.deepcopy(visited), i, copy.deepcopy(airport_route))
    if False not in visited:
        answer.append(airport_route)


def solution(tickets):
    global answer
    answer = []
    for i, (departure, arrival) in enumerate(tickets):
        if departure == 'ICN':
            visited = [False if i != t_i else True for t_i, _ in enumerate(tickets)]
            bfs(tickets, visited, i, ['ICN'])
    return sorted(answer)[0]


# """
# # 시도 1. (실패)
# ## 방법
#   1. tickets의 각 행을 [a, b]라고 할 때, 먼저 a를 기준으로 다음으로 b를 기준으로 tickets를 역순으로 정렬한다.
#   2. tickets를 역순으로 순회한다.
#     - 역순으로 정렬했기 때문에 "ICN"에서 가장 먼저 출발하는 공항은 뒤에 있으므로
#   3. DFS로 앞에서부터 끝까지 탐색하고 반환한다.
#
# """
# from collections import deque
#
# answer = []
#
#
# def bfs(tickets, start_index):
#     global answer
#     visited = [False if i != start_index else True for i, _ in enumerate(tickets)]
#     arrival = tickets[start_index][1]
#     airport_route = ["ICN"]
#     dq = deque([arrival])
#     while dq:
#         target = dq.pop()
#         airport_route.append(target)
#         for i, (departure, arrival) in enumerate(tickets):
#             if not visited[i] and departure == target:
#                 visited[i] = True
#                 dq.append(arrival)
#     return airport_route
#
#
# def solution(tickets):
#     global answer
#     answer = []
#     tickets.sort(key=lambda x: (x[0], x[1]), reverse=True)
#     for i in range(len(tickets) - 1, -1, -1):
#         departure, arrival = tickets[i]
#         if departure == 'ICN':
#             return bfs(tickets, i)
#     return answer
