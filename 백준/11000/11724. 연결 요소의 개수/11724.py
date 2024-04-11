"""
# 시도 2. (성공) BFS, 인접 리스트
## 방법
  -
"""
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def bfs(adjacency_edges, edges, start):
    queue = {start}
    while queue:
        t = queue.pop()
        if adjacency_edges.get(t):
            queue.update(adjacency_edges.get(t))
            edges -= set(adjacency_edges.get(t))
            adjacency_edges.pop(t)


def main():
    answer = 0
    n, m = map(int, input().split())
    adjacency_edges = dict()

    edges = set([i for i in range(1, n + 1)])
    for _ in range(m):
        u, v = map(int, input().split())
        adjacency_edges.setdefault(u, []).append(v)
        adjacency_edges.setdefault(v, []).append(u)

    while edges:
        start = edges.pop()
        if adjacency_edges.get(start):
            bfs(adjacency_edges, edges, start)
        answer += 1
    print(answer)


if __name__ == '__main__':
    main()

# """
# # 시도 1. (실패) DFS
# """
# def dfs(graph, visited, target):
#     dq = [target]
#     while dq:
#         t = dq.pop()
#         for i, (u, v) in enumerate(graph):
#             if visited[i]:
#                 continue
#             if t == u:
#                 dq.append(v)
#                 visited[i] = True
#
#
# def main():
#     answer = 0
#     n, m = map(int, input().split())
#     graph = []
#     for _ in range(m):
#         graph.append(list(map(int, input().split())))
#     visited = [False for _ in range(m)]
#     for i, (u, v) in enumerate(graph):
#         if visited[i]:
#             continue
#         answer += 1
#         visited[i] = True
#         dfs(graph, visited, v)
#     print(answer)
#
#
# if __name__ == '__main__':
#     main()
