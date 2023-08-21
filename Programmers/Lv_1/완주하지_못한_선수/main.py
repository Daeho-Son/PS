from solution import solution
from run_test import run_test


def main():
    test_case = [
        # participant	completion	return
        [["leo", "kiki", "eden"], ["eden", "kiki"], "leo"],
        [["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"], "vinko"],
        [["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"], "mislav"],
    ]

    run_test(test_case, solution)


if __name__ == '__main__':
    main()
