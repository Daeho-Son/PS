import math

def solution(x, y, n):
    dp = [math.inf] * (y + 1)
    dp[x] = 0
    if x == y:
        return 0
    for i in range(x + n, y + 1):
        dp[i] = dp[i - n] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    answer = dp[y]
    if math.isinf(answer):
        return -1
    return answer
