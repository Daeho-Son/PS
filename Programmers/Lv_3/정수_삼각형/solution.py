def solution(triangle):
    for t_index in range(len(triangle)-1, 0, -1):
        current_line = triangle[t_index]
        target_line = triangle[t_index-1]
        for i in range(len(target_line)):
            target_line[i] = max(target_line[i] + current_line[i], target_line[i] + current_line[i+1])
    return triangle[0][0]

# def solution(triangle):
#     answer = [triangle[0]]
#     for t_index in range(len(triangle) - 1):
#         current_line = answer[t_index]
#         next_line = triangle[t_index + 1]
#         max_sum_line = list()
#         for i in range(len(current_line)):
#             if len(max_sum_line) == i:
#                 max_sum_line.append(current_line[i] + next_line[i])
#             else:
#                 max_sum_line[i] = max(max_sum_line[i], current_line[i] + next_line[i])
#             max_sum_line.append(current_line[i] + next_line[i + 1])
#         answer.append(max_sum_line)
#     return max(answer[-1])