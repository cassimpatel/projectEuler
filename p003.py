import math

# finds smallest prime factor of n
def minFactor(n):
    for i in range(2, math.ceil(n**0.5)):
        if n % i == 0:
            return i
    return n

# maximum prime factor of n
def sol(n):
    while n > 1:
        factor = minFactor(n)
        n /= factor
    return factor

if __name__ == "__main__":
    assert sol(13195) == 29
    print(sol(600851475143))