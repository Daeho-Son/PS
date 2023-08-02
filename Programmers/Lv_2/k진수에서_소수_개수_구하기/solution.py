def solution(n, k):
    k_base = ''
    while n > 0:
        _div, _mod = divmod(n, k)
        k_base += str(_mod)
        n = _div

    k_base = list(map(lambda x: int(x) if x else 0, k_base[::-1].split('0')))
    print(k_base)
    max_prime = max(k_base)
    primes = [True] * (max_prime + 1)
    for i in range(0, max_prime + 1):
        if i == 0 or i == 1:
            primes[i] = False
        if not primes[i]:
            continue
        for j in range(i * 2, max_prime + 1, i):
            primes[j] = False

    answer = 0
    for _n in k_base:
        if primes[_n]:
            answer += 1
    return answer
