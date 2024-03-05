# 다른 사람 풀이
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])


# def solution(lines):
#     answer = 0
#     start = min([start for start, _ in lines])
#     end = max([end for start, end in lines])
#     for i in range(start, end):
#         line_count = 0
#         for s_l, e_l in lines:
#             if s_l <= i and i+1 <= e_l:
#                 line_count += 1
#         if line_count >= 2:
#             answer += 1
#     return answer
#
