from math import factorial

# number of unique paths from top right to bottom left of an nxn grid
def sol(n):
    # we must go right n times and down n times giving a 2n long sequence e.g. rdrddrr...d
    # n of these are d, the others are r
    # combinatorially, we choose n of 2n to be r then the rest are d, hence C(2n, n) options
    result = factorial(2*n) / factorial(n) ** 2
    return int(result)
    

if __name__ == "__main__":
    assert sol(2) == 6
    print(sol(20))