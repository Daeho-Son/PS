import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    board = [[0] * (n + 1)]
    for column, _ in enumerate(range(n)):
        column += 1
        board.append([0])
        for row, n in enumerate(input().split()):
            row += 1
            board[-1].append(int(n) + board[column][row - 1] + board[column - 1][row] - board[column - 1][row - 1])

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        print(board[x2][y2] - board[x1 - 1][y2] - board[x2][y1 - 1] + board[x1 - 1][y1 - 1])


if __name__ == '__main__':
    main()

# # 통과
# import sys
# input = sys.stdin.readline
#
# def main():
#     nm = input()
#     n, m = map(lambda x: int(x), nm.split())
#     board = []
#     for column, _ in enumerate(range(n)):
#         board.append([])
#         board_line = input()
#         for row, n in enumerate(board_line.split()):
#             n = int(n)
#             if column - 1 >= 0 and row - 1 >= 0:
#                 n -= board[column - 1][row - 1]
#             if column - 1 >= 0:
#                 n += board[column - 1][row]
#             if row - 1 >= 0:
#                 n += board[column][row - 1]
#             board[-1].append(n)
#
#     for _ in range(m):
#         target_sector = input()
#         x1, y1, x2, y2 = map(lambda x: int(x) - 1, target_sector.split())
#         answer = board[x2][y2]
#         if x1 - 1 >= 0 and y1 - 1 >= 0:
#             answer += board[x1 - 1][y1 - 1]
#         if x1 - 1 >= 0:
#             answer -= board[x1 - 1][y2]
#         if y1 - 1 >= 0:
#             answer -= board[x2][y1 - 1]
#         print(answer)


# # 시간 초과
# n, m = map(lambda x: int(x), input().split())
# board = []
# for _ in range(n):
#     board += map(lambda x: int(x), input().split())
# for _ in range(m):
#     answer = 0
#     x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())
#     for l_index in range(x1, x2+1):
#         answer += sum(board[n*l_index+y1: n*l_index+y2+1])
#     print(answer)
