from run_test import run_test
from solution import solution


def main():
    test_case = [
        # cap	n	deliveries	pickups	result
        [4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0], 16],
        [2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0], 30],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
