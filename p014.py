# dictionary of remembered collatz sequence lengths
collatzLen = {1:1}

# recursively computes collatz len for n, using globally remembered values
def getCollatzSeqLen(n):
    # print(n)
    if n in collatzLen:
        return collatzLen[n]
    nextNum = n/2 if n % 2 == 0 else 3 * n + 1
    collatzLen[n] = getCollatzSeqLen(nextNum) + 1
    return collatzLen[n]

# computes starting number under n with the longest collatz sequence
def sol(n):
    maxStartNum = 1
    maxSeqLen = 1
    for i in range(1, n):
        if i % 50000 == 0:
            print(i/n*100, "%")
        if getCollatzSeqLen(i) > maxSeqLen:
            maxStartNum, maxSeqLen = i, getCollatzSeqLen(i)
    return maxStartNum

if __name__ == "__main__":
    print(sol(10**6))