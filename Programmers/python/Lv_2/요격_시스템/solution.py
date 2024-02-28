"""
# 시도 3.
- 마지막에 발사한 미사일의 위치를 기억하고 겹치는 부분이면 패스
## 풀이
  1. e를 기준으로 정렬
  2. s가 마지막에 발사한 위치보다 작거나 같으면 겹치는 부분이므로 패스
  3. 겹치지 않는 경우, 마지막 미사일의 위치를 업데이트하고, answer를 증가
## 결과
  - (통과)
"""
def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    last_missile = -1
    for s, e in targets:
        if last_missile >= s + 0.1:
            continue
        last_missile = e - 0.1
        answer += 1
    return answer

# """
# # 시도 2.
# - 요격 미사일의 최솟값을 찾는 방법 변경
# ## 풀이
#   1. e를 기준으로 정렬
#   2. 다른 미사일의 s + 0.1이 e - 0.1 보다 작거나 같으면 포함되므로 체크
#
# ## 결과
#   - 테스트 6, 7, 8: (실패) 시간 초과
# """
# def solution(targets):
#     answer = 0
#     targets.sort(key=lambda x: x[1])
#     target_count = len(targets)
#     visited = [False] * target_count
#     for i in range(target_count):
#         s, e = targets[i]
#         if visited[i]:
#             continue
#         answer += 1
#         for next_i in range(i + 1, target_count):
#             next_s, next_e = targets[next_i]
#             if visited[next_i]:
#                 continue
#             if e - 0.1 >= next_s + 0.1:
#                 visited[next_i] = True
#     return answer

# """
# # 시도 1. (실패)
# - 효율적인 방법이 생각나지 않기 때문에 시간복잡도 신경쓰지 말고 풀어보자
#
# - 방법
#     1. 범위가 좁은 순으로 정렬
#     2. for 문을 돌면서 s, e가 포함 되면 answer를 증가. (이미 체크한 미사일은 무시)
#
# - 결과
#     - 테스트 4, 5: (실패)
#     - 테스트 6, 7, 8: (실패) 시간 초과
# """
# def solution(targets):
#     answer = 0
#     visited = [False] * len(targets)
#     targets.sort(key=lambda x: x[1] - x[0])
#     target_count = len(targets)
#     for i in range(target_count):
#         s, e = targets[i]
#         if not 0 <= s < e <= 100000000:
#             continue
#         if visited[i]:
#             continue
#         visited[i] = True
#         answer += 1
#         for next_i in range(i+1, target_count):
#             next_s, next_e = targets[next_i]
#             if visited[next_i]:
#                 continue
#             if next_s <= s < next_e:
#                 visited[next_i] = True
#             if next_s <= s and e <= next_e:
#                 visited[next_i] = True
#             if next_s < e <= next_e:
#                 visited[next_i] = True
#             if s <= next_s and next_e <= e:
#                 visited[next_i] = True
#     return answer
