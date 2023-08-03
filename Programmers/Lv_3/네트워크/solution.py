# BFS
from collections import deque


def bfs(n, computers, computer, visited):
    queue = deque([computer])
    while queue:
        computer = queue.popleft()
        visited[computer] = True
        for connect in range(n):
            if not visited[connect] and computers[computer][connect] == 1:
                queue.append(connect)


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for computer in range(n):
        if not visited[computer]:
            bfs(n, computers, computer, visited)
            answer += 1
    return answer




# DFS
# def dfs(n, computers, computer, visited):
#     visited[computer] = True
#     for connect in range(n):
#         if not visited[connect] and computers[computer][connect] == 1:
#             dfs(n, computers, connect, visited)
#
#
# def solution(n, computers):
#     answer = 0
#     visited = [False] * n
#     for computer in range(n):
#         if not visited[computer]:
#             dfs(n, computers, computer, visited)
#             answer += 1
#     return answer
