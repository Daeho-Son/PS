from run_test import run_test
from solution import solution


def main():
    test_case = [
        # board	moves	result
        [[[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
         [1, 5, 3, 5, 1, 2, 1, 4], 4]
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
