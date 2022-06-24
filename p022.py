from urllib.request import urlopen

inputURL = "https://projecteuler.net/project/resources/p022_names.txt"

# gets the alphabetical value of a name
def alphaValue(name):
    return sum([ord(x)-64 for x in name])
    
# finds weighted sum of names in a file
def sol():
    names = urlopen(inputURL).read().decode("utf-8")
    names = [x[1:-1] for x in names.split(",")]
    names.sort()

    nameSum = 0
    for i in range(len(names)):
        nameSum += (i+1) * alphaValue(names[i])
    return nameSum

if __name__ == "__main__":
    assert alphaValue("COLIN") == 53
    print(sol())