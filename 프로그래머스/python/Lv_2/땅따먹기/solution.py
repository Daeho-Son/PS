def solution(land):
    for y in range(1, len(land)):
        for x in range(0, len(land[y])):
            land[y][x] += max(land[y-1][:x] + land[y-1][x+1:])
    return max(land[-1])

# 모든 케이스 실패. [[[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]], 20]
# 각 자리 수마다 최선의 값을 선택했어야됨.
# 먼저 나온 수의 인덱스를 저장해서 선택할 경우 0, 1 인덱스 위주로 선택이 되서 4, 2, 6, 7 = 19가 나옴
# def solution(land):
#     if not land:
#         return 0
#     answer = [(i, l) for i, l in enumerate(land[0])]
#     for line in land[1:]:
#         for i in range(len(answer)):
#             last_column = answer[i][0]
#             target = line[:last_column] + line[last_column+1:]
#             print(answer, target)
#             max_number = max(target)
#             target_index = line.index(max_number)
#             answer[i] = (target_index, answer[i][1] + max_number)
#     print(answer)
#     return max([accumulate_number for _, accumulate_number in answer])


# 모든 케이스 실패. 원인을 잘 모르겠음
# def solution(land):
#     answer = 0
#     last_column = -1
#     for l in land:
#         while True:
#             max_n = max(l)
#             column = l.index(max_n)
#             l[column] = -1
#             if column != last_column:
#                 answer += max_n
#                 last_column = column
#                 break
#     return answer
