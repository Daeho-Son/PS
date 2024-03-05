from solution import solution


def main():
    nums_list = [
        [1, 2, 3, 4],
        [1, 2, 7, 6, 4]
    ]
    answer_list = [
        1,
        4
    ]

    for nums, answer in zip(nums_list, answer_list):
        print('#', nums, answer)
        if (result := solution(nums)) == answer:
            print(result, "OK")
        else:
            print(result, "KO")
        print()


if __name__ == '__main__':
    main()