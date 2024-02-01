def is_palindrome(word):
    word = ''.join(c.lower() for c in word )
    return word == word[::-1]