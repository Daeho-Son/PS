from run_test import run_test
from solution import solution


def main():
    test_case = [
        # maps	result
        # [["X591X", "X1X5X", "X231X", "1XXX1"], [1, 1, 27]],
        # [["XXX", "XXX", "XXX"], [-1]],
        # [["X1", "1X"], [1, 1]],
        [["X5XX5X", "111111", "XXXXXX", "111111"], [6, 16]]
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
