# 키워드
# python re 모듈
# python regex
import re


def solution(files):
    return sorted(files, key=lambda file: (re.split(r'\d+', file)[0].lower(), int(re.findall(r'\d{1,5}', file)[0])))


# import re
#
#
# def solution(files):
#     tokens = list()
#     for file in files:
#         words = re.split(r'\d+', file)
#         head = words[0]
#         number = ''
#         tail = ''
#         if len(words) >= 2:
#             number_start_index = len(words[0])
#             if words[1] == '':
#                 number = file[number_start_index:]
#             else:
#                 tail_start_index = number_start_index + file[number_start_index:].index(words[1])
#                 number = file[number_start_index:tail_start_index]
#                 tail = file[tail_start_index:]
#         tokens.append((head, number, tail))
#     tokens.sort(key=lambda x: (x[0].lower(), int(x[1])) if x[1] else (x[0].lower()))
#     return list(map(lambda x: ''.join(x), tokens))
