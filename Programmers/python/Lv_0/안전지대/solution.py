def solution(board):
    n = len(board)
    danger_zone = set()
    for y in range(n):
        for x in range(n):
            if board[y][x] == 0:
                continue
            danger_zone.update((x + d_x, y + d_y) for d_x in [-1, 0, 1] for d_y in [-1, 0, 1])
    return n * n - sum([1 for x, y in danger_zone if 0 <= x < n and 0 <= y < n])

# moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
#
#
# def is_danger_zone(board, current_x, current_y):
#     for move in moves:
#         move_x, move_y = move
#         move_x += current_x
#         move_y += current_y
#         if not (0 <= move_x < len(board) and 0 <= move_y < len(board)):
#             continue
#         if board[current_y][current_x] != 1 and board[move_y][move_x] == 1:
#             return True
#     return False
#
#
# def solution(board):
#     board_size = len(board)
#     for y in range(board_size):
#         for x in range(board_size):
#             if is_danger_zone(board, x, y):
#                 board[y][x] = 2
#     answer = 0
#     for line in board:
#         answer += line.count(0)
#     return answer
