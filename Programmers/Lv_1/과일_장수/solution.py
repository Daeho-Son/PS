def solution(k, m, score):
    return sum(sorted(score, reverse=True)[m-1::m]) * m
    # score.sort(reverse=True)
    # answer = 0
    # for i in range(0, len(score), m):
    #     apples = score[i:i+m]
    #     if len(apples) == m:
    #         answer += apples[-1] * m
    # return answer
