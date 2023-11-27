from run_test import run_test
from solution import solution


def main():
    test_case = [
        # queue1	queue2	result
        # [[3, 2, 7, 2], [4, 6, 5, 1], 2],
        # [[1, 2, 1, 2], [1, 10, 1, 2], 7],
        # [[1, 1], [1, 5], -1],
        # [[1, 1], [5], -1],
        # [[1, 1, 1], [1, 1, 1, 1], -1],
        # [[2, 1, 1], [1, 10, 1], -1],
        [[4, 6, 5, 1], [3, 2, 7, 2], 2],
        [[1, 1], [100], -1]
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
