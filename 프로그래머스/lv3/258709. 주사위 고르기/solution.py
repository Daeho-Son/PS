"""
# 시도 3. (성공) 카카오 문제해설 참고해서 구혀
"""
from itertools import combinations, product
from heapq import heappush, heappop

def solution(dice):
    answer = (0, [0, 0])
    dice_indexes = [i + 1 for i in range(len(dice))]

    for comb in combinations(dice_indexes, len(dice) // 2):
        a_sums = []
        a = [dice[i - 1] for i in comb]
        for p_a in product(*a):
            heappush(a_sums, (-sum(p_a), sum(p_a)))
        b_sums = []
        b = [dice[i-1] for i in set(dice_indexes) - set(comb)]
        for p_b in product(*b):
            heappush(b_sums, (-sum(p_b), sum(p_b)))

        win = 0
        while a_sums and b_sums:
            while b_sums and a_sums[0][1] <= b_sums[0][1]:
                heappop(b_sums)
            if b_sums and a_sums[0][1] > b_sums[0][1]:
                win += len(b_sums)
                heappop(a_sums)
        if win > answer[0]:
            answer = (win, list(comb))
    return answer[1]


# """
# # 시도 2. (실패) 완전탐색. 시간 고려 x 전체
# """
# from itertools import combinations, product
# def solution(dice):
#     answer = (0, [0, 0])
#     dice_indexes = [i+1 for i in range(len(dice))]
#     for comb in combinations(dice_indexes, len(dice) // 2):
#         a = [dice[i-1] for i in comb]
#         b = [dice[i-1] for i in set(dice_indexes) - set(comb)]
#         win = 0
#         draw = 0
#         lose = 0
#         for p_a in product(*a):
#             for a_n, b_n in product([p_a], product(*b)):
#                 if sum(a_n) > sum(b_n):
#                     win += 1
#                 elif sum(a_n) < sum(b_n):
#                     lose += 1
#                 else:
#                     draw += 1
#         if win > answer[0]:
#             answer = (win, comb)
#     return list(answer[1])


# """
# # 시도 1. (실패) 테케 3 통과 하지 못 함
# ## 방법
#   - 배열을 평균 순으로 정렬
#   - 평균이 같다면 제일 작은 수를 빼내고 다시 비교
#
# ## 문제
#   - 평균이 높아도 합쳤을 때, 상대적으로 작은 숫자가 많은 경우가 있음
# """
# from functools import cmp_to_key
#
# def compare_dice(x, y):
#     copy_x = sorted(x[1], reverse=True)
#     copy_y = sorted(y[1], reverse=True)
#     print(copy_x, copy_y)
#     while (sum(copy_x) / 6) == (sum(copy_y) / 6):
#         copy_x.pop()
#         copy_y.pop()
#     return 1 if (sum(copy_x) / 6) > (sum(copy_y) / 6) else -1
#
#
# def solution(dice):
#     answer = []
#     max_dice_count = len(dice) // 2
#     sorted_indexed_dice = sorted([(i+1, d) for i, d in enumerate(dice)], key=cmp_to_key(compare_dice))
#
#     for d in sorted_indexed_dice:
#         print(d[0], d[1], sum(d[1]) / 6)
#
#     while len(answer) < max_dice_count:
#         answer.append(sorted_indexed_dice.pop()[0])
#     return answer
