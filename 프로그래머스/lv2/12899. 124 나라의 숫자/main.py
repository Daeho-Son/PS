from run_test import run_test
from solution import solution


def main():
    test_case = [
        [1, "1"],
        [2, "2"],
        [3, "4"],
        [4, "11"],
        [5, "12"],
        [6, "14"],
        [7, "21"],
        [8, "22"],
        [9, "24"],
        [10, "41"],
        [11, "42"],
        [12, "44"],
        [13, "111"],
        [14, "112"],
        [15, "114"],
        [16, "121"]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
