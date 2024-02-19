# 풀이 2. set을 이용해서 풀이
def solution(n, wires):
    answer = n
    for i, [v1, v2] in enumerate(wires):
        visited = [False for _ in range(n)]
        visited[i] = True
        s = {v1}
        for _ in wires:
            for j, wire in enumerate(wires):
                if visited[j]:
                    continue
                if s & set(wire):
                    s.update(wire)
        answer = min(answer, abs(2 * len(s) - n))
    return answer

# 풀이 1. (성공) BFS로 완전  탐색
# from collections import deque
#
#
# def bfs(wires, visited_index, cut_wire):
#     connections_count = 0
#     visited = [True if i == visited_index else False for i in range(len(wires))]
#     sector = deque([cut_wire])
#     while sector:
#         transmission_tower = sector.popleft()
#         connections_count += 1
#         for i, wire in enumerate(wires):
#             if visited[i] or transmission_tower not in wire:
#                 continue
#             visited[i] = True
#             if transmission_tower == wire[0]:
#                 sector.append(wire[1])
#             elif transmission_tower == wire[1]:
#                 sector.append(wire[0])
#     return connections_count
#
#
# def solution(n, wires):
#     answer = n
#     for i, [v1, v2] in enumerate(wires):
#         diff_count = abs(bfs(wires, i, v1) - bfs(wires, i, v2))
#         if answer > diff_count:
#             answer = diff_count
#     return answer
