from solution import solution
from run_test import run_test


def main():
    test_case = [
        # scoville	K	return
        [[1, 2, 3, 9, 10, 12], 7, 2],
        [[1, 2], 7, -1]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
