"""
# 시도 2.

"""

# TODO: https://peanut159357.tistory.com/77
def minimum_edit_distance(a, b):
    return

# """
# # 시도 1. 최소 편집 거리 알고리즘. 방법을 찾지 못 했고, 다른 사람 풀이 방식 참고
# ## 고민
#   - 연산 3개, 최대 1000자이기 때문에 DFS 안됨. 3^1000
# """
#
# def minimum_edit_distance(a, b):
#     answer = 0
#     len_a = len(a)
#     len_b = len(b)
#     edit_table = [[0] * (len_a + 1) for _ in range(len_b + 1)]
#
#     for c in range(1, len_a + 1):
#         edit_table[0][c] = c
#     for r in range(1, len_b + 1):
#         edit_table[r][0] = r
#
#     for r in range(1, len_b + 1):
#         for c in range(1, len_a + 1):
#             if a[c-1] == b[r-1]:
#                 edit_table[r][c] = edit_table[r-1][c-1]
#             else:
#                 edit_table[r][c] = min(edit_table[r-1][c], edit_table[r-1][c-1], edit_table[r][c-1]) + 1
#     return edit_table[-1][-1]
#
#
if __name__ == '__main__':
    print(minimum_edit_distance(input(), input()))
