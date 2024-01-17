from run_test import run_test
from solution import solution


def main():
    test_case = [
        # x	y	n	result
        [10, 40, 5, 2],
        [10, 40, 30, 1],
        [2, 5, 4, -1],
        [4, 4, 3, 0]
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
