from run_test import run_test
from solution import solution


def main():
    test_case = [
        # wallpaper	result
        [[".#...", "..#..", "...#."], [0, 1, 3, 4]],
        [["..........", ".....#....", "......##..", "...##.....", "....#....."], [1, 3, 5, 8]],
        [[".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."], [0, 0, 7, 9]],
        [["..", "#."], [1, 0, 2, 1]],
    ]
    run_test(test_case, solution)


if __name__ == '__main__':
    main()
