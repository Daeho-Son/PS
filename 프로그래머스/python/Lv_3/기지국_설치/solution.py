def solution(n, stations, w):
    answer = 0
    w_range = 2 * w + 1
    prev_end_w = 0
    stations.append(n + 1 + w)
    for station in stations:
        current_start_w = station - w
        current_end_w = station + w
        _div, _mod = divmod(current_start_w - prev_end_w - 1, w_range)
        answer += _div if not _mod else _div + 1
        prev_end_w = current_end_w
    return answer
