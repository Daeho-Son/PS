from run_test import run_test
from solution import solution


def main():
    test_case = [
        # tickets	return
        [[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]], ["ICN", "JFK", "HND", "IAD"]],
        [[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]], ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]],
        [[["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]], ["ICN", "A", "C", "A", "B", "D"]]

    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
