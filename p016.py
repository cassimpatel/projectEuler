# computes 2^n recursively
def power(n):
    if n == 1:
        return 2
    if n % 2 == 0:
        return power(n/2) ** 2
    else:
        return power(n-1) * 2

# finds sum of digits of 2^n
def sol(n):
    result = power(n)
    digitSum = sum([int(x) for x in str(result)])
    return digitSum

if __name__ == "__main__":
    assert sol(15) == 26
    print(sol(1000))