from math import factorial

# finds the sum of the digits in n!
def sol(n):
    result = factorial(n)
    return sum([int(x) for x in str(result)])

if __name__ == "__main__":
    assert sol(10) == 27
    print(sol(100))