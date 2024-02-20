# 시도 1. (정답) BFS
from collections import deque

move = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def is_valid_pos(maps, x, y, x_end, y_end):
    if not 0 <= x <= x_end:
        return False
    if not 0 <= y <= y_end:
        return False
    return True


def is_food(maps, x, y):
    if not '1' <= maps[y][x] <= '9':
        return False
    return True


def search_food(visited, maps, dq, x_end, y_end):
    count = 0
    while dq:
        x, y = dq.popleft()
        count += int(maps[y][x])
        for move_x, move_y in move:
            moved_x = x + move_x
            moved_y = y + move_y
            if not is_valid_pos(maps, moved_x, moved_y, x_end, y_end):
                continue
            if visited[moved_y][moved_x]:
                continue
            visited[moved_y][moved_x] = True
            if not is_food(maps, moved_x, moved_y):
                continue
            dq.append((moved_x, moved_y))
    return count


def solution(maps):
    answer = []
    y_end = len(maps) - 1
    x_end = len(maps[0]) - 1
    visited = [[False] * len(row) for row in maps]
    for y in range(y_end + 1):
        for x in range(x_end + 1):
            if visited[y][x]:
                continue
            visited[y][x] = True
            if not is_food(maps, x, y):
                continue
            dq = deque()
            dq.append((x, y))
            answer.append(search_food(visited, maps, dq, x_end, y_end))
    return sorted(answer) if answer else [-1]
