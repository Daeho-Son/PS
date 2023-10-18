from collections import deque

n = int(input())
ns = deque([_n for _n in range(1, n+1)])

while n > 1:
    ns.popleft()
    top = ns.popleft()
    ns.append(top)
    n -= 1

print(ns[0])