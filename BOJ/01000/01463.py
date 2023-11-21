# DP::Top-Down
# d = [0] * 11
#
#
# def solution(n):
#     if n == 1:
#         return 0
#     if d[n]:
#         return d[n]
#     d[n] = solution(n - 1) + 1
#     if n % 3 == 0:
#         d[n] = min(d[n], d[n // 3] + 1)
#     if n % 2 == 0:
#         d[n] = min(d[n], d[n // 2] + 1)
#     return d[n]


# DP::Bottom-Top
def solution(n):
    d = [0] * (n + 1)
    for i in range(2, n + 1):
        d[i] = d[i - 1] + 1
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
    return d[n]
#

n = int(input())
print(solution(n))
