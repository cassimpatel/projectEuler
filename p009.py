# product abc for pythagorean triplet where a<b<c and a+b+c=n
def sol(n):
    # since we know a<b<c, we know a<=n/3, b<=n/2
    for a in range(1, int(n/3)):
        for b in range(1, int(n/2)):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a*b*c

if __name__ == "__main__":
    assert sol(12) == 60
    print(sol(1000))