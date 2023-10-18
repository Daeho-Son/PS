from collections import Counter

n = int(input())
ns = list(map(int, input().split()))
counter_ns = dict(Counter(ns))
m = int(input())
ms = list(map(int, input().split()))
for _m in ms:
    print(0 if _m not in counter_ns else counter_ns[_m])
