from run_test import run_test
from solution import solution


def main():
    test_case = [
        # prices	return
        [[1, 2, 3, 2, 3], [4, 3, 1, 1, 0]]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
