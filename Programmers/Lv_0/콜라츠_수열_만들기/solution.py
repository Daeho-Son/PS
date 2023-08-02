def solution(n):
    answer = []
    x = n
    while x != 1:
        answer.append(x)
        if x % 2 == 0:
            x = int(x / 2)
        else:
            x = int(3 * x + 1)
        print(x)
    answer.append(1)
    return answer