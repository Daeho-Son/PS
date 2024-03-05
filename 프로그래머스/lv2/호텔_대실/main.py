from run_test import run_test
from solution import solution


def main():
    test_case = [
        # book_time	result
        [[["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]], 3],
        [[["09:10", "10:10"], ["10:20", "12:20"]], 1],
        [[["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]], 3],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
