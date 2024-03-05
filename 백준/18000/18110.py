import sys


def ft_round(f):
    if f - int(f) >= 0.5:
        return int(f) + 1
    else:
        return int(f)


input = sys.stdin.readline
n = int(input())
if not n:
    print(0)
else:
    ns = [int(input()) for _ in range(n)]
    exclude_count = ft_round(n * 0.15)
    new_ns = sorted(ns)[exclude_count:n-exclude_count]
    print(ft_round(sum(new_ns) / len(new_ns)))
