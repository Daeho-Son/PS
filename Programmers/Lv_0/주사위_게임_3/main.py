from run_test import run_test
from solution import solution


def main():
    # a	b	c	d	result
    test_case = [
        [2, 2, 2, 2, 2222],
        [4, 1, 4, 4, 1681],
        [6, 3, 3, 6, 27],
        [2, 5, 2, 6, 30],
        [6, 4, 2, 5, 2],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
