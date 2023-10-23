import sys

input = sys.stdin.readline
k, n = list(map(int, input().split()))  # 가지고 있는 랜선의 개수 K, 필요한 랜선의 개수 N
lan_cables = [int(input()) for _ in range(k)]  # 가지고 있는 모든 랜선의 길이

lan_cables.sort()
low = 0
high = lan_cables[-1]
while True:
    mid = (high + low) // 2
    if mid == 0:
        mid = 1
        break
    count = sum(map(lambda x: x // mid, lan_cables))
    if low > high:
        break
    if count < n:
        high = mid - 1
    else:
        low = mid + 1
print(mid)
