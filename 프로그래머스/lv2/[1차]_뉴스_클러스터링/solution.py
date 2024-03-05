# def solution(str1, str2):
#     str1_set = list(str1[i].lower() + str1[i + 1].lower() for i in range(len(str1) - 1)
#                     if str1[i].isalpha() and str1[i + 1].isalpha())
#     str2_set = list(str2[i].lower() + str2[i + 1].lower() for i in range(len(str2) - 1)
#                     if str2[i].isalpha() and str2[i + 1].isalpha())
#
#     if str1_set == str2_set:
#         return 65536
#
#     inter = set(str1_set) & set(str2_set)
#     union = set(str1_set) | set(str2_set)
#     inter_set = list()
#     for s in inter:
#         min_cwount = min(str1_set.count(s), str2_set.count(s))
#         inter_set.extend([s] * min_count)
#     union_set = list()
#     for s in union:
#         max_count = max(str1_set.count(s), str2_set.count(s))
#         union_set.extend([s] * max_count)
#     return int((len(inter_set) / len(union_set)) * 65536)


def solution(str1, str2):
    str1_set = [str1[i:i + 2].lower() for i in range(0, len(str1) - 1)
                if str1[i:i + 2].isalpha()]
    str2_set = [str2[i:i + 2].lower() for i in range(0, len(str2) - 1)
                if str2[i:i + 2].isalpha()]

    if str1_set == str2_set:
        return 65536

    inter = set(str1_set) & set(str2_set)
    union = set(str1_set) | set(str2_set)

    inter_count = [min(str1_set.count(s), str2_set.count(s)) for s in inter]
    union_set = [max(str1_set.count(s), str2_set.count(s)) for s in union]
    return int(sum(inter_count) / sum(union_set) * 65536)
