def solution(N, stages):
    total_user = len(stages)
    user_count = list([0] * (N+1))
    answer = dict()
    for i in stages:
        user_count[i-1] += 1
    user_count = user_count[:-1]
    for i, _count in enumerate(user_count):
        if total_user:
            answer[i+1] = _count / total_user
        else:
            answer[i+1] = 0
        total_user -= _count
    return sorted(answer, key=lambda x: -answer[x])


# from collections import deque
#
#
# def solution(N, stages):
#     count_list = list([0] * (N+1))
#     acc_list = deque()
#     for stage in stages:
#         count_list[stage-1] += 1
#     for c_index in range(N, -1, -1):
#         if not acc_list:
#             acc_list.appendleft(count_list[c_index])
#         else:
#             acc_list.appendleft(acc_list[0] + count_list[c_index])
#
#     answer = list()
#     for i, _zip in enumerate(zip(count_list[:-1], list(acc_list)[:-1])):
#         count, acc = _zip
#         if acc:
#             answer.append((i+1, count / acc))
#         else:
#             answer.append((i+1, 0))
#     answer.sort(key=lambda x: -x[1])
#     return [first for first, _ in answer]


# def solution(N, stages):
#     acc_list = list([0] * (N+1))
#     answer = list()
#     for n in range(N+1, 0, -1):
#         _acc = stages.count(n) if n == N+1 else acc_list[n]+ stages.count(n)
#         acc_list[n-1] = _acc
#
#         if _acc:
#             answer.append((n, stages.count(n) / _acc))
#         else:
#             answer.append((n, 0))
#     return [first for first, _ in sorted(answer[1:], key=lambda x: (-x[1], x[0]))]


## 시간이 최악
# def solution(N, stages):
#     stats = dict()
#     for i in range(N+1, 0, -1):
#         if not stats.get(i + 1):
#             stats[i] = stages.count(i)
#         else:
#             stats[i] = stats.get(i + 1) + stages.count(i)
#     print(stats)
#     answer = list()
#     for _key, _value in stats.items():
#         _fail = stages.count(_key) / _value if _value else 0
#         if _key != N + 1:
#             answer.append((_key, _fail))
#     answer.sort(key=lambda x: (-x[1], x[0]))
#     return [first for first, second in answer]


# from collections import deque
#
#
# def solution(N, stages):
#     stages_stats = dict(zip(range(1, N+2), [0] * (N + 1)))
#     for stage in stages:
#         stages_stats[stage] += 1
#     pass_though = deque()
#     for staged in reversed(stages_stats.keys()):
#         if not pass_though:
#             pass_though.appendleft(stages_stats[staged])
#         else:
#             pass_though.appendleft(pass_though[0] + stages_stats[staged])
#
#     answer = list()
#     for i, _zip in enumerate(zip(list(stages_stats.values())[:-1], list(pass_though)[:-1])):
#         _current, _pass = _zip
#         if _pass == 0:
#             answer.append((i + 1, 0))
#         else:
#             answer.append((i + 1, _current / _pass))
#     answer.sort(key=lambda x: -x[1])
#     return [first for first, second in answer]
