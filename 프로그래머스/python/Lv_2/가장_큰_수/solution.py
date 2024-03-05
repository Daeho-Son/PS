from functools import cmp_to_key


def compare(x, y):
    if x + y > y + x:
        return -1
    return 1


def solution(numbers):
    numbers = list(map(lambda x: str(x), numbers))
    numbers.sort(key=cmp_to_key(compare))
    return str(int(''.join(numbers)))
