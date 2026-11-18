def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None

    gunler = [31, 28, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29

    return gunler[month - 1]


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yil = test_years[i]
    ay = test_months[i]

    sonuc = days_in_month(yil, ay)

    print(yil, ay, "->", sonuc)
