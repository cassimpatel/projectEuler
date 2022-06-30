primeCheck = {}

def isPrime(n):
    if n < 2:
        return False
    if n in primeCheck:
        return primeCheck[n]
    primeCheck[n] = False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    primeCheck[n] = True
    return True
    
# finds a*b such that |a|,|b|<=1000 and n^2+an+b produces the largest number of primes for consecutive n
# for simplicity we let parameter n represent the upper bound for |a|,|b|
def sol(bound):
    maxA, maxB, maxPrimeLen = -bound, -bound, 0
    for a in range(-bound, bound+1):
        if (a+bound) % 100 == 0:
            print("{:.2f}".format((a+bound)/(2*bound)*100), "%")
        for b in range(-bound, bound+1):
            n = 0
            while isPrime(n**2 + a*n + b):
                n += 1
            if n >= maxPrimeLen:
                maxA, maxB, maxPrimeLen = a, b, n
                # print(a, b, n)
    return maxA * maxB

if __name__ == "__main__":
    assert sol(1601) == -126479
    print(sol(1000))