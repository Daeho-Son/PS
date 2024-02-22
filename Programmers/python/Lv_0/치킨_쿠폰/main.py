from run_test import run_test
from solution import solution


def main():
    test_case = [
        # chicken	result
        [100, 11],
        [1081, 120],
        [1999, 222]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
