def main():
    n = int(input())
    houses = sorted(map(int, input().split()))
    return houses[(n - 1) // 2]


if __name__ == '__main__':
    print(main())
