import time


def fibo_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)


dp = [0] * 91


def fibo_dp(n):
    if n == 1 or n == 2:
        return 1
    if dp[n]:
        return dp[n]
    dp[n] = fibo_dp(n - 1) + fibo_dp(n - 2)
    return dp[n]


n = int(input())
start = time.time()
print(fibo_recursive(n))
end = time.time()
print(f'{end - start:.4f}')

n = int(input())
start = time.time()
print(fibo_dp(n))
end = time.time()
print(f'{end - start:.4f}')

