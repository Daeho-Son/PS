from run_test import run_test
from solution import solution


def main():
    test_case = [
        # keymap	targets	result
        [["ABACD", "BCEFD"], ["ABCD", "AABB"], [9, 4]],
        [["AA"], ["B"], [-1]],
        [["AGZ", "BSSS"], ["ASA", "BGZ"], [4, 6]],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
