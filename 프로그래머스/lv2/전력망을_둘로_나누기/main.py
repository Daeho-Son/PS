from run_test import run_test
from solution import solution


def main():
    test_case = [
        [9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]], 3],
        [4, [[1, 2], [2, 3], [3, 4]], 0],
        [7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]], 1],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
