from collections import Counter
from functools import reduce


def solution(clothes):
    count_clothes = Counter([_type for _name, _type in clothes])
    return reduce(lambda accumulate, current: accumulate * (current + 1), count_clothes.values(), 1) - 1

