def solution(n, lost, reserve):
    intersection = set(lost) & set(reserve)
    lost = set(lost) - intersection
    reserve = set(reserve) - intersection

    borrowed_count = 0
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
            borrowed_count += 1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            borrowed_count += 1
    return n - len(lost) + borrowed_count

# def solution(n, lost, reserve):
#     lost.sort()
#     reserve.sort()
#
#     numbers = [0 if i == 0 or i == n + 1 else 1 for i in range(n + 2)]
#     for l in lost:
#         numbers[l] -= 1
#     for r in reserve:
#         numbers[r] += 1
#     for i in range(1, n + 1):
#         if numbers[i] != 0:
#             continue
#         if numbers[i - 1] > 1:
#             numbers[i - 1] -= 1
#             numbers[i] += 1
#         elif numbers[i + 1] > 1:
#             numbers[i + 1] -= 1
#             numbers[i] += 1
#     return n - numbers[1:-1].count(0)
