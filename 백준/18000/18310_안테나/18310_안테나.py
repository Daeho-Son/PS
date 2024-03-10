"""
시도 2. (성공)
## 방법
  - 집들을 정렬한 다음, 가운데 있는 값을 반환한다.
    1. 집들의 숫자를 정렬
    2. 홀수인 경우, 가운데 있는 값을 반환
    3. 짝수인 경우, 가운데 값 둘 중 어떤 걸 선택해도 상관없지만 그 중 작은 값인 왼쪽 값을 반환
"""
def main():
    n = int(input())
    houses = sorted(map(int, input().split()))
    return houses[(n - 1) // 2]


if __name__ == '__main__':
    print(main())


# """
# 시도 1. (실패)
# ## 방법
#   - 처음 집과 마지막 집의 가운데 숫자를 구하고, (1 5 7 9 의 경우, 1 + 9 // 2를 통해 가운데 값인 5를 구한다.)
#     가운데 값들과의 차이가 가장 적은 값을 반환한다.
#
# ## 문제점
#   - 주어진 집들의 숫자를 신경쓰지 않고 처음 집과 마지막 집의 가운데 값을 구한게 문제점
#   - 1 3 4 12의 경우 가운데 값은 6이다. 이 경우, 4가 반환되기 때문에 실패
# """
# def main():
#     n = int(input())
#     houses = sorted(map(int, input().split()))
#     optimum_distance = mid_number = (houses[0] + houses[-1]) // 2
#     answer = houses[0]
#     for number in houses:
#         if abs(mid_number - number) >= optimum_distance:
#             return answer
#         optimum_distance = abs(mid_number - number)
#         answer = number
#     return answer
#
#
# if __name__ == '__main__':
#     print(main())
