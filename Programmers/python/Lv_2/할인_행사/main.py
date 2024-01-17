from solution import solution


def main():
    want_list = [
        ["banana", "apple", "rice", "pork", "pot"],
        ["apple"]
    ]
    number_list = [
        [3, 2, 2, 2, 1],
        [10]
    ]
    discount_list = [
        ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"],
        ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
    ]
    answer_list = [
        3,
        0
    ]

    for want, number, discount, answer in zip(want_list, number_list, discount_list, answer_list):
        print('#', want, number, discount, answer)
        if (result := solution(want, number, discount)) == answer:
            print(result, "OK")
        else:
            print(result, "KO")
        print()


if __name__ == '__main__':
    main()
