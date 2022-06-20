from collections import defaultdict
import math

# get the number of factors of a number n
def numFactors(n):
    # first we calculate the prime factorisation
    primes = defaultdict(int)
    while n > 1:
        for i in range(2, int(n+1)):
            if n % i == 0:
                primes[i] += 1
                n /= i
                break
                
    # combinatorially calculate number of factors
    combos = [x+1 for x in primes.values()]
    return math.prod(combos)

# gets first triangle number to have over n divisors
def sol(n):
    i = 0
    while True:
        if i > 0 and i % 1000 == 0:
            print("Iteration", i)
        triangleNum = (i)*(i+1)/2
        if numFactors(triangleNum) > n:
            return triangleNum
        i += 1
        
if __name__ == "__main__":
    assert sol(5) == 28
    print(sol(500))