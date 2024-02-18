# 시도 4. 누적합 2 (성공)
def solution(book_time):
    time_table = [0 for _ in range(1450)]
    for b in book_time:
        book_start = int(b[0][:2]) * 60 + int(b[0][3:])
        book_end = int(b[1][:2]) * 60 + int(b[1][3:]) + 10
        time_table[book_start] += 1
        time_table[book_end] -= 1
    for m in range(1, 1439):
        time_table[m] += time_table[m - 1]
    return max(time_table[:1440])


# # 시도 3. 누적합 1 (성공)
# def solution(book_time):
#     time_table = [0 for _ in range(1440)]
#     for b in book_time:
#         book_start = int(b[0][:2]) * 60 + int(b[0][3:])
#         book_end = int(b[1][:2]) * 60 + int(b[1][3:]) + 10 - 1
#         for m in range(book_start, book_end+1):
#             if m > 1439:
#                 break
#             time_table[m] += 1
#     return max(time_table)


# # 시도 2. 힙 (성공)
# from heapq import heappop, heappush
#
#
# def time_to_minutes(time):
#     hour, minutes = map(int, time.split(':'))
#     return hour * 60 + minutes
#
#
# def solution(book_time):
#     book_time_minutes = list(map(lambda x: [time_to_minutes(x[0]), time_to_minutes(x[1])], book_time))
#     book_time_minutes.sort(key=lambda x: x[0])
#
#     heap = []
#     for book_start, book_end in book_time_minutes:
#         print(book_start, book_end)
#         if not heap:
#             heappush(heap, book_end + 10)
#             continue
#         if heap[0] <= book_start:
#             heappop(heap)
#         heappush(heap, book_end + 10)
#     return len(heap)


# # 시도 1. 시작 시간 기준으로 정렬 후, 배열(방)에 직접 할당 (성공)
# def time_to_minutes(time):
#     hour, minutes = map(int, time.split(':'))
#     return hour * 60 + minutes
#
#
# def solution(book_time):
#     rooms = []
#     book_time_minutes = list(map(lambda x: [time_to_minutes(x[0]), time_to_minutes(x[1])], book_time))
#     book_time_minutes.sort(key=lambda x: (x[0], x[1]))
#     for rent_start, rent_end in book_time_minutes:
#         flag = False
#         for i, room in enumerate(rooms):
#             if room <= rent_start:
#                 rooms[i] = rent_end + 10
#                 flag = True
#                 break
#         if not flag:
#             rooms.append(rent_end + 10)
#         print(rent_start, rent_end)
#     return len(rooms)
