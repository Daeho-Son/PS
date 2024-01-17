from solution import solution


def main():
    cards1_list = [
        ["i", "drink", "water"],
        ["i", "water", "drink"]
    ]
    cards2_list = [
        ["want", "to"],
        ["want", "to"]
    ]
    goal_list = [
        ["i", "want", "to", "drink", "water"],
        ["i", "want", "to", "drink", "water"]
    ]
    answer_list = [
        "Yes",
        "No"
    ]

    for cards1, cards2, goal, answer in zip(cards1_list, cards2_list, goal_list, answer_list):
        print('#', cards1, cards2, goal, answer)
        if (result := solution(cards1, cards2, goal)) == answer:
            print(result, "OK")
        else:
            print(result, "KO")
        print()


if __name__ == '__main__':
    main()
