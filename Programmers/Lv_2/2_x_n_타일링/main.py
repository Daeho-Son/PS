from run_test import run_test
from solution import solution


def main():
    test_case = [
        # n	result
        [2, 2],
        [3, 3],
        [4, 5],
        [5, 8],
        [6, 13],
        [7, 21],
        [8, 34],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
