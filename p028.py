from math import ceil

# each diagonal forms a quadratic sequence
#    4n^2 -4n + 1
#    4n^2 -10n + 7
#    4n^2 -8n + 5
#    4n^2 -6n + 3
# we sum each quadratic sequence to find a new one
#    16n^2 -28 + 16
# then we find the sum of the quadratic sequence for n terms (use formula online)
#    16n(n+1)(2n+1)/6 - 28n(n+1)/2 + 16n
# note: then we minus 3 to account for the overlapping 1 in the centre

# gets sum of numbers on diagonal of an n by n spiral grid
def sol(n):
    # calculate length of diagonal in each direction
    n = ceil(n/2)
    result = 16*n*(n+1)*(2*n+1)/6 - 28*n*(n+1)/2 + 16*n - 3
    return int(result)

if __name__ == "__main__":
    assert sol(5) == 101
    print(sol(1001))