def solution(lottos, win_nums):
    ranking_by_right_number = dict(zip([6, 5, 4, 3, 2, 1, 0], [1, 2, 3, 4, 5, 6, 6]))
    wrong_count = 6 - len(set(win_nums) - set(lottos))

    return [ranking_by_right_number[wrong_count + lottos.count(0)], ranking_by_right_number[wrong_count]]

≠
# def solution(lottos, win_nums):
#     ranking_by_right_number = dict(zip([6, 5, 4, 3, 2, 1, 0], [1, 2, 3, 4, 5, 6, 6]))
#     wrong_numbers = list(set(win_nums) - set(lottos))
#     minimum_right_number = 6 - len(wrong_numbers)
#     for z in range(lottos.count(0)):
#         zero_index = lottos.index(0)
#         lottos[zero_index] = wrong_numbers.pop()
#     maximum_right_number = 6 - len(list(set(win_nums) - set(lottos)))
#     return [ranking_by_right_number[maximum_right_number], ranking_by_right_number[minimum_right_number]]
