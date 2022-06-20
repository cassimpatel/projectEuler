import math

# sum of primes below n
def sol(n):
    sieve = set(range(2, n))
    for i in range(2, int(math.sqrt(n)) + 1):
        if i % 10 == 0:
            print("Iteration", i, "of", int(math.sqrt(n)))
        if i not in sieve:
            continue
        sieve = set([x for x in sieve if x%i!=0])
        sieve.add(i)
    return sum(sieve)

if __name__ == "__main__":
    assert sol(10) == 17
    print(sol(2*10**6))