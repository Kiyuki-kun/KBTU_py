def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

'''
word1 = "madam"
word2 = "Able was I ere I saw Elba"
word3 = "hello"

print(f"'{word1}' is a palindrome:", is_palindrome(word1))
print(f"'{word2}' is a palindrome:", is_palindrome(word2))
print(f"'{word3}' is a palindrome:", is_palindrome(word3))
'''