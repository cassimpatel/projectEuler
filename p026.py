# returns number of digits in recurring cycle of 1/n:
def cycleLen(n):
    while True:
        if n % 2 == 0:
            n /= 2
        elif n % 5 == 0:
            n /= 5
        else:
            break
    i, n = 9, int(n)
    while True:
        if i % n == 0:
            break
        i = i*10 + 9
    return len(str(i))

# returns  some d < n for which 1/d contains the longest recurring cycle in its decimal fraction part
def sol(n):
    d, dLen = 1, 0
    for i in range(1, n):
        if cycleLen(i) > dLen:
            d, dLen = i, cycleLen(i)
    return d

if __name__ == "__main__":
    assert sol(10) == 7
    print(sol(1000))