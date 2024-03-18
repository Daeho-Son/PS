"""
# 시도 1. (성공)
## 방법.
  - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]에서 1은 인덱스 1이다. 9는 인덱스 9이다.
  - [1, 2, 4]에서 1은 인덱스 0이다. 2는 인덱스 1이다. 3은 인덱스 2이다.
  - 위 조건을 만족 시키기 위해 매번 n에 -1을 해주어 값을 찾는다.
"""
def solution(n):
    answer = ''
    n = int(n)
    n -= 1
    while n >= 3:
        n, m = divmod(n, 3)
        answer = '124'[m % 3] + answer
        n -= 1
    answer = '124'[n % 3] + answer
    return answer
