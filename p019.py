from datetime import datetime

# finds the number of sundays that fell on the first month during the nth century
def sol(n):
    result = 0
    for y in range((n-1)*100 + 1, n*100 + 1):
        for m in range(1, 13):
            startOfMonth = datetime(year=y, month=m, day=1)
            if startOfMonth.weekday() == 6:
                result += 1
    return result

if __name__ == "__main__":
    print(sol(20))