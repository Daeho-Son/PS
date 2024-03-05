'''
# 시도 3. 다른 사람 풀이를 분석하고, 다시 풀어보기 - 2
- 최소성 검사하는 코드를 비트 연산자를 내가 작성한 코드보다 쉽게 사용하는 코드
'''
def solution(relation):
    candidate_key_list = []
    tuple_count = len(relation)
    attribute_count = len(relation[0])
    for attribute_combination_bit in range(1, 1 << attribute_count):
        attribute_combination_key_list = set()
        for tuple_index in range(tuple_count):
            attribute_combination_key = tuple()
            for attribute_index in range(attribute_count):
                if attribute_combination_bit & (1 << attribute_index):
                    attribute_combination_key += (relation[tuple_index][attribute_index],)
            attribute_combination_key_list.add(attribute_combination_key)
        if len(attribute_combination_key_list) != tuple_count:
            continue
        for candidate_key in candidate_key_list:
            if (candidate_key & attribute_combination_bit) == candidate_key:
                break
        else:
            candidate_key_list.append(attribute_combination_bit)
    return len(candidate_key_list)

# '''
# # 시도 2. 다른 사람 풀이를 분석하고, 다시 풀어보기 - 1
# ## 방법
#   1. 비트연산으로 속성의 조합을 표현. range(1, 1 << {속성의 개수})
#     - 예를 들어 4개의 속성일 경우, 0001은 학번, 0110은 이름과 전공으로 표현할 수 있다.
#       0001부터 1111까지 표현을 하면 0001부터 1111 (1 0000 - 0001)이므로 range(1, 1 << 4)
#       즉, range(1, 1 << {속성의 개수})이면 0001부터 1111까지 표현할 수 있다.
#   2. 속성의 조합의 개수가 튜플의 개수가 아닐 경우, 무시 (유일성)
#   3. 속성의 조합으로 나올 수 있는 경우에서 이미 후보키 목록에 있는 경우, 무시 (최소성)
#     - 예를 들어 1110인 경우, 0010, 0100, 0110, 1000, 1010, 1100, 1110 중에서 후보키에 있는 경우 최소성을 만족하지 못함
# '''
# def solution(relation):
#     candidate_key_list = []
#     tuple_count = len(relation)
#     attribute_count = len(relation[0])
#     for attribute_combination_bit in range(1, 1 << attribute_count):
#         attribute_combination_key_list = set()
#         for tuple_index in range(tuple_count):
#             attribute_combination_key = tuple()
#             for attribute_index in range(attribute_count):
#                 if attribute_combination_bit & (1 << attribute_index):
#                     attribute_combination_key += (relation[tuple_index][attribute_index],)
#             attribute_combination_key_list.add(attribute_combination_key)
#         if len(attribute_combination_key_list) != tuple_count:
#             continue
#         for attribute_combination_key in range(1, attribute_combination_bit):
#             # 1110으로 만들 수 있는 조합이 아닌 경우, continue
#             if (((1 << attribute_count) - 1) ^ attribute_combination_bit) & attribute_combination_key:
#                 continue
#             if attribute_combination_key in candidate_key_list:
#                 break
#         else:
#             candidate_key_list.append(attribute_combination_bit)
#     return len(candidate_key_list)

# '''
# # 시도 1. (성공)
# ## 방법
#   1. 0, 1, 2, 3, 4, 01, 02, 03, 04, ... 0123 의 조합을 전부 딕셔너리로 저장한다.
#   2. 해당 조합의 개수가 튜플의 개수와 같지 않으면, 모든 튜플을 식별할 수 없으므로 무시한다.
#   3. 키 조합이 유일성을 만족한다면, 키를 한 개씩 제거하며 최소성을 만족하는 지 확인한다.
#     - 예를 들어 키가 012라면, 0, 1, 2, 01, 02, 12
#     3.1. 키 조합에서 한 개씩 제거한 조합을 set 변수에 담고 answer와 교집합이 있는 지 확인
#   4. answer의 개수를 반환한다.
# '''
# from itertools import combinations
#
#
# def solution(relation):
#     answer = set()
#     column_count = len(relation[0])
#     row_count = len(relation)
#
#     relation_comb_keys = []
#     for i in range(1, column_count+1):
#         relation_comb_keys.extend(list(combinations([i for i in range(column_count)], i)))
#
#     relation_comb = dict()
#     for key in relation_comb_keys:
#         relation_comb[key] = set()
#
#     for r in relation:
#         relation_comb_values = []
#         for i in range(1, column_count + 1):
#             relation_comb_values.extend(list(combinations(r, i)))
#         for k, v in zip(relation_comb_keys, relation_comb_values):
#             relation_comb[k].add(v)
#
#     for k, v in sorted(relation_comb.items(), key=lambda x: len(x)):
#         if len(v) != row_count:
#             continue
#         tmp_keys = set()
#         for d in range(1, len(k)):
#             tmp_keys.update(list(combinations(k, d)))
#         if not tmp_keys & answer:
#             answer.add(k)
#     return len(answer)
