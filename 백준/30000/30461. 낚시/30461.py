"""
# 시도 1. 구간 합 응용
## 방법
  - `(1, b) + ... + (a, b) + (1, b - 1) + ... + (a - 1, b - 1) + ...` 의 방식으로 합을 구하는 문제
  - 값을 구할 때마다 하나씩 더해서 구한다면 N=2000, M=2000, a=2000, b=2000, Q=300000 일 경우,
    - 1 + 2 + 3 + ... + 2000 을 300000번. 즉, (2000 * 2001 / 2) * 300000 =
  - `구간합을 구하는 방식과 비슷하게 (i - 1, j - 1) + (i - 1, j) + 현재 값` 을 배열에 저장해놓는다.
  -
"""
import sys

input = sys.stdin.readline


def solution():
    n, m, q = map(int, input().rstrip().split())
    section_sum_triangle = [[0] * (m + 1) for _ in range(n + 1)]
    for y in range(1, n + 1):
        for x, fish_count in enumerate(map(int, input().rstrip().split())):
            x += 1
            section_u = section_sum_triangle[y-1][x]
            section_ul = section_sum_triangle[y-1][x-1]
            section_uul = section_sum_triangle[y-2][x-1]
            if y - 2 < 0 or x - 1 < 0:
                section_uul = 0
            section_sum_triangle[y][x] = fish_count + section_u + section_ul - section_uul
    for _ in range(q):
        w, p = map(int, input().split())
        print(section_sum_triangle[w][p])


def main():
    solution()


if __name__ == '__main__':
    main()
