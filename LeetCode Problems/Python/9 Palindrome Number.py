#9. Palindrome Number
def isPalindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False


