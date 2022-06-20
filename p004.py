# whether or not n is palindromic
def isPalindrome(n):
    if type(n) != type("string"):
        n = str(n)
    if len(n) < 2:
        return True
    if n[0] != n[-1]:
        return False
    return isPalindrome(n[1:-1])

# largest palindrome product of two n-digit integers
def sol(n):
    n = 10 ** n - 1
    max = 0
    for i in range(n, 0, -1):
        for j in range(n, i-1, -1):
            if isPalindrome(i*j) and i*j > max:
                max = i*j
                # print(max, i, j)
    return max

if __name__ == "__main__":
    assert sol(2) == 9009
    print(sol(3))