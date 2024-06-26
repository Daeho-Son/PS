from run_test import run_test
from solution import solution


def main():
    test_case = [
        # dice	result
        [[[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]], [1, 4]],
        [[[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]], [2]],
        [[[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]], [1, 3]],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
