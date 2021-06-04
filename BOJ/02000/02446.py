count = int(input())
for i in range(count):
    print(' '*i + '*'*((2*count-1) - (2*i)))

for j in range(count-2, -1, -1):
    print(' '*j + '*'*((2*count-1) - (2*j)))

# count = int(input())
# 
# for i in range(1, 2*count, 2):
#     print(('*'*(2*count-i)).center(2*count-1))
# 
# for j in range(2*count-3, 0, -2):
#     print(('*'*(2*count-j)).center(2*count-1))