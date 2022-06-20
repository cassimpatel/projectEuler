# finds difference between sum of squares and squared sum
def sol(n):
    sumSquares = (n)*(n+1)*(2*n+1)/6
    squaredSum = ((n)*(n+1)/2)**2
    return abs(sumSquares - squaredSum)

if __name__ == "__main__":
    assert sol(10) == 2640
    print(sol(100))