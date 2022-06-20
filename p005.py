import math

# gets list of all prime factors of n
def primeFactors(n):
    factors = []
    while n > 1:
        for i in range(2, int(n+1)):
            if n % i == 0:
                factors.append(i)
                n /= i
                break
    return factors

# combines factor list b into a, ignoring repetitions in b
def combineFactorLists(a, b):
    a = a.copy()
    for i in set(b):
        if a.count(i) >= b.count(i):
            continue
        else:
            extraInstances = b.count(i) - a.count(i)
            a += [i for x in range(extraInstances)]
    return a

# gets smallest number that can be divided by 1...n
def sol(n):
    factors = []
    for i in range(n, 1, -1):
        #print(i, primeFactors(i))
        factors = combineFactorLists(factors, primeFactors(i))
        #print(factors)
    return math.prod(factors)

if __name__ == "__main__":
    assert sol(10) == 2520
    print(sol(1000))