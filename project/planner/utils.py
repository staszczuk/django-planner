def prev_month(year, month):
    if year == 1 and month == 1:
        return {
            'year': year,
            'month': month,
        }
    elif month == 1:
        return {
            'year': year - 1,
            'month': 12,
        }
    else:
        return {
            'year': year,
            'month': month - 1,
        }


def next_month(year, month):
    if year == 9999 and month == 11:
        return {
            'year': year,
            'month': month,
        }
    elif month == 12:
        return {
            'year': year + 1,
            'month': 1,
        }
    else:
        return {
            'year': year,
            'month': month + 1,
        }
