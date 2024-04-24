from run_test import run_test
from solution import solution


def main():
    test_case = [
        # n	costs	return
        [4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]], 4]
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
