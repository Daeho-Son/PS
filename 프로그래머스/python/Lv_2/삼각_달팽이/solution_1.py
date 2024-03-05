from collections import deque


def solution(n):
    answer = []

    front = [[] for _ in range(n)]
    back = [deque([]) for _ in range(n)]
    current_n = 1
    current_index = -1
    for i in range(n):
        for j in range(n - i):
            if i % 3 == 0:
                current_index += 1
                front[current_index].append(current_n)
            elif i % 3 == 1:
                front[current_index].append(current_n)
            else:
                current_index -= 1
                back[current_index].appendleft(current_n)
            current_n += 1
    for i in range(n):
        answer += front[i]
        answer += back[i]
    return answer
