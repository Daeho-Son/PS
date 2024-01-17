from solution import solution


def main():
    str1_list = [
        "FRANCE",
        "handshake",
        "aa1+aa2",
        "E=M*C^2"
    ]
    str2_list = [
        "french",
        "shake hands",
        "AAAA12",
        "e=m*c^2"
    ]
    answer_list = [
        16384,
        65536,
        43690,
        65536,
    ]

    for str1, str2, answer in zip(str1_list, str2_list, answer_list):
        print('#', str1, str2, answer)
        if (result := solution(str1, str2)) == answer:
            print(result, "OK")
        else:
            print(result, "KO")
        print()


if __name__ == '__main__':
    main()
