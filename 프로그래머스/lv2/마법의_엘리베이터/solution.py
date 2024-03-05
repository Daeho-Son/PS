def solution(storey):
    answer = 0

    while storey:
        n = storey % 10
        if 0 <= n <= 4:
            answer += n
            storey -= n
        elif 6 <= n <= 9:
            answer += 10 - n
            storey += 10 - n
        else:
            answer += n
            next_n = (storey // 10) % 10
            if 0 <= next_n <= 4:
                storey -= n
            else:
                storey += 10 - n
        storey //= 10
    return answer
