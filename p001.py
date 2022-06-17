# sum of an arithmetic series with equal stepsize and start number
# which does not exceed max
def sum(max, start):
    max -= 1
    numTerms = int(max/start)
    finalTerm = start * numTerms
    return numTerms / 2 * (start + finalTerm)

def sol(n):
    return sum(n, 3) + sum(n, 5) - sum(n, 15)

if __name__ == "__main__":
    assert sol(10) == 23
    print(sol(1000))