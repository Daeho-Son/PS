import random

from run_test import run_test
from solution_1 import solution as solution_1
from solution_2 import solution as solution_2
from solution_3 import solution as solution_3

type_genre = ["classic", "rock", "pop", "edm"]


def get_test_case():
    return [
        [["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500], [4, 1, 3, 0]],
        [["classic"], [100], [0]],
        [["classic", "rock", "classic", "classic", "pop"], [500, 600, 150, 800, 2500], [4, 3, 0, 1]],
        [["classic", "rock", "classic", "classic", "pop"], [500, 600, 150, 500, 2500], [4, 0, 3, 1]],
    ]


def get_test_case_maximum():
    genres = []
    plays = []
    answer = []
    for i in range(10000):
        genres.append(type_genre[random.randrange(0, len(type_genre))])
        plays.append(random.randrange(1, 100000))
    return [
        [genres, plays, answer]
    ]


def main():
    # test_case = get_test_case()
    test_case = get_test_case_maximum()
    run_test(test_case, solution_3)


if __name__ == "__main__":
    main()
