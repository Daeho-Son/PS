"""
# 시도 3. 성공
## 방법:
  - 시도 2에서 예외 케이스가 발생해서 수정
  - 주기만 하는 정점 중 다른 정점으로 가장 많이 연결된 정점이 생성된 정점
"""
from enum import Enum


class GraphType(Enum):
    DOUGHNUT = 1
    STICK = 2
    FIGURE_OF_EIGHT = 3


def get_graph_type(edge_frequency, start_edge):
    queue = [start_edge]
    linked_edges = set()
    linked_count = -1
    while queue:
        from_edge = queue.pop()
        linked_edges.add(from_edge)
        linked_count += 1
        if from_edge in edge_frequency.keys():
            queue.extend(edge_frequency.get(from_edge))
            edge_frequency.pop(from_edge)
    edge_count = len(linked_edges)
    if edge_count == linked_count:
        return GraphType.DOUGHNUT.value
    if edge_count == linked_count + 1:
        return GraphType.STICK.value
    if edge_count == linked_count - 1:
        return GraphType.FIGURE_OF_EIGHT.value
    return 0

def solution(edges):
    answer = [0, 0, 0, 0]
    all_edges = set()
    edges_from = dict()
    edges_to = dict()
    for from_edge, to_edge in edges:
        all_edges.add(from_edge)
        all_edges.add(to_edge)
        edges_from.setdefault(from_edge, []).append(to_edge)
        edges_to.setdefault(to_edge, []).append(from_edge)
    answer[0] = max(list(all_edges - set(edges_to.keys())), key=lambda x: len(edges_from.get(x)))
    for start_edge in edges_from.pop(answer[0]):
        graph_type = get_graph_type(edges_from, start_edge)
        answer[graph_type] += 1
    return answer

"""
# 시도 2. 성공
## 방법: 가장 많이 연결된 정점을 생성된 정점이라고 판단하고, dict를 돌면서 연결된 정점을 찾는다.
  1. dict에 연결된 정점을 저장한다.
    - key는 a번 정점, value는 a번 정점과 연결된 b번 정점의 리스트
  2. 가장 많이 연결된 점점을 찾는다.
  3. while을 돌면서 연결된 정점을 찾고 중복되지 않게 set()에 저장, 연결된 간선의 길이를 증가시킨다.
  4. 정점의 개수와 연결된 간선의 개수로 그래프를 판단한다.
"""
# from enum import Enum
#
# class GraphType(Enum):
#     DOUGHNUT = 1
#     STICK = 2
#     FIGURE_OF_EIGHT = 3
#
#
# def get_graph_type(edge_frequency, start_edge):
#     queue = [start_edge]
#     linked_edges = set()
#     linked_count = -1
#     while queue:
#         from_edge = queue.pop()
#         linked_edges.add(from_edge)
#         linked_count += 1
#         if from_edge in edge_frequency.keys():
#             queue.extend(edge_frequency.get(from_edge))
#             edge_frequency.pop(from_edge)
#     edge_count = len(linked_edges)
#     if edge_count == linked_count:
#         return GraphType.DOUGHNUT.value
#     if edge_count == linked_count + 1:
#         return GraphType.STICK.value
#     if edge_count == linked_count - 1:
#         return GraphType.FIGURE_OF_EIGHT.value
#     return 0
#
# def solution(edges):
#     answer = [0, 0, 0, 0]
#     edge_frequency = dict()
#     for from_edge, to_edge in edges:
#         edge_frequency.setdefault(from_edge, []).append(to_edge)
#         # edge_frequency.setdefault(to_edge, []).append(from_edge)
#     created_edge = max(edge_frequency.items(), key=lambda x: len(x[1]))[0]
#     answer[0] = created_edge
#     for start_edge in edge_frequency.get(created_edge):
#         graph_type = get_graph_type(edge_frequency, start_edge)
#         answer[graph_type] += 1
#     return answer


# """
# # 시도 1. (실패) 시간 초과
# ## 방법: 생성된 정점을 찾고, DFS/BFS 탐색
#   1. 주어진 정점들(edges)을 순회하면서 시작 정점의 횟수가 가장 높은 정점을 찾는다.
#   2. DFS/BFS 탐색을 하면서 정점의 개수와 간선의 개수를 구한다.
#   3. 조건에 따라 그래프 타입을 반환한다.
# """
# from collections import deque
# from enum import Enum
#
# class GraphType(Enum):
#     DOUGHNUT = 1
#     STICK = 2
#     FIGURE_OF_EIGHT = 3
#
#
# def get_graph_type(edges, visited, start_edge):
#     dq = deque([start_edge])
#     edge_numbers = {start_edge}
#     line_count = 0
#     count = 0
#     while dq:
#         count += 1
#         target_edge = dq.pop()
#         for index, (from_edge, to_edge) in enumerate(edges):
#             if visited[index] or target_edge not in [from_edge, to_edge]:
#                 continue
#             if target_edge == to_edge:
#                 dq.appendleft(from_edge)
#                 edge_numbers.add(from_edge)
#             elif target_edge == from_edge:
#                 dq.append(to_edge)
#                 edge_numbers.add(to_edge)
#             visited[index] = True
#             line_count += 1
#     edge_count = len(edge_numbers)
#     if edge_count == line_count:
#         return GraphType.DOUGHNUT.value
#     if edge_count == line_count + 1:
#         return GraphType.STICK.value
#     if edge_count == line_count - 1:
#         return GraphType.FIGURE_OF_EIGHT.value
#
#
# def solution(edges):
#     answer = [0, 0, 0, 0]
#     visited = [False] * len(edges)
#     edge_frequency = dict()
#     for from_edge, to_edge in edges:
#         edge_frequency[from_edge] = edge_frequency.get(from_edge, 0) + 1
#     answer[0] = max(edge_frequency.items(), key=lambda x: x[1])[0]
#     for index, (from_edge, to_edge) in enumerate(edges):
#         if visited[index]:
#             continue
#         if from_edge == answer[0]:
#             visited[index] = True
#             graph_type = get_graph_type(edges, visited, to_edge)
#             answer[graph_type] += 1
#     return answer
