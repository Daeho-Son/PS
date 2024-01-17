from run_test import run_test
from solution import solution


def main():
    test_case = [
        # maps	answer
        [[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]], 11],
        [[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]], -1],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
