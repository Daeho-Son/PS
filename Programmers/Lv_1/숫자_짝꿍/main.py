from run_test import run_test
from solution import solution


def main():
    test_case = [
        # X	Y	result
        ["100", "2345", "-1"],
        ["100", "203045", "0"],
        ["100", "123450", "10"],
        ["12321", "42531", "321"],
        ["5525", "1255", "552"],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
