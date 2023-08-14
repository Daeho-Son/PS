from run_test import run_test
from solution import solution


def main():
    test_case = [
        # word	result
        ["AAAAE", 6],
        ["AAAE", 10],
        ["I", 1563],
        ["EIO", 1189],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
