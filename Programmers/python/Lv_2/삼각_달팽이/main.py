from run_test import run_test
from solution import solution as solution
from solution_1 import solution as solution_1


def main():
    test_case = [
        # n	result
        [4, [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]],
        # [5, [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]],
        # [6, [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11]],
    ]

    run_test(test_case, solution_1)


if __name__ == '__main__':
    main()
