import heapq


def solution(operations):
    hq = list()

    for operation in operations:
        if operation[0] == 'I':
            value = int(operation[2:])
            heapq.heappush(hq, value)
        else:
            if not hq:
                continue
            if operation == "D 1":
                hq.remove(max(hq))
            elif operation == "D -1":
                heapq.heappop(hq)
    return [0, 0] if not hq else [max(hq), hq[0]]
