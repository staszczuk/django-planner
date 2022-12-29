def prev_month(year, month):
    if month == 1:
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
    if month == 12:
        return {
            'year': year + 1,
            'month': 1,
        }
    else:
        return {
            'year': year,
            'month': month + 1,
        }
