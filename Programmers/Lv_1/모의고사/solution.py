from math import ceil


def solution(answers):
    people1 = [1, 2, 3, 4, 5]
    people2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0] * 3
    for i, n in enumerate(answers):
        if people1[i % len(people1)] == n:
            scores[0] += 1
        if people2[i % len(people2)] == n:
            scores[1] += 1
        if people3[i % len(people3)] == n:
            scores[2] += 1

    max_score = max(scores)
    return [i + 1 for i, n in enumerate(scores) if n == max_score]
