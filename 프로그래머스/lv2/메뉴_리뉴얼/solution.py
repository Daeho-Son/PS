# 2
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for menu_count in course:
        menu_comb = []
        for order in orders:
            menu_comb += combinations(sorted(order), menu_count)
        most_ordered_menu_comb = Counter(menu_comb).most_common()
        if not most_ordered_menu_comb:
            continue
        most_ordered_count = most_ordered_menu_comb[0][1]
        answer += [''.join(k) for k, v in most_ordered_menu_comb if v > 1 and v >= most_ordered_count ]
    return sorted(answer)



# # 1
# from itertools import combinations
# from collections import Counter
#
#
# def solution(orders, course):
#     answer = []
#     menu_combinations = []
#     for order in orders:
#         for menu_count in course:
#             for c in combinations(sorted(order), menu_count):
#                 menu_combinations.append(''.join(c))
#
#     menu_combinations_count = sorted(Counter(menu_combinations).most_common(), key=lambda x: (-len(x[0]), x[1]))
#     target_count = -1
#     most_count = 0
#     while menu_combinations_count:
#         menu_comb, count = menu_combinations_count[-1]
#         if count < 2:
#             menu_combinations_count.pop()
#             continue
#         if not answer or len(menu_comb) != course[target_count]:
#             answer.append(menu_comb)
#             most_count = count
#             target_count += 1
#         elif most_count == count:
#             answer.append(menu_comb)
#         menu_combinations_count.pop()
#     return sorted(answer)
