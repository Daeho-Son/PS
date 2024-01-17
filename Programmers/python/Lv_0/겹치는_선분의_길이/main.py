from run_test import run_test
from solution import solution


def main():
    test_case = [
        # lines	result
        [[[0, 1], [2, 5], [3, 9]], 2],
        [[[-1, 1], [1, 3], [3, 9]], 0],
        [[[0, 5], [3, 9], [1, 10]], 8],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
