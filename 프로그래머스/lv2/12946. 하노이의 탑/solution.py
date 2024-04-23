"""
# 시도 2. 다른 사람 풀이를 다시 읽고 구현
"""
answer = list()

def move(n, current_index, target_index, temp_index):
    if n == 1:
        answer.append([current_index, target_index])
        return
    move(n - 1, current_index, temp_index, target_index)
    answer.append([current_index, target_index])
    move(n - 1, temp_index, target_index, current_index)
    return


def solution(n):
    global answer
    answer = list()

    hanoi = [[i for i in range(n, 0, -1)], [], []]
    move(n, 1, 3, 2)
    return answer

# """
# # 시도 1. 구현 실패 후, 다른 사람 풀이 이해하고 구현
# """
# hanoi = list()
# answer = list()
# hanoi_indexes = {0, 1, 2}
#
# def print_hanoi():
#     print(hanoi[0])
#     print(hanoi[1])
#     print(hanoi[2])
#     print()
#
# def move(target_number, current_index, dest_index, temp_index):
#     global hanoi, answer
#     if target_number == 1:
#         answer.append([current_index + 1, dest_index + 1])
#         hanoi[dest_index].append(hanoi[current_index].pop())
#         return
#     move(target_number - 1, current_index, temp_index, dest_index)
#     answer.append([current_index + 1, dest_index + 1])
#     hanoi[dest_index].append(hanoi[current_index].pop())
#     move(target_number - 1, temp_index, dest_index, current_index)
#
#
# def solution(n):
#     global hanoi, answer
#     answer = list()
#     hanoi = [[i for i in range(n, 0, -1)], [], []]
#     move(n, 0, 2, 1)
#     return answer
