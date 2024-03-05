from itertools import product


def solution(word):
    dictionary = list()
    for i in range(1, 6):
        for comb in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            dictionary.append(''.join(comb))
    return sorted(dictionary).index(word) + 1
