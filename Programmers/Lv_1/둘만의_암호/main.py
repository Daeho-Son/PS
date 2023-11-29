from run_test import run_test
from solution import solution


def main():
    test_case = [
        # s	skip	index	result
        ["aukks", "wbqd", 5, "happy"],
        ["a", "cb", 1, "d"],
        ["a", "bcdefghijk", 20, "o"]
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
