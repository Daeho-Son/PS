def solution(n, s):
    if n > s:
        return [-1]

    d, m = divmod(s, n)
    print(d, m)
    answer = list()
    for _ in range(n - m):
        answer.append(d)
    for _ in range(m):
        answer.append(d+1)
    return answer
