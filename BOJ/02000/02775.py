# 0층 1호부터 시작
# 0층 i호에는 i명이 산다
# k층 n호에는 몇 명?
def solution(k, n):
    board = [[i for i in range(n + 1)]]
    board.extend([[0] * (n + 1) for _ in range(k)])
    for y in range(1, k+1):
        for x in range(1, n+1):
            board[y][x] = board[y-1][x] + board[y][x-1]
    return board[k][n]


def main():
    test_case = int(input())
    for t in range(test_case):
        k = int(input())
        n = int(input())
        answer = solution(k, n)
        print(answer)


if __name__ == '__main__':
    main()
