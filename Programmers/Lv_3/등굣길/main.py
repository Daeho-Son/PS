from solution import solution
from run_test import run_test


def main():
    test_case = [
        # m	n	puddles	return
        [4,	3,	[[2, 2]],	4]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()