"""
# 조건
  - array_a의 모든 숫자를 나눌 수 있고, array_b의 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a
  - array_b의 모든 숫자를 나눌 수 있고, array_a의 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a

# 반환값
  - 위 조건 중 하나를 만족하는 가장 큰 양의 정수 a
  - 조건을 만족하는 a가 없다면 0
"""

"""
# 시도 2. (성공)
## 방법
  - math.gcd 함수를 사용해서 구현
"""
from math import gcd


def solution(array_a, array_b):
    answer = []
    gcd_a = array_a[0]
    for a_n in array_a[1:]:
        gcd_a = gcd(gcd_a, a_n)
    if not any(b_n % gcd_a == 0 for b_n in array_b):
        answer.append(gcd_a)

    gcd_b = array_b[0]
    for b_n in array_b[1:]:
        gcd_b = gcd(gcd_b, b_n)
    if not any(a_n % gcd_b == 0 for a_n in array_a):
        answer.append(gcd_b)
    return max(answer) if answer else 0


# """
# # 시도 1. (실패) 시간 초과
# ## 방법
#   - 모든 공약수를 구하고, 상대방의 숫자에 해당 공약수가 겹치는 게 있는 지 체크한다.
#   - list의 길이가 500,000이고, 숫자가 100,000,000이기 때문에 공약수를 구하는 과정에서 시간 초과 발생
# """
# def get_divisor(target_n):
#     divisor = set()
#     n = 1
#     while target_n >= n ** 2:
#         if target_n % n == 0:
#             divisor.add(n)
#             divisor.add(target_n // n)
#         n += 1
#     return divisor
#
#
# def solution(array_a, array_b):
#     answer = []
#     divisors_a = []
#     for a_n in array_a:
#         divisors_a.append(get_divisor(a_n))
#     common_divisors_a = set()
#     for divisor_a in divisors_a:
#         common_divisors_a = divisor_a if not common_divisors_a else common_divisors_a & divisor_a
#
#     divisors_b = []
#     for b_n in array_b:
#         divisors_b.append(get_divisor(b_n))
#     common_divisors_b = set()
#     for divisor_b in divisors_b:
#         common_divisors_b = divisor_b if not common_divisors_b else common_divisors_b & divisor_b
#     for cda in common_divisors_a:
#         if any([b_n % cda == 0 for b_n in array_b]):
#             continue
#         answer.append(cda)
#
#     for cdb in common_divisors_b:
#         if any([a_n % cdb == 0 for a_n in array_a]):
#             continue
#         answer.append(cdb)
#     return max(answer) if answer else 0
