from solution import solution


def main():
    clothes = [
        [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]],
        [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"]],
        [["yellow_hat", "headgear"]],
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"], ["green_turban", "headgear"], ["yellow_hat", "headgear"]],
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["green_turban", "headgear"], ["yellow_hat", "headgear"], ["smoky_pants", "pants"]]
    ]
    answer = [
        5,
        3,
        3,
        1,
        11,
        17
    ]

    for c, a in zip(clothes, answer):
        print(f'##########\n{a}, {c}')
        if (result := solution(c)) == a:
            print("OK", result)
        else:
            print("KO", result)
        print()

if __name__ == '__main__':
    main()
