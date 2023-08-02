def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    k_base = ''
    while n > 0:
        n, _mod = divmod(n, k)
        k_base += str(_mod)
    nums = list(map(lambda x: int(x) if x != '' else 0, k_base[::-1].split('0')))
    for num in nums:
        if result := is_prime(num):
            answer += 1
    return answer
