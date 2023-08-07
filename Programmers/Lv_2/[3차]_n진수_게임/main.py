from run_test import run_test
from solution import solution


def main():
    # n	t	m	p	result
    test_case = [
        [2, 4, 2, 1, "0111"],
        [16, 16, 2, 1, "02468ACE11111111"],
        [16, 16, 2, 2, "13579BDF01234567"],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
