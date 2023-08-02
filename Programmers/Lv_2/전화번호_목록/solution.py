def solution(phone_book):
    _dict = dict()
    for phone_number in phone_book:
        _dict[phone_number] = 0
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            if phone_number[:i] in _dict.keys():
                return False
    return True


# def solution(phone_book):
#     phone_book.sort()
#     for p1, p2 in zip(phone_book, phone_book[1:]):
#         print(p1, p2)
#         if p2.startswith(p1):
#             return False
#     return True


# 통과
# def solution(phone_book):
#     phone_book.sort()
#     for pb_index in range(len(phone_book) - 1):
#         if phone_book[pb_index + 1].startswith(phone_book[pb_index]):
#             return False
#     return True


# 효율성 테스트 3, 4 시간 초과
# def solution(phone_book):
#     for a in phone_book:
#         for b in phone_book:
#             if a != b and b.startswith(a):
#                 return False
#     return True
