import sys

for i in range(0, int(input())):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")
