from run_test import run_test
from solution import solution


def main():
    test_case = [
        # order	result
        [[4, 3, 1, 2, 5], 2],
        [[5, 4, 3, 2, 1], 5],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
