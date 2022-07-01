# finds num of different ways to make £n using 1p,2p,5p,10p,20p,50p,£1, and £2 coins
def sol(n):
    n = int(n*100)
    solution = [1 for i in range(n+1)]
    for coin in [2, 5, 10, 20, 50, 100, 200]:
        for i in range(coin, n+1):
            if coin <= i:
                solution[i] += solution[i-coin]
    return solution[-1]

if __name__ == "__main__":
    assert sol(0.01) == 1
    assert sol(0.02) == 2
    assert sol(0.03) == 2
    assert sol(0.04) == 3
    assert sol(0.05) == 4
    print(sol(2))