def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
    while True:
        remove_count = 0
        remove_mask = set()
        for y in range(m - 1):
            for x in range(n - 1):
                target = board[y][x]
                if target and target == board[y][x + 1] == board[y + 1][x] == board[y + 1][x + 1]:
                    remove_mask.add((x, y))
                    remove_mask.add((x+1, y))
                    remove_mask.add((x, y+1))
                    remove_mask.add((x+1, y+1))

        if not remove_mask:
            break

        for rx, ry in remove_mask:
            board[ry][rx] = ''
            remove_count += 1

        for x in range(n):
            stack = [board[y][x] for y in range(m) if board[y][x]]
            for y in range(m-1, -1, -1):
                board[y][x] = stack.pop() if stack else ''
        answer += remove_count
    return answer

# from collections import deque
#
# check_pos = [[1, 0], [0, 1], [1, 1]]
#
#
# def check_block(m, n, board, x, y, c):
#     for dx, dy in check_pos:
#         nx, ny = x + dx, y + dy
#         if not (0 <= nx < n and 0 <= ny < m):
#             return False
#         if board[ny][nx] != c:
#             return False
#     return True
#
#
# def remove_block(m, n, board):
#     remove_pos = list()
#     visited = [[False] * n for _ in range(m)]
#     queue = deque()
#     for y in range(m):
#         for x in range(n):
#             if not visited[y][x]:
#                 word = board[y][x]
#                 if word == '':
#                     continue
#                 if check_block(m, n, board, x, y, word):
#                     queue.append((x, y))
#                 while queue:
#                     tx, ty = queue.popleft()
#                     visited[ty][tx] = True
#                     board[ty][tx] = ''
#                     if check_block(m, n, board, tx, ty, word):
#                         if (tx, ty) not in remove_pos:
#                             remove_pos.append((tx, ty))
#                         for dx, dy in check_pos:
#                             nx, ny = tx + dx, ty + dy
#                             queue.append((nx, ny))
#                             if (nx, ny) not in remove_pos:
#                                 remove_pos.append((nx, ny))
#     return len(remove_pos)
#
#
# def relocation_board(m, n, board):
#     tmp_board = list()
#     for i in range(n):
#         tmp_board.append(['' if c == '0' else c for c in ''.join([b[i] for b in board]).rjust(m, '0')])
#     new_board = list()
#     for i in range(m):
#         new_board.append([b[i] for b in tmp_board])
#     return new_board
#
#
# def solution(m, n, board):
#     answer = 0
#     board = [list(line) for line in board]
#     while True:
#         if not (remove_count := remove_block(m, n, board)):
#             break
#         answer += remove_count
#         board = relocation_board(m, n, board)
#     return answer
