from solution import solution


def main():
    s_list = [
        "{{2},{2,1},{2,1,3},{2,1,3,4}}",
        "{{1,2,3},{2,1},{1,2,4,3},{2}}",
        "{{20,111},{111}}",
        "{{123}}",
        "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    ]
    answer_list = [
        [2, 1, 3, 4],
        [2, 1, 3, 4],
        [111, 20],
        [123],
        [3, 2, 4, 1]
    ]

    for s, answer in zip(s_list, answer_list):
        print('#', s, answer)
        if (result := solution(s)) == answer:
            print(result, "OK")
        else:
            print(result, "KO")
        print()


if __name__ == '__main__':
    main()
