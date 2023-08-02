answer = 0


def dfs(k, dungeons, count, visited):
    global answer

    if answer == len(dungeons):
        return

    if count > answer:
        answer = count

    for i, d in enumerate(dungeons):
        if not visited[i] and k >= d[0]:
            visited[i] = True
            dfs(k - d[1], dungeons, count + 1, visited)
            visited[i] = False


def solution(k, dungeons):
    visited = [False] * len(dungeons)
    dfs(k, dungeons, 0, visited)
    return answer

# from itertools import permutations
#
#
# def solution(k, dungeons):
#     answer = 0
#     for dungeons_permutations in permutations(dungeons, len(dungeons)):
#         count = 0
#         tmp_k = k
#         for d in dungeons_permutations:
#             need = d[0]
#             use = d[1]
#             if tmp_k < need or tmp_k - use < 0:
#                 break
#             tmp_k -= use
#             count += 1
#         print(dungeons_permutations, count)
#         if count > answer:
#             answer = count
#     return answer
