from heapq import heapify, heappop, heappush


def solution(scoville, k):
    answer = 0
    heapify(scoville)
    while len(scoville) >= 2:
        first = heappop(scoville)
        if first >= k:
            break
        second = heappop(scoville)
        heappush(scoville, first + second * 2)
        answer += 1
    return answer if heappop(scoville) >= k else -1
