def solution(num, total):
    answer = list()
    if num == 1:
        return [total]
    n = (total + 1) // num - ((num + 1) // 2 - 1)
    for _ in range(num):
        answer.append(n)
        n += 1
    return answer

