from run_test import run_test
from solution import solution


def main():
    test_case = [
        # land	answer
        [[[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]], 16],
        [[[1, 2, 3, 5]], 5],
        [[[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1], [7, 6, 5, 4]], 22],
        [[[1, 2, 3, 5], [5, 6, 7, 100], [4, 3, 2, 1]], 107],
        [[[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]], 20]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
