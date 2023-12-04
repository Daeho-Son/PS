from run_test import run_test
from solution import solution


def main():
    test_case = [
        # numbers	return
        [[6, 10, 2], "6210"],
        [[3, 30, 34, 5, 9], "9534330"]
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
