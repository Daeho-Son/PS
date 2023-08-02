def solution(cards1, cards2, goal):
    cards1 = list(reversed(cards1))
    cards2 = list(reversed(cards2))
    for g in goal:
        if cards1 and cards1[-1] == g:
            cards1.pop()
        elif cards2 and cards2[-1] == g:
            cards2.pop()
        else:
            return "No"
    return "Yes"
