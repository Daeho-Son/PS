# DP
def solution(m, n, puddles):
    puddle_map = [[False] * (m + 1) for _ in range(n + 1)]
    for puddle_x, puddle_y in puddles:
        puddle_map[puddle_y][puddle_x] = True
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if y == x == 1:
                continue
            if puddle_map[y][x]:
                continue
            dp[y][x] = dp[y-1][x] + dp[y][x-1]
    return dp[n][m] % 1000000007

# BFS
# from collections import deque
#
# d = [[1, 0], [0, 1]]
#
#
# def bfs(maps, puddles_map, m, n):
#     pos_queue = deque([(0, 0)])
#     while pos_queue:
#         x, y = pos_queue.popleft()
#         if [x, y] == [m - 1, n - 1]:
#             break
#         for dx, dy in d:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < m and 0 <= ny < n and not puddles_map[ny][nx]:
#                 maps[ny][nx] += maps[y][x]
#                 if (nx, ny) not in pos_queue:
#                     pos_queue.append((nx, ny))
#     return maps[n-1][m-1]
#
#
# def solution(m, n, puddles):
#     maps = [[0] * m for _ in range(n)]
#     maps[0][0] = 1
#     puddles_map = [[False] * m for _ in range(n)]
#     for x, y in puddles:
#         puddles_map[y - 1][x - 1] = True
#     answer = bfs(maps, puddles_map, m, n)
#     return answer % 1000000007
