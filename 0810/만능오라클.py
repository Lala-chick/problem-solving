import sys

strings = sys.stdin.readline().rstrip().split("What")
for string in strings:
    if '?' in string:
        idx = string.find("?")
        string = string[:idx+1]
        string = string.replace("?", ".")
        print(f"Forty-two{string}")