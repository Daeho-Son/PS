from run_test import run_test
from solution import solution


def main():
    test_case = [
        # topping	result
        [[1, 2, 1, 3, 1, 4, 1, 2], 2],
        [[1, 2, 3, 1, 4], 0],
        [[1], 0],
        [[1, 1, 1, 1, 1], 4],
        [[1, 1, 1, 1, 1, 1], 5],
        [[1, 1, 2, 1], 0],
        [[1, 1, 1, 2, 3, 4], 0],
        [[1, 2, 1, 3, 4, 1], 0]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
