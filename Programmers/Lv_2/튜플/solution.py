from collections import Counter
import re


def solution(s):
    n_counter = Counter(re.findall(r'\d+', s))
    return [int(t[0]) for t in sorted(n_counter.items(), key=lambda x: x[1], reverse=True)]
