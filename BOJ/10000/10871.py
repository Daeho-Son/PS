n, x = map(int, input().split())
sequence = list(map(int, input().split()))

for item in range(n):
    if sequence[item] < x:
        print(sequence[item], end=' ')

# import random
# 
# n, x = map(int, input().split())
# 
# sequence = random.sample(range(1, 11), n)
# for item in range(n):
#     print(sequence[item], end=' ')
# print()
# for item in range(n):
#     if sequence[item] < x:
#         print(sequence[item], end=' ')
#     else:
#         None