import sys

for i in range(1, (int(input())+1)):
    x = map(int, sys.stdin.readline().split())
    print(sum(x))