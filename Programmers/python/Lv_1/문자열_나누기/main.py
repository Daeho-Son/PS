from run_test import run_test
from solution import solution


def main():
    # s	result
    test_case = [
        ["banana", 3],
        ["abracadabra", 6],
        ["aaabbaccccabba", 3],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
