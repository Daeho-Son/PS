from run_test import run_test
from solution import solution


def main():
    test_case = [
        # dots	result
        [[[1, 4], [9, 2], [3, 8], [11, 6]], 1],
        [[[3, 5], [4, 1], [2, 4], [5, 10]], 0],
        [[[10, 1], [9, 3], [2, 2], [4, 4]], 0],
        [[[1, 2], [5, 1], [3, 6], [6, 3]], 1]
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
