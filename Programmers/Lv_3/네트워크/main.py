from solution import solution
from run_test import run_test


def main():
    test_case = [
        [3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]],	2],
        [3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]],	1]
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()