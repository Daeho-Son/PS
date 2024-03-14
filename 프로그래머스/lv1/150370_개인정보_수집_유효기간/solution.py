"""
# 시도 1. (성공)
## 방법
  1. date를 일자로 통일 => YY*12*28 + MM*28 + DD
  2. 현재 일자가 만료 일자보다 크거나 같은 경우 반환.
"""

def date_to_days(date):
    return int(date[:4]) * 12 * 28 + int(date[5:7]) * 28 + int(date[8:])


def is_expiration_privacy(current_days, expiration_days):
    if current_days >= expiration_days:
        return True
    return False

def solution(today, terms, privacies):
    days = date_to_days(today)
    expiration_days_by_terms_type = dict()
    for term in terms:
        term_name = term[:1]
        expiration_days = int(term[2:]) * 28
        expiration_days_by_terms_type[term_name] = expiration_days
    return list(map(lambda x: x[0] + 1, filter(lambda p: is_expiration_privacy(days, date_to_days(p[1][:10]) + expiration_days_by_terms_type.get(p[1][11:])), enumerate(privacies))))