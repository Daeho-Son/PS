'''
# 시도 2. 다른 사람 풀이를 분석하고 풀기
'''
n = int(input())
hs = list(map(int, input().split()))
if sum(hs) % 3 != 0:
    print("NO")
else:
    number_of_sprayers2_used = sum(list(map(lambda x: x // 2, hs)))
    if number_of_sprayers2_used >= (sum(hs) // 3):
        print("YES")
    else:
        print("NO")

# '''
# # 시도 1. (실패) 시간 초과
# '''
# from collections import deque
#
# n = int(input())
# hs = deque(sorted(map(int, input().split())))
# reminder_hs = deque([0] * n)
# for i, h in enumerate(hs):
#     reminder_hs[i] = hs[i] % 3
#
# f = True
# hs_count = len(hs)
# while hs_count > 2:
#     if reminder_hs[-1] >= 2:
#         reminder_hs[0] -= 1
#         reminder_hs[-1] -= 2
#     else:
#         incoming = 3
#         for i in range(hs_count - 1, -1, -1):
#             while incoming and reminder_hs[i] < hs[i]:
#                 reminder_hs[i] += 1
#                 incoming -= 1
#     if reminder_hs[-1] == 0:
#         reminder_hs.pop()
#         hs.pop()
#         hs_count -= 1
#     if reminder_hs[0] == 0:
#         reminder_hs.popleft()
#         hs.popleft()
#         hs_count -= 1
# if len(reminder_hs) == 2:
#     for i in range(reminder_hs[0]):
#         reminder_hs[0] -= 1
#         reminder_hs[1] -= 2
#     reminder_hs.popleft()
# if reminder_hs[0] >= 0 and reminder_hs[0] % 3 == 0:
#     print("YES")
# else:
#     print("NO")
