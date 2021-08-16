import sys

def inner_palindrome(input_str, start, end):
    while start < end:
        if input_str[start] == input_str[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

def palindrome(input_str, start, end):
    while start < end:
        if input_str[start] == input_str[end]:
            start += 1
            end -= 1
        else:
            fc = inner_palindrome(input_str, start, end-1)
            sc = inner_palindrome(input_str, start+1, end)
            if fc or sc:
                return 1
            else:
                return 2
    return 0

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    string = sys.stdin.readline().rstrip()
    print(palindrome(string, 0, len(string)-1))