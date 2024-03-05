from collections import deque


def solution(n):
    front = [[] for _ in range(n)]
    back = [deque([]) for _ in range(n)]
    current_n = 1
    end_n = (n * (n + 1)) // 2
    fill_count = n
    top_index = 0
    bottom_index = n - 1
    while current_n <= end_n:
        for i in range(top_index, bottom_index+1):
            front[i].append(current_n)
            current_n += 1
        top_index += 1
        fill_count -= 1
        for _ in range(fill_count):
            front[bottom_index].append(current_n)
            current_n += 1
        bottom_index -= 1
        fill_count -= 1
        for i in range(bottom_index, top_index - 1, -1):
            back[i].appendleft(current_n)
            current_n += 1
        top_index += 1
        fill_count -= 1

    answer = []
    for i in range(n):
        answer += front[i]
        answer += back[i]
    return answer
