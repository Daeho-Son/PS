"""
# 구현 2
## 방법
  - Union-Find 알고리즘
  - find 경로 압축
"""

def solution(n, graph):
    total_weight = 0
    graph.sort(key=lambda x: -x[2])
    parents = [i for i in range(n)]
    linked_count = 0

    def find(node):
        if node != parents[node]:
            parents[node] = find(parents[node])
        return parents[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        parents[root2] = root1

    while linked_count != n - 1:
        u, v, weight = graph.pop()
        if find(u) != find(v):
            union(u, v)
            linked_count += 1
            total_weight += weight
    return total_weight





# """
# # 구현 1
# """
# def solution(n, graph):
#     graph.sort(key=lambda x: x[2])
#     u, v, weight = graph.pop(0)
#     node_set = {u, v}
#     total_weight = weight
#     while len(node_set) != n:
#         for (u, v, weight) in graph:
#             if not {u, v} & node_set:
#                 continue
#             if {u, v} - node_set:
#                 node_set.update([u, v])
#                 total_weight += weight
#                 break
#     return total_weight


def main():
    n = 10
    graph = [
        [0, 1, 16],
        [0, 2, 21],
        [0, 4, 19],
        [1, 2, 11],
        [1, 3, 5],
        [1, 5, 6],
        [2, 4, 33],
        [2, 5, 14],
        [3, 5, 10],
        [4, 5, 18]
    ]

    # graph = [
    #     [2, 0, 1],
    #     [3, 0, 1],
    #     [2, 3, 1],
    #     [0, 1, 3],
    #     [1, 3, 2],
    # ]

    # n = 5
    # graph = [
    #     [0, 1, 3],
    #     [0, 2, 1],
    #     [0, 3, 1],
    #     [1, 3, 2],
    #     [2, 4, 1],
    # ]

    # n = 5
    # graph = [
    #     [0, 2, 1],
    #     [0, 3, 1],
    #     [0, 1, 1],
    #     [1, 3, 1],
    #     [2, 4, 1],
    #     [3, 4, 1],
    # ]
    print(solution(n, graph))


if __name__ == '__main__':
    main()
