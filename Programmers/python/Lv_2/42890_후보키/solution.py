'''
# 시도 1. (성공)
## 방법
  1. 0, 1, 2, 3, 4, 01, 02, 03, 04, ... 0123 의 조합을 전부 딕셔너리로 저장한다.
  2. 해당 조합의 개수가 튜플의 개수와 같지 않으면, 모든 튜플을 식별할 수 없으므로 무시한다.
  3. 키 조합이 유일성을 만족한다면, 키를 한 개씩 제거하며 최소성을 만족하는 지 확인한다.
    - 예를 들어 키가 012라면, 0, 1, 2, 01, 02, 12
    3.1. 키 조합에서 한 개씩 제거한 조합을 set 변수에 담고 answer와 교집합이 있는 지 확인
  4. answer의 개수를 반환한다.
'''
from itertools import combinations


def solution(relation):
    answer = set()
    column_count = len(relation[0])
    row_count = len(relation)

    relation_comb_keys = []
    for i in range(1, column_count+1):
        relation_comb_keys.extend(list(combinations([i for i in range(column_count)], i)))

    relation_comb = dict()
    for key in relation_comb_keys:
        relation_comb[key] = set()

    for r in relation:
        relation_comb_values = []
        for i in range(1, column_count + 1):
            relation_comb_values.extend(list(combinations(r, i)))
        for k, v in zip(relation_comb_keys, relation_comb_values):
            relation_comb[k].add(v)

    for k, v in sorted(relation_comb.items(), key=lambda x: len(x)):
        if len(v) != row_count:
            continue
        tmp_keys = set()
        for d in range(1, len(k)):
            tmp_keys.update(list(combinations(k, d)))
        if not tmp_keys & answer:
            answer.add(k)
    return len(answer)
