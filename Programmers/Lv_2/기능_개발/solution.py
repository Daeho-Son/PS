def solution(progresses, speeds):
    answer = list()
    while progresses:
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.remove(progresses[0])
            speeds.remove(speeds[0])
            count += 1
        progresses = [n + speeds[i] for i, n in enumerate(progresses)]
        if count:
            answer.append(count)
    return answer
