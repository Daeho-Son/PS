from solution import solution


def main():
    phone_book_list = [
        ["119", "97674223", "1195524421"],
        ["123", "456", "789"],
        ["12", "123", "1235", "567", "88"],
        ["12", "135", "1235", "567", "88"]
    ]
    result_list = [
        False,
        True,
        False,
        False
    ]

    for phone_book, result in zip(phone_book_list, result_list):
        print('#', phone_book, result)
        if (answer := solution(phone_book)) == result:
            print(answer, "OK")
        else:
            print(answer, "KO")
        print()


if __name__ == '__main__':
    main()
