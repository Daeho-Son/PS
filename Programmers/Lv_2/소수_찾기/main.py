from run_test import run_test
from solution import solution


def main():
    test_case = [
        # numbers	return
        ["17", 3],
        ["011", 2],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
