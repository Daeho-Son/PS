# 투 포인터
import sys
input=sys.stdin.readline


def main():
    answer = 0
    start_n = 0
    total_ns = 0
    n = int(input())
    for number in range(1, n + 1):
        total_ns += number
        while total_ns > n:
            total_ns -= start_n
            start_n += 1
        if total_ns == n:
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()
