from run_test import run_test
from solution import solution


def main():
    test_case = [
        # ingredient	result
        [[2, 1, 1, 2, 3, 1, 2, 3, 1], 2],
        [[1, 3, 2, 1, 2, 1, 3, 1, 2], 0],
        [[1, 2, 3, 1, 1, 2, 3, 1], 2],
        [[1, 1, 2, 3, 1, 2, 3, 1], 2],
        [[1, 2, 1, 2, 3, 1, 3, 1], 2],
        [[1, 2, 3, 1, 2, 3, 1, 1], 1]
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
