import math

# gets the n'th prime number
def sol(n):
    MAXNUM = 10**6
    sieve = set(range(2, MAXNUM+1))
    for i in range(2, int(math.sqrt(MAXNUM)) + 1):
        if i not in sieve:
            continue
        sieve = set([x for x in sieve if x%i!=0])
        sieve.add(i)
    if len(sieve) < n-1:
        return "PRIME NOT FOUND IN GIVEN RANGE"
    # print(sorted(list(sieve)))
    return sorted(list(sieve))[n-1]

if __name__ == "__main__":
    assert sol(6) == 13
    print(sol(10001))