from itertools import combinations


def solution(dots):
    for l_1 in combinations(dots, 2):
        l_2 = [dot for dot in dots if dot not in l_1]
        dist_1 = (l_1[1][1] - l_1[0][1]) / (l_1[1][0] - l_1[0][0])
        dist_2 = (l_2[1][1] - l_2[0][1]) / (l_2[1][0] - l_2[0][0])
        if dist_1 == dist_2:
            return 1
    return 0
