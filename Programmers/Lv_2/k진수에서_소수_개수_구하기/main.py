from run_test import run_test
from solution import solution


def main():
    # n, k, result
    test_case = [
        [437674, 3, 3],
        [110011, 10, 2],
        [1, 3, 0],
        [1, 10, 0],
        [1000000, 3, 2],
        [1000000, 10, 0],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
