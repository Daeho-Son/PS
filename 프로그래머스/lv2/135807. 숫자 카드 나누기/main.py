from run_test import run_test
from solution import solution


def main():
    test_case = [
        # arrayA	arrayB	result
        [[10, 17], [5, 20], 0],
        [[10, 20], [5, 17], 10],
        [[14, 35, 119], [18, 30, 102], 7],
        [[10, 10], [1, 1], 10],
        [[1, 1], [10, 10], 10],
        [[1, 1], [1, 1], 0],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
