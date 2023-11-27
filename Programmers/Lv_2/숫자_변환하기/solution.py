# 풀이 2
def solution(x, y, n):
    answer = 0
    numbers = set()
    numbers.add(x)

    while numbers:
        if y in numbers:
            return answer
        next_numbers = set()
        for number in numbers:
            if number + n <= y:
                next_numbers.add(number + n)
            if number * 2 <= y:
                next_numbers.add(number * 2)
            if number * 3 <= y:
                next_numbers.add(number * 3)
        numbers = next_numbers
        answer += 1
    if not numbers:
        return -1
    return numbers


# 풀이 1 - DP
# import math
#
# def solution(x, y, n):
#     dp = [math.inf] * (y + 1)
#     dp[x] = 0
#     if x == y:
#         return 0
#     for i in range(x + n, y + 1):
#         dp[i] = dp[i - n] + 1
#         if i % 2 == 0:
#             dp[i] = min(dp[i], dp[i // 2] + 1)
#         if i % 3 == 0:
#             dp[i] = min(dp[i], dp[i // 3] + 1)
#
#     answer = dp[y]
#     if math.isinf(answer):
#         return -1
#     return answer
