import datetime as dt

'''
https://projecteuler.net/problem=19
Counting Sundays
'''


def main() -> int:
    '''Returns the number of sundays in the 20th century.'''
    START = dt.date(1901, 1, 1)
    END = dt.date(2000, 12, 31)

    DURATION = (END - START).days

    sundays = (START+dt.timedelta(days=k) for k in range(DURATION+1)
               if is_first_sunday_of_month(START+dt.timedelta(days=k)))
    result = sum(1 for sd in sundays)

    return result


def is_first_sunday_of_month(date: dt.date) -> bool:
    '''Checks if a given date is a sunday and the first day of the month.'''
    result = (date.weekday() == 6 and date.day == 1)
    return result


if __name__ == '__main__':
    result = main()
    print(result)
