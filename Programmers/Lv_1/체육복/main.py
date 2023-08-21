from run_test import run_test
from solution import solution


def main():
    test_case = [
        # n	lost	reserve	return
        [5, [2, 4], [1, 3, 5], 5],
        [5, [2, 4], [3], 4],
        [3, [3], [1], 2],
        [3, [3, 2], [1, 2], 2],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
