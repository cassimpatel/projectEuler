# sum of all amicable numbers under n
def sol(n):
    d = {x:1 for x in range(1, n)}
    for i in range(2, n):
        if i % 1000 == 0:
            print(i/n*100, "%")
        for j in range(i, n, i):
            d[j] += i
    # print(d)
    d = {x:d[x]-x for x in range(1, n)}
    amicableSum = 0
    for i in range(1, n):
        if i != d[i] and d[i] in d and d[d[i]] == i:
            amicableSum += i
    return amicableSum

if __name__ == "__main__":
    print(sol(10000))