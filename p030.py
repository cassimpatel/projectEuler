# gets sum of n'th powers of integer m
def digitPowerSum(n, m):
    return sum([int(x)**n for x in str(m)])
    
# calculates sum of all numbers which can be written as the sum of nth powers of their digits
def sol(n):
    lowerBound = 2**n
    upperBound = 9**n * len(str(9**n))
    result = 0
    for i in range(lowerBound, upperBound + 1):
        if i % 50000 == 0:
            print("{:.2f} %".format((i-lowerBound)/(upperBound-lowerBound)*100))
        if i == digitPowerSum(n, i):
            result += i
    return result

if __name__ == "__main__":
    assert sol(4) == 19316
    print(sol(5))