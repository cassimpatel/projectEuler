# finds number of distinct terms a^b for 2 <=a,b<=n
def sol(n):
    results = set([])
    for a in range(2, n+1):
        for b in range(2, n+1):
            results.add(a**b)
    return len(results)

if __name__ == "__main__":
    assert sol(5) == 15
    print(sol(100))