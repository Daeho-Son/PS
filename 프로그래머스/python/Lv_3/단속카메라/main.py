from run_test import run_test
from solution import solution


def main():
    test_case = [
        # routes	return
        [[[-20, -15], [-14, -5], [-18, -13], [-5, -3]], 2],
        [[[2, 2], [0, 1], [-10, 9]], 2],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
