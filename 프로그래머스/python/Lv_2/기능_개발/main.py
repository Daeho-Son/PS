from solution import solution


def main():
    progresses = [
        [93, 30, 55],
        [95, 90, 99, 99, 80, 99],
        [90, 90, 90, 90]
    ]
    speeds = [
        [1, 30, 5],
        [1, 1, 1, 1, 1, 1],
        [30, 1, 1, 1]
    ]
    answers = [
        [2, 1],
        [1, 3, 2],
        [1, 3]
    ]

    for progress, speed, answer in zip(progresses, speeds, answers):
        print('#', progress, speed, answer)
        if (result := solution(progress, speed)) == answer:
            print(result, "OK")
        else:
            print(result, "KO")
        print()

if __name__ == '__main__':
    main()
