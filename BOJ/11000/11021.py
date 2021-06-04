import sys

for i in range(0, int(input())):
    x = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {sum(x)}")