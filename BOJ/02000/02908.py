import sys

list_number = []
for i in map(str, sys.stdin.readline().split()):
    list_number.append(i[::-1])
print(max(list_number))

#import sys
#
# number = map(str, sys.stdin.readline().split())
# list_number = []
# for i in number:
#     reverse = ''
#     for j in range(-1, -len(i)-1, -1):
#         reverse = reverse + i[j]
#     list_number.append(int(reverse))
# print(max(list_number))