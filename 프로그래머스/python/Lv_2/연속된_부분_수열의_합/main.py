from run_test import run_test
from solution import solution


def main():
    test_case = [
        # [[1, 2, 3, 4, 5], 7, [2, 3]],
        [[1, 1, 1, 2, 3, 4, 5], 5, [6, 6]],
        # [[2, 2, 2, 2, 2], 6, [0, 2]],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
