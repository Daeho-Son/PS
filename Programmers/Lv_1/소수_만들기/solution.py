# from itertools import combinations
#
#
# MAX_N = 3001
#
#
# def solution(nums):
#     global MAX_N
#     primes = [True] * MAX_N
#
#     for i in range(2, int(MAX_N ** 0.5) + 1):
#         if not primes[i]:
#             continue
#         n = 2
#         while i * n <= MAX_N:
#             primes[i * n] = False
#             n += 1
#
#     answer = 0
#     for comb_n in combinations(nums, 3):
#         if primes[sum(comb_n)]:
#             answer += 1


from itertools import combinations

MAX_N = 3001


def solution(nums):
    answer = 0
    primes = set(range(2, MAX_N))
    for i in range(2, MAX_N):
        if i in primes:
            primes -= set(range(i * 2, MAX_N, i))
    for n in combinations(nums, 3):
        if sum(n) in primes:
            answer += 1
    return answer
