from run_test import run_test
from solution import solution


def main():
    # msg	answer
    test_case = [
        ["KAKAO", [11, 1, 27, 15]],
        # ["TOBEORNOTTOBEORTOBEORNOT", [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]],
        # ["ABABABABABABABAB", [1, 2, 27, 29, 28, 31, 30]]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
