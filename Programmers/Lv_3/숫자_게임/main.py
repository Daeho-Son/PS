from run_test import run_test
from solution import solution


def main():
    test_case = [
        # A	B	result
        [[5, 1, 3, 7], [2, 2, 6, 8], 3],
        [[2, 2, 2, 2], [1, 1, 1, 1], 0],
        [[15, 17], [14, 17], 1]
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
