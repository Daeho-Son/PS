"""
# 시도 3. 크루스칼 알고리즘 + Union-Find 알고리즘
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
# # 시도 2. 크루스칼 알고리즘
# """
# def solution(n, costs):
#     answer = 0
#     costs.sort(key=lambda x: (x[2], x[0], x[1]))
#     node_set = set()
#     print(costs)
#     for (_from, _to, _cost) in costs:
#         print(node_set)
#         if { _from, _to } - node_set:
#             node_set.update([_from, _to])
#             answer += _cost
#     return answer



# """
# # 시도 1. (실패) 벨만 포드 알고리즘
# ## 문제점
#   - 벨만 포드 알고리즘은 특정 노드에서 다른 노드까지의 최소 거리를 구하는 알고리즘이므로 실패
# """
# import math
#
#
# def solution(n, costs):
#     answer = 0
#     island_indexes = [i for i in range(n)]
#     recieve_to_connection = dict(zip(island_indexes, [i for i in range(n)]))
#     island_scores = dict(zip(island_indexes, [math.inf if i != 0 else 0 for i in range(n)]))
#     costs.sort(key=lambda x: (x[0], x[1]))
#     while True:
#         is_changed = False
#         for i, (_from, _to, _cost) in enumerate(costs):
#             if island_scores.get(_from) < island_scores.get(_to):
#                 start = _from
#                 end = _to
#             else:
#                 start = _to
#                 end = _from
#             if island_scores.get(start) + _cost < island_scores.get(end):
#                 island_scores[end] = island_scores.get(start) + _cost
#                 recieve_to_connection[end] = start
#                 is_changed = True
#         if not is_changed:
#             break
#     for (_from, _to, _cost) in costs:
#         if recieve_to_connection.get(_to) == _from or recieve_to_connection.get(_from) == _to:
#             answer += _cost
#     return answer