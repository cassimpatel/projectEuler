# finds the index of the first fibonacci number which contains n digits
def sol(n):
    a, b = 1, 1
    index = 1
    while True:
        if len(str(a)) >= n:
            return index
        a, b = b, a+b
        index += 1
    return 0

if __name__ == "__main__":
    assert sol(2) == 7
    assert sol(3) == 12
    print(sol(1000))