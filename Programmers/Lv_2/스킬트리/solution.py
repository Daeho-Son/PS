from collections import deque


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_order = deque(skill)
        for skl in skill_tree:
            if skl in skill_order:
                if skl != skill_order.popleft():
                    break
        else:
            answer += 1
    return answer


# def is_right_skill_tree(skill, skill_tree):
#     skill_indices = [27] * len(skill)
#     for i, s in enumerate(skill):
#         if s in skill_tree:
#             skill_indices[i] = skill_tree.index(s)
#     skill_indices = list(filter(lambda x: x != -1, skill_indices))
#     if sorted(skill_indices) != skill_indices:
#         return False
#     return True
#
#
# def solution(skill, skill_trees):
#     answer = 0
#     for skill_tree in skill_trees:
#         if is_right_skill_tree(skill, skill_tree):
#             answer += 1
#     return answer
