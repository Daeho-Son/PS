from run_test import run_test
from solution import solution


def main():
    test_case = [
        # new_id	result
        ["...!@BaT#*..y.abcdefghijklm", "bat.y.abcdefghi"],
        ["z-+.^.", "z--"],
        ["=.=", "aaa"],
        ["123_.def", "123_.def"],
        ["abcdefghijklmn.p", "abcdefghijklmn"],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
