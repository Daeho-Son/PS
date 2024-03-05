# MAX_N = 1000001
# primes = [True] * MAX_N
#
#
# def sieve_of_eratosthenes():
#     global primes
#     primes[0] = False
#     primes[1] = False
#     for i in range(2, int(MAX_N ** 0.5) + 1):
#         if not primes[i]:
#             continue
#         n = 2
#         while i * n < MAX_N:
#             primes[i * n] = False
#             n += 1
#
#
# def is_prime(n):
#     return primes[n]
#
#
# def solution(n):
#     sieve_of_eratosthenes()
#     answer = 0
#     for i in range(1, n + 1):
#         if primes[i]:
#             answer += 1
#     return answer


def solution(n):
    answer = 0
    primes = set(range(2, n+1))

    for i in range(2, n+1):
        if i in primes:
            primes -= set(range(i * 2, n+1, i))
    return len(primes)