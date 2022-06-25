# sum of all integers that cannot be expressed as the sum of two abundant integers
def sol():
    n = 28123
    d = {x:1 for x in range(1, n)}
    for i in range(2, n):
        for j in range(i, n, i):
            d[j] += i
    d = {x:d[x]-x for x in range(1, n)}
    d = [x for x in d if d[x] > x]

    result = set(range(n))
    for i in range(len(d)):
        if i % 500 == 0:
            print(i/len(d)*100, "%")
        for j in range(i, len(d)):
            abundantSum = d[i] + d[j]
            result.discard(abundantSum)
            if abundantSum > n:
                break
    return sum(result)

if __name__ == "__main__":
    print(sol())