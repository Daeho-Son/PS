from run_test import run_test
from solution import solution


def main():
    test_case = [
        # N	number	return
        [5, 12, 4],
        [2, 11, 3],
        [1, 121, 4],
        [5, 3025, 4],
        [5, 3125, 5],
        [9, 9, 1],
        [9, 99, 2],
        [9, 999, 3],
        [9, 9999, 4],
        [9, 99999, 5],
        [9, 999999, 6],
        [9, 9999999, 7],
        [9, 99999999, 8],
        [9, 999999999, -1],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
