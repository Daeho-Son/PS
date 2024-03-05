from run_test import run_test
from solution import solution


def main():
    test_case = [
        # works	n	result
        [4, [4, 3, 3], 12],
        [1, [2, 1, 2], 6],
        [3, [1, 1], 0],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
