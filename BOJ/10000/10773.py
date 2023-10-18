k = int(input())
ns = list()
for _ in range(k):
    n = int(input())
    if n == 0:
        ns.pop()
    else:
        ns.append(n)
print(sum(ns))