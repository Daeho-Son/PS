from run_test import run_test
from solution import solution


def main():
    test_case = [
        # bridge_length	weight	truck_weights	return
        [2, 10, [7, 4, 5, 6], 8],
        [100, 100, [10], 101],
        [100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 110],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
