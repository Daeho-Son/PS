import sys

n = int(input())
x = list(map(int, sys.stdin.readline().split()))
print(f"{min(x)}\n{max(x)}")