def isValid(today, afterday, add_month):
    today_year, today_month, today_day = list(map(int, today.split(".")))
    prev_year, prev_month, prev_day = list(map(int, afterday.split(".")))

    print(today, afterday, add_month)

    prev_year += add_month // 12
    prev_month += add_month % 12

    if prev_month > 12:
        prev_month -= 12
        prev_year += 1

    if prev_day - 1 == 0:
        prev_month -= 1
        prev_day = 28
    else:
        prev_day = prev_day - 1

    print(today_year, today_month, today_day)
    print(prev_year, prev_month, prev_day)
    if prev_year > today_year:
        return True
    elif prev_year == today_year:
        if prev_month > today_month:
            return True
        elif prev_month == today_month:
            if prev_day >= today_day:
                return True
            
    
    return False


def solution(today, terms, privacies):
    answer = []
    
    term = {}
    for value in terms:
        alpha, month = value.split()
        term[alpha] = int(month)
    print(term)
    for idx, value in enumerate(privacies):
        prev_day, month = value.split(" ")
        if not isValid(today, prev_day, int(term[month])):
            answer.append(idx + 1)


    
    return answer