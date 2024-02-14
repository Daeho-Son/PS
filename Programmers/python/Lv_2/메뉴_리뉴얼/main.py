from run_test import run_test
from solution import solution


def main():
    test_case = [
        # orders	course	result
        [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4], ["AC", "ACDE", "BCFG", "CDE"]],
        [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5], ["ACD", "AD", "ADE", "CD", "XYZ"]],
        [["XYZ", "XWY", "WXA"], [2, 3, 4], ["WX", "XY"]],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
