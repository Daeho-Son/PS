number = [int(input()) for i in range(9)]

print(max(number))
print(number.index(max(number))+1)

# number = []
# for i in range(9):
#     number.append(int(input()))

# max_number = number[0]
# for i in number:
#     if max_number < i:
#         max_number = i
# print(max_number)
# print(number.index(max_number)+1)