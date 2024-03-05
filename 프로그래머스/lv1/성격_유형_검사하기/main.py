from run_test import run_test
from solution import solution


def main():
    test_case = [
        # survey	choices	result
        [["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5], "TCMA"],
        [["TR", "RT", "TR"], [7, 1, 3], "RCJA"],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
