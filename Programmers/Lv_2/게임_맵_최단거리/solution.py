# BFS. 성공
from collections import deque

moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def is_valid_pos(maps, height, width, pos_x, pos_y):
    if not (0 <= pos_x < width and 0 <= pos_y < height):
        return False
    if maps[pos_y][pos_x] == 0:
        return False
    return True


def bfs(maps, height, width, visited):
    queue = deque([[0, 0]])
    while queue:
        current_x, current_y = queue.popleft()
        if [current_x, current_y] == [width - 1, height - 1]:
            break
        for m in moves:
            move_x, move_y = m
            target_x = current_x + move_x
            target_y = current_y + move_y
            if is_valid_pos(maps, height, width, target_x, target_y) and not visited[target_y][target_x]:
                visited[target_y][target_x] = True
                queue.append([target_x, target_y])
                maps[target_y][target_x] = maps[current_y][current_x] + 1
    answer = maps[height - 1][width - 1]
    return -1 if answer == 1 else answer


def solution(maps):
    height = len(maps)
    width = len(maps[0])
    visited = [[False] * width for _ in maps]
    answer = bfs(maps, height, width, visited)
    return answer


# DFS - 재귀. 실패. 효율성 테스트: 시간초과
# answer = -1
# move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# height = 0
# width = 0
#
#
# def is_valid_pos(maps, pos_x, pos_y):
#     if not (0 <= pos_x < width and 0 <= pos_y < height):
#         return False
#     if maps[pos_y][pos_x] == 0:
#         return False
#     return True
#
#
# def dfs(maps, current_x, current_y, visited, move_count):
#     global answer
#     if [current_x, current_y] == [width - 1, height - 1]:
#         answer = move_count if answer == -1 else min(answer, move_count)
#         return
#
#     for move_x, move_y in move:
#         target_x = current_x + move_x
#         target_y = current_y + move_y
#         if is_valid_pos(maps, target_x, target_y) and not visited[target_y][target_x]:
#             visited[current_y][current_x] = True
#             dfs(maps, target_x, target_y, visited, move_count + 1)
#             visited[current_y][current_x] = False
#
#
# def solution(maps):
#     global answer, height, width
#
#     answer = -1
#     height = len(maps)
#     width = len(maps[0])
#     visited = list()
#     for line in maps:
#         visited.append(list(map(lambda x: True if not x else False, line)))
#     dfs(maps, 0, 0, visited, 0)
#
#     return -1 if answer == -1 else answer + 1