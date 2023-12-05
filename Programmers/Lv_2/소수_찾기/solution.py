from itertools import permutations
import math


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    permutation_numbers = set()
    for i in range(1, len(numbers)+1):
        for permutation in permutations(numbers, i):
            permutation_numbers.add(int(''.join(permutation)))
    for p in permutation_numbers:
        if is_prime(p):
            answer += 1
    return answer
