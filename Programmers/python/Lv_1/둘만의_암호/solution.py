# 풀이 2
from string import ascii_lowercase


def solution(s, skip, index):
    answer = ''
    lower_alphabet = sorted(set(ascii_lowercase) - set(skip)) * 2
    alphabet_mapper = dict(zip(lower_alphabet, lower_alphabet[index:] + lower_alphabet[:index]))
    for c in s:
        answer += alphabet_mapper.get(c)
    return answer

# 풀이 1
# def increase_alphabet(c):
#     if ord(c) + 1 > ord('z'):
#         return chr((ord(c) + 1) % 123 + 97)
#     return chr((ord(c) + 1))
#
#
# def solution(s, skip, index):
#     answer = ''
#     for c in s:
#         i = 0
#         while i < index:
#             c = increase_alphabet(c)
#             if c in skip:
#                 continue
#             i += 1
#         answer += c
#     return answer