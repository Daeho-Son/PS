def solution(board, moves):
    answer = 0
    lines = list()
    for i in range(len(board)):
        lines.append([b[i] for b in board])

    stack = list()
    for move in moves:
        for i, n in enumerate(lines[move-1]):
            if n != 0:
                lines[move-1][i] = 0
                if stack and stack[-1] == n:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(n)
                break
    return answer