import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
ns = [int(input()) for _ in range(n)]
sorted_ns = sorted(ns)
_arithmetic_mean = round(sum(ns) / n)
print(_arithmetic_mean)  # 산술평균

_median_value = sorted_ns[((n + 1) // 2) - 1]
print(_median_value)  # 중앙값

most_common_ns = Counter(sorted_ns).most_common()
most_count = most_common_ns[0][1]
modes = [value for value, count in most_common_ns if count == most_count]
if len(modes) == 1:
    _mode = modes[0]
else:
    _mode = modes[1]
print(_mode)  # 최빈값

_range = sorted_ns[-1] - sorted_ns[0]
print(_range)  # 범위
