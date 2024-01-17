def solution(my_string, m, c):
    answer = []
    for i in range(len(my_string) // m):
        answer.append(my_string[m * i : m * (i + 1)])
    print(c, type(c))
    print(answer[0], answer[1])
    print(answer[0][c - 1])
