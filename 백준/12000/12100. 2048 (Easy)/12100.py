import copy
import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def merge(line):
    max_index = n
    while line and line[0] == 0:
        max_index -= 1
        del line[0]
    i = 0
    while line and i < max_index - 1:
        if line[i] == 0:
            del line[i]
            max_index -= 1
            i -= 1
            continue
        if line[i] == line[i + 1]:
            line[i] *= 2
            del line[i + 1]
            max_index -= 1
        i += 1
    return line + [0] * (n - len(line))


def merge_up(new_board):
    for r in range(n):
        line = merge([new_board[c][r] for c in range(n)])
        for c in range(n):
            new_board[c][r] = line[c]
    return new_board


def merge_down(new_board):
    for r in range(n):
        line = merge([new_board[c][r] for c in range(n - 1, -1, -1)])
        for c in range(n - 1, -1, -1):
            new_board[c][r] = line[n - 1 - c]
    return new_board


def merge_left(new_board):
    for c in range(n):
        new_board[c] = merge(new_board[c])
    return new_board


def merge_right(new_board):
    for c in range(n):
        new_board[c] = merge(new_board[c][::-1])[::-1]
    return new_board


def pretty_print_board(b):
    for i in range(n):
        print(b[i])
    print()


def dfs(new_board, moved_count):
    global answer

    if moved_count >= 5:
        for rs in new_board:
            max_n = max(rs)
            answer = max_n if max_n > answer else answer
        return
    dfs(merge_up(copy.deepcopy(new_board)), moved_count + 1)
    dfs(merge_down(copy.deepcopy(new_board)), moved_count + 1)
    dfs(merge_left(copy.deepcopy(new_board)), moved_count + 1)
    dfs(merge_right(copy.deepcopy(new_board)), moved_count + 1)


def main():
    dfs(board, 0)
    print(answer)


if __name__ == '__main__':
    main()
