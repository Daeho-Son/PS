from run_test import run_test
from solution import solution


def main():
    # number	limit	power	result
    test_case = [
        [5, 3, 2, 10],
        [10, 3, 2, 21]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
