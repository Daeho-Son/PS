# BFS
from collections import deque


def is_difference_only_one(word1, word2):
    count = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            count += 1
        if count == 2:
            return False
    return True


def bfs(words, target, queue):
    answer = 0
    visited = [False] * len(words)
    while queue:
        begin, count = queue.popleft()
        if begin == target:
            answer = count
            return answer
        for i, word in enumerate(words):
            if not visited[i] and is_difference_only_one(begin, word):
                queue.append(([word, count + 1]))
                visited[i] = True
    return answer


def solution(begin, target, words):
    queue = deque([(begin, 0)])
    return bfs(words, target, queue)

# DFS
# min_count = 0
#
#
# def is_difference_only_one(word1, word2):
#     count = 0
#     for w1, w2 in zip(word1, word2):
#         if w1 != w2:
#             count += 1
#     return True if count == 1 else False
#
#
# def dfs(words, current_index, target, count, visited):
#     global min_count
#
#     copy_visited = visited.copy()
#     copy_visited[current_index] = True
#     current_word = words[current_index]
#
#     if current_word == target:
#         min_count = min_count if min_count < count else count
#         return
#
#     for i, word in enumerate(words):
#         if not visited[i] and is_difference_only_one(current_word, word):
#             dfs(words, i, target, count + 1, copy_visited)
#
#
# def solution(begin, target, words):
#     global min_count
#
#     min_count = len(words) + 1
#     visited = [False] * len(words)
#     for i, word in enumerate(words):
#         if not visited[i] and is_difference_only_one(begin, word):
#             dfs(words, i, target, 1, visited)
#     return min_count if min_count != len(words) + 1 else 0
