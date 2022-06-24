presets = {
    1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
    11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",
    20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"
}

# letters required to write n as a word
def letters(n):
    result = ""
    if n >= 1000:
        result += presets[int(n/1000)] + "thousand"
        n -= int(n/1000) * 1000
    if n >= 100:
        result += presets[int(n/100)] + "hundred"
        n -= int(n/100) * 100
        if n > 0:
            result += "and"
    if n >= 20:
        result += presets[int(n/10) * 10]
        n -= int(n/10) * 10
    if n > 0:
        result += presets[n]
    return len(result)

# letters required to write numbers 1 to n (inclusive) in words
def sol(n):
    return sum([letters(i) for i in range(1, n+1)])

if __name__ == "__main__":
    assert letters(342) == 23
    assert letters(115) == 20
    assert sol(5) == 19
    print(sol(1000))