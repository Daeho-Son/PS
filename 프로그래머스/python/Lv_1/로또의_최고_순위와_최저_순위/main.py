from solution import solution
from run_test import run_test


def main():
    test_case = [
        # lottos	win_nums	result
        [[44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19], [3, 5]],
        [[0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25], [1, 6]],
        [[45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35], [1, 1]],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
