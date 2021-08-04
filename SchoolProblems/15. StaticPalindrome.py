class Palindrome:
    @staticmethod
    def check_if_palindrome(string):
        if string == string[::-1]:
            return True
        return False

print(Palindrome.check_if_palindrome("AbA"))
