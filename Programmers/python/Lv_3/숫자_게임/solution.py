def solution(a, b):
    answer = 0
    a.sort()
    b.sort()
    while a:
        n = a.pop()
        if n < b[-1]:
            b.pop()
            answer += 1
    return answer