import re

def solution(dart_result):
    answer_list = list()
    bonus_dict = dict(zip(['S', 'D', 'T'], [1, 2, 3]))
    option_dict = dict(zip(['*', '#', ''], [2, -1, 1]))
    pattern = re.compile('(\d+)([SDT])([*#])?')
    for score, bonus, option in pattern.findall(dart_result):
        answer_list.append((int(score) ** bonus_dict.get(bonus)) * option_dict.get(option))
        if option == '*' and len(answer_list) >= 2:
            answer_list[-2] *= option_dict.get(option)
    print(answer_list)
    return sum(answer_list)


# import re
#
#
# def solution(dart_result):
#     answer_list = list()
#     score_list = list(filter(lambda x: x, re.split(r'[SDT*#]', dart_result)))
#     bonus_option_list = list(filter(lambda x: x, re.split(r'[0-9]', dart_result)))
#     for score, bonus_option in zip(score_list, bonus_option_list):
#         if 'S' in bonus_option[0]:
#             answer_list.append(int(score) ** 1)
#         elif 'D' in bonus_option:
#             answer_list.append(int(score) ** 2)
#         elif 'T' in bonus_option:
#             answer_list.append(int(score) ** 3)
#
#         if '*' in bonus_option:
#             if len(answer_list) >= 2:
#                 answer_list[-2] *= 2
#             answer_list[-1] *= 2
#         elif '#' in bonus_option:
#             answer_list[-1] *= -1
#     return sum(answer_list)
