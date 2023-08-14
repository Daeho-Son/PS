from solution import solution
from run_test import run_test


def main():
    test_case = [
        # numbers	result
        [[2, 3, 3, 5], [3, 5, 5, -1]],
        [[9, 1, 5, 3, 6, 2], [-1, 5, 6, 6, -1, -1]],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
