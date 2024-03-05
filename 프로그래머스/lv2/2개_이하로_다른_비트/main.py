from run_test import run_test
from solution import solution


def main():
    test_case = [
        # numbers	result
        [[2, 7], [3, 11]],
        [[9], [10]]
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
