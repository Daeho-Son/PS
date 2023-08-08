from solution import solution
from run_test import run_test


def main():
    # record	result
    test_case = [
        [["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"],
         ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]]
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
