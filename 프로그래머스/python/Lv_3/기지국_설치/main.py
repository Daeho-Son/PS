from run_test import run_test
from solution import solution


def main():
    test_case = [
        # N	stations	W	answer
        [11, [4, 11], 1, 3],
        [16, [9], 2, 3],
        [11, [4, 9], 1, 3],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
