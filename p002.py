# sum of even fibonacci numbers not exceeding n
def sol(n):
    x, y, z = 0, 1, 2
    sum = 0
    while z < n:
        sum += z
        x = y+z
        y = x+z
        z = x+y
    return sum

if __name__ == "__main__":
    assert sol(100) == 44
    print(sol(4* 10**6))
    