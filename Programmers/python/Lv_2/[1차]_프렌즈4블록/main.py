from run_test import run_test
from solution import solution


def main():
    test_case = [
        # m	n	board	answer
        [4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"], 14],
        [6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"], 15],
        [4, 4, ["AAAA", "AAAA", "BCDE", "BCDE"], 8],
        [2, 2, ["AB", "AB"], 0]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
