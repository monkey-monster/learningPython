
def is_leap(year):
    r = False
    if year % 4 == 0:
        r = True
        if year % 100 == 0:
            if year % 400 != 0:
                r = False
    return r
print( is_leap(4))
print(is_leap(200))

def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)