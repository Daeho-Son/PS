import math


def solution(n, costs, start):
    island_indexes = [i for i in range(n)]
    recieve_to_connection = dict(zip(island_indexes, [i for i in range(n)]))
    island_scores = dict(zip(island_indexes, [math.inf if i != start else 0 for i in range(n)]))
    for _round in range(n):
        is_changed = False
        for i, (_from, _to, _cost) in enumerate(costs):
            if island_scores.get(_from) > island_scores.get(_to):
                _from, _to = _to, _from
            if island_scores.get(_from) + _cost < island_scores.get(_to):
                if _round == n - 1:
                    return -1
                island_scores[_to] = island_scores.get(_from) + _cost
                recieve_to_connection[_from] = _to
                is_changed = True

        if not is_changed:
            break
    return island_scores


def main():
    costs = [
        [0, 1, 9],
        [0, 2, 2],
        [1, 2, 6],
        [1, 3, 3],
        [1, 4, 1],
        [2, 3, 2],
        [2, 5, 9],
        [3, 4, 5],
        [3, 5, 6],
        [4, 5, 3],
        [4, 6, 7],
        [5, 6, 4]
    ]
    print(solution(7, costs, 0))


if __name__ == '__main__':
    main()
