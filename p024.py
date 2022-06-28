from math import factorial

# produces the nth lexicographic permutation of digits 0..m
def sol(n, m):
    n -= 1
    digits = [str(x) for x in range(m+1)]
    result = ""
    place = 0
    for i in range(m, 0, -1):
        digitIndex = int((n-place)/factorial(i))
        place += digitIndex * factorial(i)
        result += digits.pop(digitIndex)
        # print(i, digitIndex, result, digits)
        # print(place)
    result += digits[0]
    return result

if __name__ == "__main__":
    assert sol(1, 2) == "012"
    assert sol(2, 2) == "021"
    assert sol(3, 2) == "102"
    assert sol(4, 2) == "120"
    assert sol(5, 2) == "201"
    assert sol(6, 2) == "210"
    print(sol(10**6, 9))