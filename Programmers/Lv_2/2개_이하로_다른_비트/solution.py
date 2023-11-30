# 풀이 2
def get_bit(x):
    if x % 2 == 0:
        return x + 1
    return (x + 1) | ((x ^ x + 1) >> 2)


def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(get_bit(number))
        print()
    return answer

# 풀이 1
# def get_bit(x):
#     if x % 2 == 0:
#         return x + 1
#     gg = list(format(x ^ (x + 1), 'b'))
#     gg[1] = '0'
#     return int(format(x + 1, 'b'), 2) | int(''.join(gg), 2)
#
#
# def solution(numbers):
#     answer = []
#     for number in numbers:
#         answer.append(get_bit(number))
#     return answer
