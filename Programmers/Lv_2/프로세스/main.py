from solution import solution


def main():
    priorities_list = [
        [2, 1, 3, 2],
        [1, 1, 9, 1, 1, 1]
    ]
    location_list = [
        2,
        0
    ]
    result_list = [
        1,
        5
    ]

    for priorities, location, result in zip(priorities_list, location_list, result_list):
        print('#', priorities, location, result)
        if (answer := solution(priorities, location)) == result:
            print(answer, "OK")
        else:
            print(answer, "KO")
        print()

if __name__ == '__main__':
    main()
