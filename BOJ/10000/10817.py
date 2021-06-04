import sys

print(sorted(map(int, sys.stdin.readline().split()))[-2])


# import sys
# 
# number = []
# for i in map(int, sys.stdin.readline().split()):
#     number.append(i)
# 
# number.remove(max(number))
# print(max(number))