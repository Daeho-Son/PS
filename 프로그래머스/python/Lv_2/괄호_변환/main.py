from run_test import run_test
from solution import solution_2


def main():
    test_case = [
        ["(()())()", "(()())()"],
        [")(", "()"],
        ["()))((()", "()(())()"],
        ["()", "()"]
    ]
    run_test(test_case, solution_2)


if __name__ == '__main__':
    main()
