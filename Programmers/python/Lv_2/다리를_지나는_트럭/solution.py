from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    total_weight = 0
    while truck_weights:
        total_weight -= bridge.popleft()
        if truck_weights and total_weight + truck_weights[0] <= weight:
            current_truck_weight = truck_weights.popleft()
            bridge.append(current_truck_weight)
            total_weight += current_truck_weight
        else:
            bridge.append(0)
        answer += 1
    return answer + bridge_length
