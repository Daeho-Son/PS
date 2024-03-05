from run_test import run_test
from solution import solution


def main():
    test_case = [
        [[[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]], 3],
        [[[1, 2], [2, 3], [3, 4], [1, 4]], 3],
        [[[1, 3], [2, 4], [3, 5]], 2],
        [[[1, 4], [3, 5], [6, 7], [8, 10], [9, 11]], 3]
        ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
